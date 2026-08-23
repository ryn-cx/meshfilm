"""PreviewModalVideoTitleGroupModel, strict to a type checker, all-optional at runtime.

A type checker reads the strict model, so every field carries the type and
the requiredness the schema recorded. At runtime the all-optional copy is imported
instead, so a response that has drifted still parses and a field the data is
missing is None despite what its type hint says.
"""

from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import PreviewModalVideoTitleGroupModel as OptionalModel
from .strict_models import PreviewModalVideoTitleGroupModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Boxart,
        ContentAdvisory,
        ContextualSynopsis,
        CurrentEpisode,
        Data,
        Episodes,
        Error,
        Extensions,
        ParentSeason,
        PreviewModalVideoTitleGroupModel,
        Reason,
        Seasons,
        Videos,
    )
else:
    from .optional_models import (
        Boxart,
        ContentAdvisory,
        ContextualSynopsis,
        CurrentEpisode,
        Data,
        Episodes,
        Error,
        Extensions,
        ParentSeason,
        PreviewModalVideoTitleGroupModel,
        Reason,
        Seasons,
        Videos,
    )

__all__ = [
    "Boxart",
    "ContentAdvisory",
    "ContextualSynopsis",
    "CurrentEpisode",
    "Data",
    "Episodes",
    "Error",
    "Extensions",
    "ParentSeason",
    "PreviewModalVideoTitleGroupModel",
    "Reason",
    "Seasons",
    "Videos",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> PreviewModalVideoTitleGroupModel:
    """Read a downloaded file into PreviewModalVideoTitleGroupModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
