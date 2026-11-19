# Python API reference

Import from `mathist_gmail_connector` unless a module is shown. This inventory is derived from
current source declarations. Defaults, keyword-only arguments and record fields
are listed below; caller responsibilities are specified in [setup](setup.md).

## `mathist_gmail_connector`

[Source](../src/mathist_gmail_connector/__init__.py)

### `GmailServiceConnector`

```python
GmailServiceConnector.__init__(self, services: Mapping[str, object])
```

```python
GmailServiceConnector.profile(self, *, account: str) -> dict
```

```python
GmailServiceConnector.list_messages(self, *, account: str, query: str, page_token: str | None, max_results: int) -> dict
```

```python
GmailServiceConnector.get_message(self, *, account: str, message_id: str) -> dict
```

## `mathist_gmail_connector.errors`

[Source](../src/mathist_gmail_connector/errors.py)

### `ConnectorFailure`

```python
ConnectorFailure.__init__(self, code: str)
```
