from __future__ import annotations

from inspect import Parameter, signature
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable

    from meshfilm import Meshfilm


class BaseEndpoint:
    """Base class for API endpoints."""

    WEBSITE = "Netflix"

    @property
    def default_log_id(self) -> str:
        """Get the log id of the endpoint itself, without any arguments."""
        return f"{self.WEBSITE} - {self.__class__.__name__}"

    def __init__(self, client: Meshfilm) -> None:
        """Initialize the endpoint with the Meshfilm client."""
        self._client = client

    @staticmethod
    def non_default_args(
        endpoint_method: Callable[..., Any],
        caller_locals: dict[str, Any],
    ) -> dict[str, Any]:
        """Return the args that are changed from their default values."""
        return {
            parameter_name: caller_locals[parameter_name]
            for parameter_name, parameter in signature(
                endpoint_method,
            ).parameters.items()
            if parameter.default is not Parameter.empty
            and parameter_name in caller_locals
            and caller_locals[parameter_name] != parameter.default
        }

    def get_log_id(
        self,
        endpoint: Callable[..., Any],
        caller_locals: dict[str, Any],
    ) -> str:
        """Get the log id."""
        required_args = {
            parameter_name: caller_locals[parameter_name]
            for parameter_name, parameter in signature(endpoint).parameters.items()
            if parameter.default is Parameter.empty and parameter_name in caller_locals
        }
        logged_args = {
            **required_args,
            **self.non_default_args(endpoint, caller_locals),
        }
        formatted_args = [
            f"{parameter_name}={value!r}"
            for parameter_name, value in logged_args.items()
        ]
        if not formatted_args:
            return self.default_log_id
        return f"{self.default_log_id} ({' '.join(formatted_args)})"
