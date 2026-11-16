from importlib.util import find_spec
import unittest
from unittest.mock import Mock

from mathist_gmail_connector import ConnectorFailure, GmailServiceConnector


class ConnectorTests(unittest.TestCase):
    def test_invoice_lookup(self):
        self.assertIsNone(find_spec("library_room_booking"))
        service = Mock()
        users = service.users.return_value
        messages = users.messages.return_value
        profile = users.getProfile.return_value
        search = messages.list.return_value
        fetch = messages.get.return_value
        profile.execute.return_value = {"emailAddress": "billing@example.invalid"}
        search.execute.return_value = {"messages": [{"id": "invoice"}]}
        fetch.execute.return_value = {"id": "invoice"}
        connector = GmailServiceConnector({"billing": service})

        self.assertEqual(connector.profile(account="billing"), profile.execute.return_value)
        self.assertEqual(connector.list_messages(account="billing", query="subject:invoice",
                                                 page_token="next", max_results=4),
                         search.execute.return_value)
        self.assertEqual(connector.get_message(account="billing", message_id="invoice"),
                         fetch.execute.return_value)
        users.getProfile.assert_called_once_with(userId="me")
        messages.list.assert_called_once_with(userId="me", q="subject:invoice",
                                              pageToken="next", maxResults=4)
        messages.get.assert_called_once_with(userId="me", id="invoice", format="full")
        for request in (profile, search, fetch):
            request.execute.assert_called_once_with(num_retries=0)

    def test_unknown_account_has_no_fallback(self):
        service = Mock()
        connector = GmailServiceConnector({"billing": service})
        with self.assertRaises(ConnectorFailure) as failure:
            connector.profile(account="missing")
        self.assertEqual(failure.exception.code, "authentication_required")
        service.users.assert_not_called()
