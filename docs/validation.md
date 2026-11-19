# Validation and evidence limits

Run the [quickstart](quickstart.md) from a fresh checkout into a separate
consumer. Execute every copied example using the installed wheel/tarball, with
no source-path injection. Expected output is in that guide. Record Git SHA,
artifact hash, runtime versions, actual command results and any skips privately.
All included responses are synthetic; no live provider write or mail access is
required or implied. An offline pass does not establish deployed workflows,
current provider schemas, credential validity or live follow-up delivery.

## Existing suite in an independent install

After the quickstart in the separate consumer:

```sh
cp -R "$SOURCE/tests" connector-tests
"$PYTHON" -I -B -m unittest discover -s connector-tests -p 'test_*.py'
```

It checks exact profile/list/get request arguments, num_retries=0, no booking
imports, unknown-account failure and zero fallback service calls. Build an sdist
with the pinned build interpreter's setuptools.build_meta.build_sdist, rebuild
its wheel in a clean build environment and repeat consumer/examples/tests when
reviewing package input changes. No SDK/service compatibility is claimed by mocks.

## Documentation and requirement review

Check all relative Markdown links, JSON parsing, source-derived signatures,
examples' exact output and public-data hygiene. Compare the final diff with
accepted requirements and preserve existing tests. Independent parent review
owns final approval; an implementer's pass is not that approval. Private source,
original approval and full test logs remain protected. Public contributors can
run package validation using only this repository and the optional public Gmail
component. Requirement statements/explanations live in JSON, not copied policy.

Validated documentation examples on Linux x86_64, CPython 3.12 and Node.js 24.
The declared runtime floors remain Python 3.11 / Node.js 20 where applicable;
this task does not claim testing every supported OS/runtime combination.

## Runtime requirement trace

The [owning catalog](../requirements/catalog.json) is backed by protected
extraction/release authorization resolved through [provenance](../requirements/provenance.json).
Implementation and tests corroborate that contract; neither grants user authority.

| Requirement / criteria | Existing source and evidence | Limits |
| --- | --- | --- |
| GMAIL-BINDING AC1/AC2 | [test_unknown_account_has_no_fallback and test_invoice_lookup](../tests/test_connector.py), [adapter](../src/mathist_gmail_connector/__init__.py) | Synthetic service; no live account binding verified |
| GMAIL-READS AC1/AC2 | [test_invoice_lookup](../tests/test_connector.py) asserts exact request arguments and execute(num_retries=0) | No SDK/provider compatibility claim |
| GMAIL-READS AC3 | Same test compares response dictionaries; [adapter](../src/mathist_gmail_connector/__init__.py) forwards them; [paged invoice example](../examples/invoices.py) chooses pages/messages | Read-only API and absence of interpretation inspected in source; not every malformed shape tested |
| GMAIL-ERRORS AC1 | [unknown-account test](../tests/test_connector.py), [errors](../src/mathist_gmail_connector/errors.py) | Other service exceptions are not categorized by this connector |
| GMAIL-ERRORS AC2 | [Booking Gmail shim and optional delegation tests](https://github.com/Mathist-Consulting-LLC/library-room-booking-public/blob/main/tests/gmail_connector_contracts.py), [booking email contracts](https://github.com/Mathist-Consulting-LLC/library-room-booking-public/blob/main/docs/email.md) | Separate installed core/optional suites cover composition; this connector's two tests alone do not prove translation |
| GMAIL-CALLER-OWNERSHIP AC1/AC2 | [adapter](../src/mathist_gmail_connector/__init__.py), [invoice example](../examples/invoices.py), [charter](component-charter.md); Booking separately owns interpretation | Ownership reviewed against authorization and source; no live credentials, scheduling or delivery tested |
| GMAIL-INDEPENDENT-PACKAGE AC1 | [quickstart](quickstart.md), test_invoice_lookup verifies no booking import, [invoice example](../examples/invoices.py) | Run from a separate installed consumer |
| GMAIL-INDEPENDENT-PACKAGE AC2 | [Booking validation](https://github.com/Mathist-Consulting-LLC/library-room-booking-public/blob/main/docs/validation.md) and [optional installation](https://github.com/Mathist-Consulting-LLC/library-room-booking-public/blob/main/docs/setup.md#optional-gmail-composition) | Requires separate installed Booking core and optional tests; preserved shim supports callers without the extra |

Keep exact command output and artifact hashes privately. Source inspection is
identified separately from executed tests; final independent acceptance remains
with the maintainer's review of the candidate.
