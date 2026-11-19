# Fresh consumer quickstart

Use Python 3.11+ with pip/venv and Git.
The provisioning interpreter needs pip 22.3+ (`--python` support); it installs
into isolated venvs even on systems without ensurepip.
Commands below use a POSIX shell; on Windows use the venv's Scripts/python.exe
and equivalent copy/path commands. Python needs IANA timezone data for booking;
Linux/macOS normally supply it, while other consumers may install tzdata.
The recorded validation platform is described in [validation](validation.md).

Run in a new work directory. Resolve main once, record its full Git SHA, and use
that exact revision again to reproduce the source. The commands deliberately
build artifacts locally, without registry publication. The first build downloads
only the pinned build dependency; subsequent consumer installation is offline.

```sh
git clone https://github.com/Mathist-Consulting-LLC/gmail-connector-public.git
cd gmail-connector-public
REVISION=$(git rev-parse HEAD)
printf '%s\n' "$REVISION" > ../source-revision.txt
git checkout --detach "$REVISION"
SOURCE=$(pwd)
PIP_PYTHON=$(command -v python3)
"$PIP_PYTHON" -m pip --version
"$PIP_PYTHON" -m venv --without-pip ../build-env
BUILD_PYTHON="$(cd ../build-env && pwd)/bin/python"
"$PIP_PYTHON" -m pip --python "$BUILD_PYTHON" install --require-hashes -r requirements-build.txt
mkdir -p ../wheels
WHEELS="$(cd ../wheels && pwd)"
"$PIP_PYTHON" -m pip --python "$BUILD_PYTHON" wheel --no-build-isolation --no-deps . --wheel-dir "$WHEELS"
cd ..
mkdir consumer
cd consumer
"$PIP_PYTHON" -m venv --without-pip .venv
PYTHON="$(pwd)/.venv/bin/python"
"$PIP_PYTHON" -m pip --python "$PYTHON" install --no-index --find-links "$WHEELS" 'mathist-gmail-connector==0.0.0.dev1'
"$PYTHON" -I -c 'import pathlib,sys,mathist_gmail_connector as p; assert pathlib.Path(p.__file__).is_relative_to(sys.prefix); print("installed package")'
cp "$SOURCE/examples/invoices.py" .
"$PYTHON" -I invoices.py
```

Expected output (after installation messages):

```text
installed package
profile matched
selected=invoice-one,invoice-two; pages=2
unknown account=authentication_required; no fallback
```

For a minimal first call, instantiate the example's FakeService and call
`GmailServiceConnector({'invoice-reader': FakeService()}).profile(account='invoice-reader')`.
The same script then demonstrates a bounded two-page invoice scan, selected
message retrieval and an unknown-account failure with no service access.
No booking component, SDK, credentials or mailbox access is involved.

Keep `source-revision.txt`, built artifact SHA256 and your consumer lockfile in
your own reproducibility record. A future same-version source build can differ;
Git SHA plus artifact hash is the pin. Read [setup](setup.md) before replacing
fixtures, [API](api.md) for returned shapes, and [recovery](recovery.md) for errors.
These commands create only local environments/artifacts. To clean up, remove
those directories after retaining any records you need.
