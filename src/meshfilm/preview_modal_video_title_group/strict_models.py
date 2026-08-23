from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, Field

class Extensions(BaseModel):
    error_type: str = Field(..., alias='errorType')
    origin: str

class Error(BaseModel):
    message: str
    path: list[int | str]
    extensions: Extensions

class Boxart(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    available: bool
    focal_point: None = Field(..., alias='focalPoint')
    height: int
    key: str
    status: str
    url: str
    width: int

class ContextualSynopsis(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    evidence_key: str = Field(..., alias='evidenceKey')
    text: str

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
    video_specific_rating_reason: str | None = Field(..., alias='videoSpecificRatingReason')

class Episodes(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    total_count: int = Field(..., alias='totalCount')

class ParentSeason(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    episodes: Episodes
    video_id: int = Field(..., alias='videoId')

class CurrentEpisode(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    parent_season: ParentSeason = Field(..., alias='parentSeason')
    video_id: int = Field(..., alias='videoId')

class Seasons(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    total_count: int = Field(..., alias='totalCount')

class Videos(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    video_id: int = Field(..., alias='videoId')
    boxart: Boxart
    title: str
    unified_entity_id: str = Field(..., alias='unifiedEntityId')
    contextual_synopsis: ContextualSynopsis = Field(..., alias='contextualSynopsis')
    is_available: bool = Field(..., alias='isAvailable')
    is_playable: bool = Field(..., alias='isPlayable')
    unplayable_causes: None = Field(..., alias='unplayableCauses')
    latest_year: int = Field(..., alias='latestYear')
    content_advisory: ContentAdvisory = Field(..., alias='contentAdvisory')
    playback_badges: list[str] = Field(..., alias='playbackBadges')
    has_recurring_releases: bool = Field(..., alias='hasRecurringReleases')
    is_in_playlist: bool = Field(..., alias='isInPlaylist')
    is_in_remind_me_list: bool = Field(..., alias='isInRemindMeList')
    is_in_rolling_reminders_list: bool = Field(..., alias='isInRollingRemindersList')
    playlist_actions: None = Field(..., alias='playlistActions')
    current_episode: CurrentEpisode | None = Field(None, alias='currentEpisode')
    num_seasons_label: str | None = Field(None, alias='numSeasonsLabel')
    seasons: Seasons | None = None
    bookmark: None = Field(None)
    display_runtime_sec: int | None = Field(None, alias='displayRuntimeSec')

class Data(BaseModel):
    videos: list[Videos | None]

class PreviewModalVideoTitleGroupModel(BaseModel):
    errors: list[Error]
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
