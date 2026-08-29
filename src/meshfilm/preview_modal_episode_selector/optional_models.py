from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from typing import Any

class Episodes(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    total_count: int | None = Field(None, alias='totalCount')

class Reason(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    icon_id: int | None = Field(None, alias='iconId')
    level: str | None = None
    text: str | None = None

class ContentAdvisory(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    board_id: int | None = Field(None, alias='boardId')
    board_name: str | None = Field(None, alias='boardName')
    certification_rating_id: int | None = Field(None, alias='certificationRatingId')
    certification_value: str | None = Field(None, alias='certificationValue')
    i18n_reasons_text: str | None = Field(None, alias='i18nReasonsText')
    maturity_description: str | None = Field(None, alias='maturityDescription')
    maturity_level: int | None = Field(None, alias='maturityLevel')
    reasons: list[Reason] | None = None
    video_specific_rating_reason: Any | None = Field(None, alias='videoSpecificRatingReason')

class Node(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    episodes: Episodes | None = None
    hidden_episode_numbers: bool | None = Field(None, alias='hiddenEpisodeNumbers')
    title: str | None = None
    video_id: int | None = Field(None, alias='videoId')
    content_advisory: ContentAdvisory | None = Field(None, alias='contentAdvisory')

class Edge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    cursor: str | None = None
    node: Node | None = None

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    end_cursor: str | None = Field(None, alias='endCursor')
    has_next_page: bool | None = Field(None, alias='hasNextPage')
    start_cursor: str | None = Field(None, alias='startCursor')

class Seasons(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    edges: list[Edge] | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')

class Video(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    video_id: int | None = Field(None, alias='videoId')
    seasons: Seasons | None = None

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    videos: list[Video] | None = None

class PreviewModalEpisodeSelectorModel(BaseModel):
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
