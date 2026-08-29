from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any

class ContentAdvisory(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    maturity_level: int | None = Field(None, alias='maturityLevel')

class UnifiedEntity(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    unified_entity_id: str | None = Field(None, alias='unifiedEntityId')
    content_advisory: ContentAdvisory | None = Field(None, alias='contentAdvisory')
    video_id: int | None = Field(None, alias='videoId')

class Artwork(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    height: int | None = None
    key: str | None = None
    url: str | None = None
    width: int | None = None

class ContextualArtwork(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    field_id: str | None = Field(None, alias='_id')
    artwork: Artwork | None = None
    image_congruence_context: Any | None = Field(None, alias='imageCongruenceContext')

class Node1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    display_string: str | None = Field(None, alias='displayString')
    unified_entity: UnifiedEntity | None = Field(None, alias='unifiedEntity')
    contextual_artwork: ContextualArtwork | None = Field(None, alias='contextualArtwork')

class Edge1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    node: Node1 | None = None

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    end_cursor: str | None = Field(None, alias='endCursor')
    has_next_page: bool | None = Field(None, alias='hasNextPage')

class Entities(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    edges: list[Edge1] | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')
    total_count: int | None = Field(None, alias='totalCount')

class LoggingData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    section_logging_id: str | None = Field(None, alias='sectionLoggingId')
    track_id: int | None = Field(None, alias='trackId')

class SectionTreatment(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')

class Node(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    display_string: str | None = Field(None, alias='displayString')
    entities: Entities | None = None
    id: str | None = None
    logging_data: LoggingData | None = Field(None, alias='loggingData')
    section_treatment: SectionTreatment | None = Field(None, alias='sectionTreatment')

class Edge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    node: Node | None = None

class Sections(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    edges: list[Edge] | None = None
    total_count: int | None = Field(None, alias='totalCount')

class TrackingInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    request_id: str | None = Field(None, alias='requestId')

class Page(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    field_id: str | None = Field(None, alias='_id')
    display_string: Any | None = Field(None, alias='displayString')
    expires: AwareDatetime | None = None
    sections: Sections | None = None
    tracking_info: TrackingInfo | None = Field(None, alias='trackingInfo')

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page: Page | None = None

class SearchPageResultsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    data: Data | None = None
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
