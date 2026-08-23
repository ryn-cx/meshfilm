# TODO: Validate
"""Exceptions."""

from __future__ import annotations

from typing import Any


# TODO: Validate
class MeshfilmError(Exception):
    """Base exception for Meshfilm."""

    response: str | dict[str, Any] | None = None


# TODO: Validate
class HTTPError(MeshfilmError):
    """Raised when HTTP request fails with unexpected status code."""

    # TODO: Validate
    def __init__(
        self,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize the HTTPError with the status code and response body."""
        self.status_code = status_code
        self.response = response
        super().__init__(f"Unexpected response status code: {status_code}")


# TODO: Validate
class ResourceNotFoundError(HTTPError):
    """Raised when the API reports that the requested resource does not exist."""


# TODO: Validate
class VideoNotFoundError(ResourceNotFoundError):
    """Raised when the requested video does not exist."""

    # TODO: Validate
    def __init__(
        self,
        video_id: int,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the video id and the originating response."""
        self.video_id = video_id
        super().__init__(status_code, response)


# TODO: Validate
class ShowNotFoundError(ResourceNotFoundError):
    """Raised when the requested show does not exist."""

    # TODO: Validate
    def __init__(
        self,
        show_id: int,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the show id and the originating response."""
        self.show_id = show_id
        super().__init__(status_code, response)


# TODO: Validate
class SeasonNotFoundError(ResourceNotFoundError):
    """Raised when the requested season does not exist."""

    # TODO: Validate
    def __init__(
        self,
        season_id: int,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the season id and the originating response."""
        self.season_id = season_id
        super().__init__(status_code, response)


# TODO: Validate
class InvalidFileError(MeshfilmError):
    """Raised when a downloaded file is not for what was requested."""

    # TODO: Validate
    def __init__(
        self,
        field: str,
        expected: object,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the field, the value it should hold, and the response."""
        self.field = field
        self.expected = expected
        self.response = response
        super().__init__(f"Downloaded file is not for {field} {expected!r}")
