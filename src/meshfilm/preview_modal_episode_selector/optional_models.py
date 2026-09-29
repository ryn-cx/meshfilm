from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from typing import Any

class Episodes(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    total_count: int | Any = Field(None, alias='totalCount', union_mode='left_to_right')

class Reason(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    icon_id: int | Any = Field(None, alias='iconId', union_mode='left_to_right')
    level: str | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')

class ContentAdvisory(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    board_id: int | Any = Field(None, alias='boardId', union_mode='left_to_right')
    board_name: str | Any = Field(None, alias='boardName', union_mode='left_to_right')
    certification_rating_id: int | Any = Field(None, alias='certificationRatingId', union_mode='left_to_right')
    certification_value: str | Any = Field(None, alias='certificationValue', union_mode='left_to_right')
    i18n_reasons_text: str | Any = Field(None, alias='i18nReasonsText', union_mode='left_to_right')
    maturity_description: str | Any = Field(None, alias='maturityDescription', union_mode='left_to_right')
    maturity_level: int | Any = Field(None, alias='maturityLevel', union_mode='left_to_right')
    reasons: list[Reason] | Any = Field(default=None, union_mode='left_to_right')
    video_specific_rating_reason: Any | None = Field(None, alias='videoSpecificRatingReason')

class Node(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    episodes: Episodes | Any = Field(default=None, union_mode='left_to_right')
    hidden_episode_numbers: bool | Any = Field(None, alias='hiddenEpisodeNumbers', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    video_id: int | Any = Field(None, alias='videoId', union_mode='left_to_right')
    content_advisory: ContentAdvisory | Any = Field(None, alias='contentAdvisory', union_mode='left_to_right')

class Edge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    cursor: str | Any = Field(default=None, union_mode='left_to_right')
    node: Node | Any = Field(default=None, union_mode='left_to_right')

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    end_cursor: str | Any = Field(None, alias='endCursor', union_mode='left_to_right')
    has_next_page: bool | Any = Field(None, alias='hasNextPage', union_mode='left_to_right')
    start_cursor: str | Any = Field(None, alias='startCursor', union_mode='left_to_right')

class Seasons(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    edges: list[Edge] | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')

class PreviewModalEpisodeSelectorModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    video_id: int | Any = Field(None, alias='videoId', union_mode='left_to_right')
    seasons: Seasons | Any = Field(default=None, union_mode='left_to_right')
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
