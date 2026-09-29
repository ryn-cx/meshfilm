from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any
from uuid import UUID

class ContentAdvisory(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    maturity_level: int | Any = Field(None, alias='maturityLevel', union_mode='left_to_right')

class UnifiedEntity(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    unified_entity_id: str | Any = Field(None, alias='unifiedEntityId', union_mode='left_to_right')
    content_advisory: ContentAdvisory | Any = Field(None, alias='contentAdvisory', union_mode='left_to_right')
    video_id: int | Any = Field(None, alias='videoId', union_mode='left_to_right')

class Artwork(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    key: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')

class ContextualArtwork(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    field_id: str | Any = Field(None, alias='_id', union_mode='left_to_right')
    artwork: Artwork | Any = Field(default=None, union_mode='left_to_right')
    image_congruence_context: Any | None = Field(None, alias='imageCongruenceContext')

class Node1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    display_string: str | Any = Field(None, alias='displayString', union_mode='left_to_right')
    unified_entity: UnifiedEntity | Any = Field(None, alias='unifiedEntity', union_mode='left_to_right')
    contextual_artwork: ContextualArtwork | Any = Field(None, alias='contextualArtwork', union_mode='left_to_right')

class Edge1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    node: Node1 | Any = Field(default=None, union_mode='left_to_right')

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    end_cursor: str | Any = Field(None, alias='endCursor', union_mode='left_to_right')
    has_next_page: bool | Any = Field(None, alias='hasNextPage', union_mode='left_to_right')

class Entities(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    edges: list[Edge1] | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')
    total_count: int | Any = Field(None, alias='totalCount', union_mode='left_to_right')

class LoggingData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    section_logging_id: str | Any = Field(None, alias='sectionLoggingId', union_mode='left_to_right')
    track_id: int | Any = Field(None, alias='trackId', union_mode='left_to_right')

class SectionTreatment(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Node(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    field_id: str | Any = Field(None, alias='_id', union_mode='left_to_right')
    display_string: str | Any = Field(None, alias='displayString', union_mode='left_to_right')
    entities: Entities | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    logging_data: LoggingData | Any = Field(None, alias='loggingData', union_mode='left_to_right')
    section_treatment: SectionTreatment | Any = Field(None, alias='sectionTreatment', union_mode='left_to_right')
    version: Any | None = None

class Edge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    node: Node | Any = Field(default=None, union_mode='left_to_right')

class Sections(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    edges: list[Edge] | Any = Field(default=None, union_mode='left_to_right')
    total_count: int | Any = Field(None, alias='totalCount', union_mode='left_to_right')

class TrackingInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    request_id: UUID | Any = Field(None, alias='requestId', union_mode='left_to_right')

class SearchPageQueryResultsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    field_id: str | Any = Field(None, alias='_id', union_mode='left_to_right')
    display_string: Any | None = Field(None, alias='displayString')
    expires: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    sections: Sections | Any = Field(default=None, union_mode='left_to_right')
    tracking_info: TrackingInfo | Any = Field(None, alias='trackingInfo', union_mode='left_to_right')
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode='wrap')
    @classmethod
    def _capture_raw_input(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
