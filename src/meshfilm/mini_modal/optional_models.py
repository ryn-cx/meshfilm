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

class BoxartHighRes(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    available: bool | None = None
    focal_point: Any | None = Field(None, alias='focalPoint')
    height: int | None = None
    key: str | None = None
    status: str | None = None
    url: str | None = None
    width: int | None = None

class BrandLogoSmall(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    available: bool | None = None
    focal_point: Any | None = Field(None, alias='focalPoint')
    height: int | None = None
    key: str | None = None
    status: str | None = None
    url: str | None = None
    width: int | None = None

class FocalPoint(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    x: float | None = None
    y: float | None = None

class StoryArt(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    available: bool | None = None
    focal_point: FocalPoint | None = Field(None, alias='focalPoint')
    height: int | None = None
    key: str | None = None
    status: str | None = None
    url: str | None = None
    width: int | None = None

class TitleLogoBranded(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    available: bool | None = None
    focal_point: Any | None = Field(None, alias='focalPoint')
    height: int | None = None
    key: str | None = None
    status: str | None = None
    url: str | None = None
    width: int | None = None

class TitleLogoUnbranded(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    available: bool | None = None
    focal_point: Any | None = Field(None, alias='focalPoint')
    height: int | None = None
    key: str | None = None
    status: str | None = None
    url: str | None = None
    width: int | None = None

class Episodes(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    total_count: int | None = Field(None, alias='totalCount')

class ParentSeason(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    episodes: Episodes | None = None
    video_id: int | None = Field(None, alias='videoId')
    hide_episode_numbers: bool | None = Field(None, alias='hideEpisodeNumbers')
    number: int | None = None
    number_label: str | None = Field(None, alias='numberLabel')
    title: str | None = None

class CurrentEpisode(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    video_id: int | None = Field(None, alias='videoId')
    runtime_sec: int | None = Field(None, alias='runtimeSec')
    bookmark: Any | None = None
    title: str | None = None
    watch_status: str | None = Field(None, alias='watchStatus')
    parent_season: ParentSeason | None = Field(None, alias='parentSeason')
    hide_episode_numbers: bool | None = Field(None, alias='hideEpisodeNumbers')
    number: int | None = None
    badges: list[str] | None = None

class TaglineMessage(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    cta_message: Any | None = Field(None, alias='ctaMessage')
    tagline: str | None = None
    typed_classification: str | None = Field(None, alias='typedClassification')

class PrimaryCoreGenreMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    primary_core_genre: str | None = Field(None, alias='primaryCoreGenre')

class ContentMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    content_label: str | None = Field(None, alias='contentLabel')
    primary_core_genre_metadata: PrimaryCoreGenreMetadata | None = Field(None, alias='primaryCoreGenreMetadata')

class TextEvidenceItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    key: str | None = None
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

class Seasons(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    total_count: int | None = Field(None, alias='totalCount')

class MostLikedMessage(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    tagline: str | None = None
    typed_classification: str | None = Field(None, alias='typedClassification')

class UnifiedEntities(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    video_id: int | None = Field(None, alias='videoId')
    thumbs_rating: Any | None = Field(None, alias='thumbsRating')
    title: str | None = None
    unified_entity_id: str | None = Field(None, alias='unifiedEntityId')
    next_live_event: Any | None = Field(None, alias='nextLiveEvent')
    boxart: Boxart | None = None
    boxart_high_res: BoxartHighRes | None = Field(None, alias='boxartHighRes')
    brand_logo_small: BrandLogoSmall | None = Field(None, alias='brandLogoSmall')
    live_now: Any | None = Field(None, alias='liveNow')
    story_art: StoryArt | None = Field(None, alias='storyArt')
    title_logo_branded: TitleLogoBranded | None = Field(None, alias='titleLogoBranded')
    title_logo_unbranded: TitleLogoUnbranded | None = Field(None, alias='titleLogoUnbranded')
    is_available: bool | None = Field(None, alias='isAvailable')
    is_playable: bool | None = Field(None, alias='isPlayable')
    unplayable_causes: Any | None = Field(None, alias='unplayableCauses')
    tf1_collection_ids: list[Any] | None = Field(None, alias='tf1CollectionIds')
    current_episode: CurrentEpisode | None = Field(None, alias='currentEpisode')
    tagline_messages: list[TaglineMessage] | None = Field(None, alias='taglineMessages')
    has_recurring_releases: bool | None = Field(None, alias='hasRecurringReleases')
    is_in_playlist: bool | None = Field(None, alias='isInPlaylist')
    is_in_remind_me_list: bool | None = Field(None, alias='isInRemindMeList')
    is_in_rolling_reminders_list: bool | None = Field(None, alias='isInRollingRemindersList')
    playlist_actions: Any | None = Field(None, alias='playlistActions')
    watch_status: str | None = Field(None, alias='watchStatus')
    thumb_rating: Any | None = Field(None, alias='thumbRating')
    content_metadata: ContentMetadata | None = Field(None, alias='contentMetadata')
    content_warning: Any | None = Field(None, alias='contentWarning')
    text_evidence: list[TextEvidenceItem] | None = Field(None, alias='textEvidence')
    latest_year: int | None = Field(None, alias='latestYear')
    content_advisory: ContentAdvisory | None = Field(None, alias='contentAdvisory')
    playback_badges: list[str] | None = Field(None, alias='playbackBadges')
    num_seasons_label: str | None = Field(None, alias='numSeasonsLabel')
    seasons: Seasons | None = None
    most_liked_messages: list[MostLikedMessage] | None = Field(None, alias='mostLikedMessages')
    badges: list[str] | None = None
    live_event: Any | None = Field(None, alias='liveEvent')
    bookmark: Any | None = None
    runtime_sec: int | None = Field(None, alias='runtimeSec')
    display_runtime_sec: int | None = Field(None, alias='displayRuntimeSec')

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore')
    unified_entities: list[Any | UnifiedEntities] | None = Field(None, alias='unifiedEntities')

class MiniModalModel(BaseModel):
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
