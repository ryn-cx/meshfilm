# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import PreviewModalEpisodeSelectorModel as OptionalModel
from .strict_models import PreviewModalEpisodeSelectorModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        ContentAdvisory,
        Edge,
        Episodes,
        Node,
        PageInfo,
        PreviewModalEpisodeSelectorModel,
        Reason,
        Seasons,
    )
else:
    from .optional_models import (
        ContentAdvisory,
        Edge,
        Episodes,
        Node,
        PageInfo,
        PreviewModalEpisodeSelectorModel,
        Reason,
        Seasons,
    )

__all__ = [
    "ContentAdvisory",
    "Edge",
    "Episodes",
    "Node",
    "PageInfo",
    "PreviewModalEpisodeSelectorModel",
    "Reason",
    "Seasons",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> PreviewModalEpisodeSelectorModel:
    """Read a downloaded file into PreviewModalEpisodeSelectorModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
