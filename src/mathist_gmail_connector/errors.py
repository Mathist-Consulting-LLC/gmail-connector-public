class ConnectorFailure(Exception):
    """Failure to resolve an authorized Gmail service."""

    def __init__(self, code: str):
        self.code = code
        super().__init__(code)
