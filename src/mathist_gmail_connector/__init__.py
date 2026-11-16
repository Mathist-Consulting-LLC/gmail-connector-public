"""Optional adapter for caller-created Gmail services; no SDK or credentials."""
from types import MappingProxyType
from typing import Mapping

from .errors import ConnectorFailure


class GmailServiceConnector:
    """Bind opaque account handles to already authorized, read-only services.

    The caller creates/configures services, including resource limits, deadlines,
    credential refresh and redacted diagnostics. No account fallback is allowed.
    The service must implement the Gmail discovery client's read-side shape.
    """

    def __init__(self, services: Mapping[str, object]):
        self._services = MappingProxyType(dict(services))

    def _users(self, account: str):
        try:
            service = self._services[account]
        except (KeyError, TypeError):
            raise ConnectorFailure("authentication_required") from None
        return service.users()

    def profile(self, *, account: str) -> dict:
        return self._users(account).getProfile(userId="me").execute(num_retries=0)

    def list_messages(self, *, account: str, query: str,
                      page_token: str | None, max_results: int) -> dict:
        return self._users(account).messages().list(
            userId="me", q=query, pageToken=page_token,
            maxResults=max_results,
        ).execute(num_retries=0)

    def get_message(self, *, account: str, message_id: str) -> dict:
        return self._users(account).messages().get(
            userId="me", id=message_id, format="full",
        ).execute(num_retries=0)
