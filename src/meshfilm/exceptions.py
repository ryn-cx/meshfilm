# TODO: Validate
"""Exception classes for meshfilm."""


class MeshFilmError(Exception):
    """Base exception for the meshfilm library."""


class HTTPError(MeshFilmError):
    """Raised when an HTTP request fails with an unexpected status code."""


class GraphQLNotFoundError(MeshFilmError):
    """Raised when a page has no embedded GraphQL cache.

    Usually means the page was geo/robot-gated (a challenge or redirect was
    served instead of the real title page), or Netflix changed the page format.
    """
