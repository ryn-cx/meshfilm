# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import PreviewModalEpisodeSelectorSeasonEpisodesModel as OptionalModel
from .strict_models import PreviewModalEpisodeSelectorSeasonEpisodesModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Artwork,
        ContextualSynopsis,
        CurrentEpisode,
        Edge,
        Episodes,
        Node,
        PageInfo,
        ParentShow,
        PreviewModalEpisodeSelectorSeasonEpisodesModel,
    )
else:
    from .optional_models import (
        Artwork,
        ContextualSynopsis,
        CurrentEpisode,
        Edge,
        Episodes,
        Node,
        PageInfo,
        ParentShow,
        PreviewModalEpisodeSelectorSeasonEpisodesModel,
    )

__all__ = [
    "Artwork",
    "ContextualSynopsis",
    "CurrentEpisode",
    "Edge",
    "Episodes",
    "Node",
    "PageInfo",
    "ParentShow",
    "PreviewModalEpisodeSelectorSeasonEpisodesModel",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> PreviewModalEpisodeSelectorSeasonEpisodesModel:
    """Read a downloaded file into PreviewModalEpisodeSelectorSeasonEpisodesModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
