from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, Field

class ContentAdvisory(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    maturity_level: int = Field(..., alias='maturityLevel')

class UnifiedEntity(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    unified_entity_id: str = Field(..., alias='unifiedEntityId')
    content_advisory: ContentAdvisory = Field(..., alias='contentAdvisory')
    video_id: int = Field(..., alias='videoId')

class Artwork(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    height: int
    key: str
    url: str
    width: int

class ContextualArtwork(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    field_id: str = Field(..., alias='_id')
    artwork: Artwork
    image_congruence_context: None = Field(..., alias='imageCongruenceContext')

class Node1(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    display_string: str = Field(..., alias='displayString')
    unified_entity: UnifiedEntity = Field(..., alias='unifiedEntity')
    contextual_artwork: ContextualArtwork = Field(..., alias='contextualArtwork')

class Edge1(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    node: Node1

class PageInfo(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    end_cursor: str = Field(..., alias='endCursor')
    has_next_page: bool = Field(..., alias='hasNextPage')

class Entities(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    edges: list[Edge1]
    page_info: PageInfo = Field(..., alias='pageInfo')
    total_count: int = Field(..., alias='totalCount')

class LoggingData(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    section_logging_id: str = Field(..., alias='sectionLoggingId')
    track_id: int = Field(..., alias='trackId')

class SectionTreatment(BaseModel):
    field__typename: str = Field(..., alias='__typename')

class Node(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    display_string: str = Field(..., alias='displayString')
    entities: Entities
    id: str
    logging_data: LoggingData = Field(..., alias='loggingData')
    section_treatment: SectionTreatment = Field(..., alias='sectionTreatment')

class Edge(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    node: Node

class Sections(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    edges: list[Edge]
    total_count: int = Field(..., alias='totalCount')

class TrackingInfo(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    request_id: str = Field(..., alias='requestId')

class Page(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    field_id: str = Field(..., alias='_id')
    display_string: None = Field(..., alias='displayString')
    expires: AwareDatetime
    sections: Sections
    tracking_info: TrackingInfo = Field(..., alias='trackingInfo')

class Data(BaseModel):
    page: Page

class SearchPageResultsModel(BaseModel):
    data: Data
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
