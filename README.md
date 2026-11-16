# Gmail Connector

Read-only Gmail profile, message search, and retrieval through a caller-authorized service.

## Install from source

Requires Python 3.11 or newer. From the repository root, run `python -m pip install .`.

Import `GmailServiceConnector` from `mathist_gmail_connector` and pass a mapping from account handles to authorized Gmail services. The adapter exposes `profile`, `list_messages`, and `get_message`. Run the synthetic workflow with `python -m unittest discover -s tests` after installation.

## License

[PolyForm Small Business 1.0.0](LICENSE.md). Preserve the [required notice](NOTICE) when redistributing.
