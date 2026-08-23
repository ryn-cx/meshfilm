"""PreviewModalEpisodeSelectorSeasonEpisodesModel, strict to a type checker, all-optional at runtime.

A type checker reads the strict model, so every field carries the type and
the requiredness the schema recorded. At runtime the all-optional copy is imported
instead, so a response that has drifted still parses and a field the data is
missing is None despite what its type hint says.
"""

from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import PreviewModalEpisodeSelectorSeasonEpisodesModel as OptionalModel
from .strict_models import PreviewModalEpisodeSelectorSeasonEpisodesModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Artwork,
        ContextualSynopsis,
        CurrentEpisode,
        Data,
        Edge,
        Episodes,
        Error,
        Extensions,
        Node,
        PageInfo,
        ParentShow,
        PreviewModalEpisodeSelectorSeasonEpisodesModel,
        Video,
    )
else:
    from .optional_models import (
        Artwork,
        ContextualSynopsis,
        CurrentEpisode,
        Data,
        Edge,
        Episodes,
        Error,
        Extensions,
        Node,
        PageInfo,
        ParentShow,
        PreviewModalEpisodeSelectorSeasonEpisodesModel,
        Video,
    )

__all__ = [
    "Artwork",
    "ContextualSynopsis",
    "CurrentEpisode",
    "Data",
    "Edge",
    "Episodes",
    "Error",
    "Extensions",
    "Node",
    "PageInfo",
    "ParentShow",
    "PreviewModalEpisodeSelectorSeasonEpisodesModel",
    "Video",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> PreviewModalEpisodeSelectorSeasonEpisodesModel:
    """Read a downloaded file into PreviewModalEpisodeSelectorSeasonEpisodesModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
