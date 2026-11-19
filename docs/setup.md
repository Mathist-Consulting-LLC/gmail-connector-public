# Supplying an authorized Gmail service

The [quickstart](quickstart.md) needs no credentials. For optional live use,
provision a Gmail API application and read permission through the provider's
supported process in your own account. The caller creates an already authorized
service implementing the fluent discovery interface in [API](api.md), then maps
an opaque account handle to it. This library neither provisions that account nor
installs a Google SDK. Use the official
[Gmail authorization guide](https://developers.google.com/workspace/gmail/api/auth/about-auth)
and [Python quickstart](https://developers.google.com/workspace/gmail/api/quickstart/python)
for the caller's independently managed SDK/application setup. Reading full message
content needs a content-readable permission such as gmail.readonly; metadata-only
credentials cannot be assumed to support every query/full-content workflow.

Keep the chosen SDK version pinned in your consumer. Supply the authorized
service to `GmailServiceConnector({'invoice-reader': service})`; the connector
always uses userId='me', so verify that this service represents the intended
mailbox before use. `profile` returns the provider profile, but this connector
does not itself compare an expected mailbox address. The caller must check it.
Multiple services may be bound to distinct explicit handles; never use fallback
accounts when one fails. Mapping immutability does not validate service identity.

The service must expose `users().getProfile(...)`,
`users().messages().list(...)`, `users().messages().get(...)`, each returning a
request with `execute(num_retries=0)`. The [fake service](../examples/invoices.py)
is a complete offline implementation. A live caller replaces its fake mapping
with real authorized services; no deployment credentials belong in this repo.

The caller configures credential storage/rotation/refresh, read-only access,
TLS/hostname validation, HTTP deadlines, decompression/response/resource bounds,
socket cleanup, proxy policy and private logs. The connector's retry argument
controls request-level SDK retries only. Credential refresh or a lower HTTP layer
can independently retry; configure and validate those layers yourself. A blocking
execute call is not interrupted by this connector. Share sessions across threads
only if the caller's selected service/transport supports it.

Construction performs no provider I/O. Calls execute synchronously; the connector
has no close method, background work or storage. The caller closes its service,
HTTP resources and credential owner at application shutdown. Live mailbox checks
need separate authorization and privacy handling; the supplied tests do not
access mail. Generic mail access is separate from the optional booking adapter in
[Library Tools](https://github.com/Mathist-Consulting-LLC/library-room-booking-public).
