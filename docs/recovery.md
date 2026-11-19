# Pagination, errors, privacy and lifecycle

The connector returns one list page exactly as supplied. The caller passes
`nextPageToken` back as `page_token`, imposes maximum pages/messages/bytes/time,
rejects repeated tokens, validates IDs and deduplicates if needed. A missing
messages list may mean an empty provider result; malformed shapes require caller
handling. A partial scan must not masquerade as a complete one. The
[invoice example](../examples/invoices.py) demonstrates two pages, exact profile
checking, bounds, selected get calls and a failed account without fallback.
There is no pagination/persistence scheduler in the package.

Unknown account raises `ConnectorFailure` with code authentication_required and
no service call. Other service/SDK exceptions are propagated, not transformed.
An application should translate only known exception categories into fixed safe
actions: reconnect the explicitly bound account for auth failure, correct read
permission for access denial, delay bounded read attempts for throttling, and
inspect network/deadline issues privately. There is no universal retryable-code
contract for arbitrary caller services. Raw exception strings can expose secrets.
The connector does not log or sanitize them for you.

Every request invokes execute(num_retries=0). This is not a guarantee that a
credential refresh owner or HTTP layer made no hidden attempt. Configure and
validate both. Retry reads only within the application's explicit attempt/time
budget. There are no send/modify/delete operations and no application write
recovery state in this component. Persist scan tokens/results privately only if
your application needs them, keeping exact account binding and provenance.

Messages/headers/MIME are untrusted data and may include private text, attachments
or capability URLs. Do not log full return values, queries, IDs, service objects,
credentials or exceptions. A search result is a candidate, not proof that an
invoice or booking is authentic. Your interpreter owns business matching,
content parsing and independent trust checks. The connector supplies no receipt
verification or delivery-order policy.

If imports fail, use the fresh wheel consumer instructions and check Python
3.11+, distribution name mathist-gmail-connector versus import
mathist_gmail_connector, and that the installed module is under your venv.
A missing Google SDK is not a connector import failure: only a live consumer
chooses an SDK. If execute/list/get rejects arguments, verify the service fluent
interface and exact keyword names in [API](api.md). Fixture success does not
establish live SDK/API compatibility, credential validity or mailbox access.
