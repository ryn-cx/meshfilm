from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, Field

class Episodes(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    total_count: int = Field(..., alias='totalCount')

class Reason(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    icon_id: int = Field(..., alias='iconId')
    level: str
    text: str

class ContentAdvisory(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    board_id: int = Field(..., alias='boardId')
    board_name: str = Field(..., alias='boardName')
    certification_rating_id: int = Field(..., alias='certificationRatingId')
    certification_value: str = Field(..., alias='certificationValue')
    i18n_reasons_text: str = Field(..., alias='i18nReasonsText')
    maturity_description: str = Field(..., alias='maturityDescription')
    maturity_level: int = Field(..., alias='maturityLevel')
    reasons: list[Reason]
    video_specific_rating_reason: None = Field(..., alias='videoSpecificRatingReason')

class Node(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    episodes: Episodes
    hidden_episode_numbers: bool = Field(..., alias='hiddenEpisodeNumbers')
    title: str
    video_id: int = Field(..., alias='videoId')
    content_advisory: ContentAdvisory = Field(..., alias='contentAdvisory')

class Edge(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    cursor: str
    node: Node

class PageInfo(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    end_cursor: str = Field(..., alias='endCursor')
    has_next_page: bool = Field(..., alias='hasNextPage')
    start_cursor: str = Field(..., alias='startCursor')

class Seasons(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    edges: list[Edge]
    page_info: PageInfo = Field(..., alias='pageInfo')

class Video(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    video_id: int = Field(..., alias='videoId')
    seasons: Seasons | None = None

class Data(BaseModel):
    videos: list[Video]

class PreviewModalEpisodeSelectorModel(BaseModel):
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
