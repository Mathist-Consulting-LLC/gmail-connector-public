# Consumer composition and extension

Use the standalone [invoice example](../examples/invoices.py) as a minimal
non-booking consumer: bind one service, check profile, scan a bounded query,
fetch explicit IDs and pass selected provider dictionaries to your own
interpreter. Replace the fake service only when authorization and the setup
contract are satisfied. Do not embed your credentials, sender identities or
message interpretation in the connector.

An adapter may wrap a caller-created service to add fixed safe error categories,
bounds or transport ownership. Preserve explicit account selection and
execute(num_retries=0). Tests must assert every exact request keyword and zero
service calls for an unknown account. Alternate email providers need their own
scope, service contract and independently usable component; Gmail-shaped calls
are not a universal mailbox protocol. No additional provider is implemented here.

Booking-specific matching and receipt semantics live in
[Library Tools](https://github.com/Mathist-Consulting-LLC/library-room-booking-public),
which can consume this package through its optional gmail extra. Verify that seam
in installed consumers whenever account/failure contracts change. The application
still owns member/operator authority, storage and updates.

A coordinated repository rename should update clone instructions, cross-repo
Gmail links, charters, requirement routing and any owner-managed monitor target.
Keep distribution/import names stable and do not publish a registry artifact as
part of a documentation change. No monitoring is activated here.
