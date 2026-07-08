# TODO: Validate
"""Base API endpoint."""

from __future__ import annotations

from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import GAPIBaseModel, GAPIClient

if TYPE_CHECKING:
    from meshfilm import MeshFilm


class BaseEndpoint[T: GAPIBaseModel](GAPIClient[T]):
    """Base class for API endpoints."""

    def __init__(self, client: MeshFilm) -> None:
        """Initialize the endpoint with the MeshFilm client."""
        self._client = client
