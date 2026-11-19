# Gmail connector API contract

Import `GmailServiceConnector` and `ConnectorFailure` from
`mathist_gmail_connector`. [Source signatures](python-api.md) are also indexed.
Python 3.11+ is required; there is no JavaScript package or Google SDK dependency.

```python
connector = GmailServiceConnector(services)  # Mapping[str, object]
connector.profile(account='opaque-handle')
connector.list_messages(account='opaque-handle', query='subject:invoice',
                        page_token=None, max_results=10)
connector.get_message(account='opaque-handle', message_id='provider-id')
```

All method arguments are keyword-only. `page_token` and `max_results` must be
supplied; they have no default. Construction copies the mapping and wraps that
copy in a read-only view. Later mapping edits cannot rebind it, but service
objects themselves remain caller-owned mutable objects. There is no implicit
account and no fallback. Unknown/unhashable account selection raises
`ConnectorFailure('authentication_required')` before service access.

| Connector method | Exact service request | Return |
| --- | --- | --- |
| `profile(*,account)` | `service.users().getProfile(userId='me').execute(num_retries=0)` | Provider profile dict, e.g. emailAddress/messagesTotal/threadsTotal/historyId |
| `list_messages(*,account,query,page_token,max_results)` | `service.users().messages().list(userId='me',q=query,pageToken=page_token,maxResults=max_results).execute(num_retries=0)` | Provider list dict, e.g. messages=[{id,threadId}], nextPageToken, resultSizeEstimate |
| `get_message(*,account,message_id)` | `service.users().messages().get(userId='me',id=message_id,format='full').execute(num_retries=0)` | Provider full message dict, e.g. id/threadId/labelIds/snippet/payload |

Return dictionaries are passed through, not copied or validated. Provider fields
are optional/provider-defined, and malformed shapes are the consumer's concern.
The connector does not fetch attachment bodies, parse MIME, validate recipients,
authenticate message origin, infer booking state or decode application content.
Interpret selected messages independently; payload parts/body may be absent.

`ConnectorFailure` exposes `.code` and stringifies that code. Only account lookup
is categorized here. SDK/service/transport exceptions propagate unchanged and
may contain sensitive data; this component does not sanitize them. Never display
or log raw exceptions or return bodies. A wrapper can translate failures into
fixed safe categories for its own application. No retry loop is implemented.

These operations implement GMAIL-BINDING, GMAIL-READS and GMAIL-ERRORS in the
[owning catalog](../requirements/catalog.json); caller boundaries are indexed in
the [charter](component-charter.md). See the [test trace](validation.md#runtime-requirement-trace)
for what existing tests actually cover.
