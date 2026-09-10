from __future__ import annotations

from typing import Any


class MeshfilmError(Exception):
    """Base exception for Meshfilm."""

    response: str | dict[str, Any] | None = None


class HTTPError(MeshfilmError):
    """Raised when HTTP request fails with unexpected status code."""

    def __init__(
        self,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize HTTPError."""
        self.status_code = status_code
        self.response = response
        super().__init__(f"Unexpected response status code: {status_code}")


class ResourceNotFoundError(HTTPError):
    """Raised when the API reports that the requested resource does not exist."""


class TitleNotFoundError(ResourceNotFoundError):
    """Raised when the requested title does not exist."""


class ShowNotFoundError(ResourceNotFoundError):
    """Raised when the requested show does not exist."""


class SeasonNotFoundError(ResourceNotFoundError):
    """Raised when the requested season does not exist."""


class InvalidArgsError(MeshfilmError):
    """Raised when the requested id is not the kind of video the endpoint takes."""


class NotAShowError(InvalidArgsError):
    """Raised if show_id is not a show."""

    def __init__(
        self,
        show_id: int | None,
        typename: str,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize NotAShowError."""
        self.show_id = show_id
        self.typename = typename
        self.response = response
        super().__init__(f"{show_id} is a {typename}, not a show")


class NotASeasonError(InvalidArgsError):
    """Raised if season_id is not a season."""

    def __init__(
        self,
        season_id: int | None,
        typename: str,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize NotASeasonError."""
        self.season_id = season_id
        self.typename = typename
        self.response = response
        super().__init__(f"{season_id} is a {typename}, not a season")


class NotATitleError(InvalidArgsError):
    """Raised if title_id is not a show or a movie."""

    def __init__(
        self,
        title_id: int | None,
        typename: str,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize NotATitleError."""
        self.title_id = title_id
        self.typename = typename
        self.response = response
        super().__init__(f"{title_id} is a {typename}, not a show or a movie")
