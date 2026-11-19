# Requirements

[The JSON catalog](catalog.json) owns statements, plain-language explanations,
positive examples and acceptance criteria. Examples explain requirements; they do
not establish acceptance. [Developer contracts](../docs/README.md) describe the
current implementation. [Validation](../docs/validation.md) explains local proof
and its limits.

This is one cohesive component, so one catalog keeps its boundaries together.
No earlier owning structured catalog was present in the source checkout.
The organization/documentation records capture the authorized public work.
The runtime records are the first owning capture of the existing accepted
extraction/release contract, using protected original authorization snapshots;
this does not invent an earlier catalog. Booking-specific requirements stay
with Library Tools. Existing IDs and revisions are preserved. The [public provenance map](provenance.json)
identifies protected original catalog digests and publication qualifications. Public issue [#4](https://github.com/Mathist-Consulting-LLC/gmail-connector-public/issues/4)
routes restoration of the sanitized records; it does not retroactively approve
them. Maintainers retain original catalogs, original sources, approval records,
revision digests and task evidence in protected storage. Historical source pointers, including change authorization, use explicit
`protected-original:sha256:` identifiers resolved in provenance.json. Authority
and decision dates remain original; publication issues are routing context only.
Named deployment references are protected. No test or historical acceptance criterion is waived by publication.
Live compatibility, composed application adoption and independent review require
separate evidence. New organization and documentation obligations come from
[#4](https://github.com/Mathist-Consulting-LLC/gmail-connector-public/issues/4) and [#3](https://github.com/Mathist-Consulting-LLC/gmail-connector-public/issues/3), with separately authorized implementation.

For a proposed change, identify affected IDs and stable acceptance IDs, compare
the accepted baseline, record authority/reason/impact and advance a revision for
normative changes. Preserve tombstones and earlier history. Never change a test
expectation merely to make a regression pass. Public consumers need no access
to protected evidence to install, use or contribute to the package.

Runtime navigation (formal statements, explanations and positive examples remain
in JSON):

| Stable ID | Contract and evidence |
| --- | --- |
| GMAIL-BINDING | [Catalog](catalog.json), [account API](../docs/api.md), [trace](../docs/validation.md#runtime-requirement-trace) |
| GMAIL-READS | [Catalog](catalog.json), [read API](../docs/api.md), [trace](../docs/validation.md#runtime-requirement-trace) |
| GMAIL-ERRORS | [Catalog](catalog.json), [recovery](../docs/recovery.md), [trace](../docs/validation.md#runtime-requirement-trace) |
| GMAIL-CALLER-OWNERSHIP | [Catalog](catalog.json), [charter](../docs/component-charter.md), [trace](../docs/validation.md#runtime-requirement-trace) |
| GMAIL-INDEPENDENT-PACKAGE | [Catalog](catalog.json), [quickstart](../docs/quickstart.md), [trace](../docs/validation.md#runtime-requirement-trace) |

Caller transport/resource/deadline recommendations in the setup guide describe
operational integration concerns. They add no accepted extraction requirements
for new limits, cancellation, retries or connector policy.
