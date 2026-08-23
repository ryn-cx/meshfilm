from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from typing import Any

class Extensions(BaseModel):
    model_config = ConfigDict(extra='ignore')
    error_type: str | None = Field(None, alias='errorType')
    origin: str | None = None

class Error(BaseModel):
    model_config = ConfigDict(extra='ignore')
    message: str | None = None
    path: list[int | str] | None = None
    extensions: Extensions | None = None

class Boxart(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    available: bool | None = None
    focal_point: Any | None = Field(None, alias='focalPoint')
    height: int | None = None
    key: str | None = None
    status: str | None = None
    url: str | None = None
    width: int | None = None

class ContextualSynopsis(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    evidence_key: str | None = Field(None, alias='evidenceKey')
    text: str | None = None

class Reason(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    icon_id: int | None = Field(None, alias='iconId')
    level: str | None = None
    text: str | None = None

class ContentAdvisory(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    board_id: int | None = Field(None, alias='boardId')
    board_name: str | None = Field(None, alias='boardName')
    certification_rating_id: int | None = Field(None, alias='certificationRatingId')
    certification_value: str | None = Field(None, alias='certificationValue')
    i18n_reasons_text: str | None = Field(None, alias='i18nReasonsText')
    maturity_description: str | None = Field(None, alias='maturityDescription')
    maturity_level: int | None = Field(None, alias='maturityLevel')
    reasons: list[Reason] | None = None
    video_specific_rating_reason: str | None = Field(None, alias='videoSpecificRatingReason')

class Episodes(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    total_count: int | None = Field(None, alias='totalCount')

class ParentSeason(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    episodes: Episodes | None = None
    video_id: int | None = Field(None, alias='videoId')

class CurrentEpisode(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    parent_season: ParentSeason | None = Field(None, alias='parentSeason')
    video_id: int | None = Field(None, alias='videoId')

class Seasons(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    total_count: int | None = Field(None, alias='totalCount')

class Videos(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    video_id: int | None = Field(None, alias='videoId')
    boxart: Boxart | None = None
    title: str | None = None
    unified_entity_id: str | None = Field(None, alias='unifiedEntityId')
    contextual_synopsis: ContextualSynopsis | None = Field(None, alias='contextualSynopsis')
    is_available: bool | None = Field(None, alias='isAvailable')
    is_playable: bool | None = Field(None, alias='isPlayable')
    unplayable_causes: Any | None = Field(None, alias='unplayableCauses')
    latest_year: int | None = Field(None, alias='latestYear')
    content_advisory: ContentAdvisory | None = Field(None, alias='contentAdvisory')
    playback_badges: list[str] | None = Field(None, alias='playbackBadges')
    has_recurring_releases: bool | None = Field(None, alias='hasRecurringReleases')
    is_in_playlist: bool | None = Field(None, alias='isInPlaylist')
    is_in_remind_me_list: bool | None = Field(None, alias='isInRemindMeList')
    is_in_rolling_reminders_list: bool | None = Field(None, alias='isInRollingRemindersList')
    playlist_actions: Any | None = Field(None, alias='playlistActions')
    current_episode: CurrentEpisode | None = Field(None, alias='currentEpisode')
    num_seasons_label: str | None = Field(None, alias='numSeasonsLabel')
    seasons: Seasons | None = None
    bookmark: Any | None = None
    display_runtime_sec: int | None = Field(None, alias='displayRuntimeSec')

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore')
    videos: list[Any | Videos] | None = None

class PreviewModalVideoTitleGroupModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    errors: list[Error] | None = None
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
