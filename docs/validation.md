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
