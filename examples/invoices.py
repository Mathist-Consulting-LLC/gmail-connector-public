"""Standalone invoice reader with fake service; never accesses Gmail."""
from mathist_gmail_connector import GmailServiceConnector, ConnectorFailure

calls = []
class Request:
    def __init__(self, value): self.value = value
    def execute(self, *, num_retries):
        assert num_retries == 0
        return self.value

class FakeService:
    def users(self): return self
    def messages(self): return self
    def getProfile(self, **kwargs):
        assert kwargs == {'userId': 'me'}
        calls.append('profile')
        return Request({'emailAddress': 'invoices@example.invalid'})
    def list(self, **kwargs):
        assert kwargs['userId'] == 'me' and kwargs['q'] == 'subject:invoice'
        assert kwargs['maxResults'] == 2
        token = kwargs['pageToken']
        assert token in (None, 'second')
        calls.append('list')
        if token is None:
            return Request({'messages': [{'id': 'invoice-one'}], 'nextPageToken': 'second'})
        return Request({'messages': [{'id': 'invoice-two'}]})
    def get(self, **kwargs):
        assert kwargs['userId'] == 'me' and kwargs['format'] == 'full'
        assert kwargs['id'] in ('invoice-one', 'invoice-two')
        calls.append('get')
        return Request({'id': kwargs['id'], 'payload': {'mimeType': 'text/plain'}})

connector = GmailServiceConnector({'invoice-reader': FakeService()})
profile = connector.profile(account='invoice-reader')
assert profile['emailAddress'] == 'invoices@example.invalid'
print('profile matched')
token, seen_tokens, identities = None, set(), []
for page_number in range(2):
    page = connector.list_messages(account='invoice-reader', query='subject:invoice',
                                   page_token=token, max_results=2)
    for row in page.get('messages', []):
        if row['id'] not in identities:
            if len(identities) >= 4: raise RuntimeError('Message budget exceeded')
            message = connector.get_message(account='invoice-reader', message_id=row['id'])
            assert message['id'] == row['id']
            identities.append(message['id'])  # A real interpreter validates untrusted content separately.
    token = page.get('nextPageToken')
    if not token: break
    if token in seen_tokens: raise RuntimeError('Repeated page token')
    seen_tokens.add(token)
else:
    raise RuntimeError('Page budget exceeded')
print('selected=' + ','.join(identities) + '; pages=2')
try:
    connector.profile(account='missing')
except ConnectorFailure as error:
    assert error.code == 'authentication_required'
    print('unknown account=' + error.code + '; no fallback')
else:
    raise AssertionError('Expected unknown account failure')
assert calls == ['profile', 'list', 'get', 'list', 'get']
