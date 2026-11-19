# Email Tools component charter

Owner: Mathist Consulting LLC maintainers. Repository: `gmail-connector-public`.
The current repository name and URLs remain in use pending coordinated mapping.
Package names and imports stay unchanged. Retaining the current directory layout
avoids a migration with no functional benefit.

| Area | Responsibility | Boundary |
| --- | --- | --- |
| `src/mathist_gmail_connector` | Existing Python component | Public API reference and synthetic contracts |

| `requirements` | Source-backed acceptance and explanations | JSON is authoritative; protected originals retain provenance |
| `docs`, `examples`, `tests` | Consumer instructions and offline evidence | Fixtures do not prove provider compatibility |

The Gmail component owns only explicit account-to-service selection and three
read calls. It has no SDK/runtime dependencies, parsing rules, booking imports,
credential store, listener, scheduler or network defaults. The caller-created
Gmail service is its upstream contract. Standalone consumers may interpret
invoices or other messages; [Library Tools](https://github.com/Mathist-Consulting-LLC/library-room-booking-public)
is an optional downstream consumer that adds exact tagged-recipient lookup and
booking evidence interpretation. Its workers, storage and UI own composed-flow
acceptance. Unknown account selection fails before service access; no fallback
is permitted. No monitor or live mailbox check is activated.

Expansion point: an additional provider would need its own independently usable
component, public requirements, service contract and isolated tests. Nothing here
implements another provider or sends/modifies mail.

Read [API](api.md), [setup and transport](setup.md), [recovery](recovery.md) and
[validation](validation.md). Acceptance and authorization are separate from
capability detection. Review changes against the original accepted baseline and
actual final diff; preserve all negative tests and state evidence limits.

Owning runtime IDs: GMAIL-BINDING, GMAIL-READS, GMAIL-ERRORS,
GMAIL-CALLER-OWNERSHIP and GMAIL-INDEPENDENT-PACKAGE. Read their authoritative
[records and provenance index](../requirements/README.md) and
[source-backed test trace](validation.md#runtime-requirement-trace).
