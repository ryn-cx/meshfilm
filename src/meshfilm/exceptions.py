# TODO: Validate
from __future__ import annotations

from typing import Any


class MeshFilmError(Exception):
    """Base exception for the meshfilm library."""


class HTTPError(MeshFilmError):
    """Raised when an HTTP request fails with an unexpected status code."""


class NoContentError(MeshFilmError):
    """Raised when a response has no meaningful content."""

    def __init__(
        self,
        response: dict[str, Any],
        log_id: str,
    ) -> None:
        """Store the downloaded response so it can be recovered by the caller."""
        self.response = response
        super().__init__(f"Response has no content for {log_id}.")
