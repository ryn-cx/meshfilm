# TODO: Validate
"""Contains BaseEndpoint."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any

from good_ass_pydantic_integrator import GAPIBaseModel, GAPIClient

from meshfilm.constants import FILES_PATH
from meshfilm.exceptions import NoContentError

if TYPE_CHECKING:
    from meshfilm import Meshfilm


class BaseEndpoint[T: GAPIBaseModel](GAPIClient[T]):
    """Base class for API endpoints."""

    JSON_FILES_ROOT = FILES_PATH

    def __init__(self, client: Meshfilm) -> None:
        """Initialize the endpoint with the MeshFilm client."""
        self._client = client

    @staticmethod
    @abstractmethod
    def has_content(*args: Any, **kwargs: Any) -> bool:  # noqa: ANN401
        """Return whether the response has meaningful content."""

    def _parse_or_raise(
        self,
        response: dict[str, Any],
        log_id: str,
        *content_args: Any,  # noqa: ANN401
    ) -> T:
        """Parse `response`, or raise `NoContentError` if it is empty.

        `content_args` are forwarded to `has_content` for endpoints whose
        emptiness check depends on the requested identifiers.

        Raises:
            NoContentError: If `has_content` is false.
        """
        if not self.has_content(response, *content_args):
            raise NoContentError(response, log_id)
        return self.parse(response)
