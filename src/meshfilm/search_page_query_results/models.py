# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import SearchPageQueryResultsModel as OptionalModel
from .strict_models import SearchPageQueryResultsModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Artwork,
        ContentAdvisory,
        ContextualArtwork,
        Data,
        Edge,
        Edge1,
        Entities,
        LoggingData,
        Node,
        Node1,
        Page,
        PageInfo,
        SearchPageQueryResultsModel,
        SectionTreatment,
        Sections,
        TrackingInfo,
        UnifiedEntity,
    )
else:
    from .optional_models import (
        Artwork,
        ContentAdvisory,
        ContextualArtwork,
        Data,
        Edge,
        Edge1,
        Entities,
        LoggingData,
        Node,
        Node1,
        Page,
        PageInfo,
        SearchPageQueryResultsModel,
        SectionTreatment,
        Sections,
        TrackingInfo,
        UnifiedEntity,
    )

__all__ = [
    "Artwork",
    "ContentAdvisory",
    "ContextualArtwork",
    "Data",
    "Edge",
    "Edge1",
    "Entities",
    "LoggingData",
    "Node",
    "Node1",
    "Page",
    "PageInfo",
    "SearchPageQueryResultsModel",
    "SectionTreatment",
    "Sections",
    "TrackingInfo",
    "UnifiedEntity",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> SearchPageQueryResultsModel:
    """Read a downloaded file into SearchPageQueryResultsModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
