# TODO: Validate
from __future__ import annotations


class MeshFilmError(Exception):
    """Base exception for the meshfilm library."""


class HTTPError(MeshFilmError):
    """Raised when an HTTP request fails with an unexpected status code."""
