# Email Tools

The existing Gmail connector is the current component. It lets your own application read through a Gmail service you supply; it creates no credentials or network client.

Start with the [developer guide](docs/README.md) for installation, runnable offline examples and API contracts. See the [component map](docs/component-charter.md) and [requirements](requirements/README.md).

Let a Python application search an authorized Gmail account and retrieve messages for its own workflow. This small, read-only connector provides account profile lookup, message search, and full-message retrieval through a Gmail service supplied by your application.

You could use it to find invoice emails, retrieve support messages, or locate reservation receipts. The connector returns Gmail responses so your application can decide how to interpret and store the results.

## Why use it?

Gmail's website lets a person search and read mail. The Gmail API lets software do that work. This connector provides a small common interface around three API operations, with explicit account selection and request-level retries disabled.

It is useful when you want application logic to depend on a narrow mailbox interface that can also be supplied by a fake service during testing. Account handles are bound to their supplied services, and an unknown account produces an authentication error. Your application can use multiple accounts by supplying separate authorized services.

## How it fits into an application

Your application creates the Gmail service, obtains the user's permission, and handles credential storage, refresh, deadlines, and resource limits. It passes the connector an account-to-service mapping.

For an invoice workflow, the application can check the account profile, search using its invoice query, follow returned page tokens, retrieve selected messages, and interpret their contents. The connector accepts the query and returns provider data. The [synthetic invoice test](tests/test_connector.py) shows this sequence without accessing a real mailbox.

The connector exposes read operations only. Gmail access is limited by the permissions on the service your application supplies. The package has no booking-specific dependency.

## Install from source

Requires Python 3.11 or newer. From the repository root, run `python -m pip install .`.

Import `GmailServiceConnector` from `mathist_gmail_connector` and pass a mapping from account handles to authorized Gmail services. The adapter exposes `profile`, `list_messages`, and `get_message`. Run the synthetic workflow with `python -m unittest discover -s tests` after installation.

## License

[PolyForm Small Business 1.0.0](LICENSE.md). Preserve the [required notice](NOTICE) when redistributing.

A script could search invoices, retrieve selected messages and interpret them
using its own business rules. The connector selects an explicitly named account
and passes read requests to an already authorized Gmail service. Your application
owns permissions, credentials, privacy, message interpretation and recovery.

It supports Python 3.11 or newer. Install from a local GitHub checkout with
`python -m pip install .`. The [quickstart](docs/quickstart.md) builds a wheel
and runs a standalone example without Gmail access.

[PolyForm Small Business 1.0.0](LICENSE.md). Preserve the [required notice](NOTICE).
