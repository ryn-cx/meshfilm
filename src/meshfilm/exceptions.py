# TODO: Validate
from __future__ import annotations


class MeshFilmError(Exception):
    """Base exception for the meshfilm library."""


class HTTPError(MeshFilmError):
    """Raised when an HTTP request fails with an unexpected status code."""

    def __init__(self, status_code: int, body: str) -> None:
        """Initialize the HTTPError with the status code and response body."""
        self.status_code = status_code
        self.body = body
        super().__init__(f"Unexpected response status code: {status_code}\n{body}")


class InvalidFileError(MeshFilmError):
    """Raised when a downloaded file does not match what was requested."""

    def __init__(self, field: str, expected: object = None) -> None:
        """Initialize the InvalidFileError with the field and its expected value.

        `expected` is left out when the check is only that the field has a value.
        """
        self.field = field
        self.expected = expected
        if expected is None:
            super().__init__(f"Downloaded file has no {field}")
        else:
            super().__init__(f"Downloaded file is not for {field} {expected!r}")
