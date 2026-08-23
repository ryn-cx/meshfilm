from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, Field
from typing import Any

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

class BoxartHighRes(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    available: bool
    focal_point: None = Field(..., alias='focalPoint')
    height: int
    key: str
    status: str
    url: str
    width: int

class BrandLogoSmall(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    available: bool
    focal_point: None = Field(..., alias='focalPoint')
    height: int
    key: str
    status: str
    url: str
    width: int

class FocalPoint(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    x: float
    y: float

class StoryArt(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    available: bool
    focal_point: FocalPoint = Field(..., alias='focalPoint')
    height: int
    key: str
    status: str
    url: str
    width: int

class TitleLogoBranded(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    available: bool
    focal_point: None = Field(..., alias='focalPoint')
    height: int
    key: str
    status: str
    url: str
    width: int

class TitleLogoUnbranded(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    available: bool
    focal_point: None = Field(..., alias='focalPoint')
    height: int
    key: str
    status: str
    url: str
    width: int

class Episodes(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    total_count: int = Field(..., alias='totalCount')

class ParentSeason(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    episodes: Episodes
    video_id: int = Field(..., alias='videoId')
    hide_episode_numbers: bool = Field(..., alias='hideEpisodeNumbers')
    number: int
    number_label: str = Field(..., alias='numberLabel')
    title: str

class CurrentEpisode(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    video_id: int = Field(..., alias='videoId')
    runtime_sec: int = Field(..., alias='runtimeSec')
    bookmark: None
    title: str
    watch_status: str = Field(..., alias='watchStatus')
    parent_season: ParentSeason = Field(..., alias='parentSeason')
    hide_episode_numbers: bool = Field(..., alias='hideEpisodeNumbers')
    number: int
    badges: list[str]

class TaglineMessage(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    cta_message: None = Field(..., alias='ctaMessage')
    tagline: str
    typed_classification: str = Field(..., alias='typedClassification')

class PrimaryCoreGenreMetadata(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    primary_core_genre: str = Field(..., alias='primaryCoreGenre')

class ContentMetadata(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    content_label: str = Field(..., alias='contentLabel')
    primary_core_genre_metadata: PrimaryCoreGenreMetadata = Field(..., alias='primaryCoreGenreMetadata')

class TextEvidenceItem(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    key: str
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

class Seasons(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    total_count: int = Field(..., alias='totalCount')

class MostLikedMessage(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    tagline: str
    typed_classification: str = Field(..., alias='typedClassification')

class UnifiedEntities(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    video_id: int = Field(..., alias='videoId')
    thumbs_rating: None = Field(..., alias='thumbsRating')
    title: str
    unified_entity_id: str = Field(..., alias='unifiedEntityId')
    next_live_event: None = Field(None, alias='nextLiveEvent')
    boxart: Boxart
    boxart_high_res: BoxartHighRes = Field(..., alias='boxartHighRes')
    brand_logo_small: BrandLogoSmall = Field(..., alias='brandLogoSmall')
    live_now: None = Field(..., alias='liveNow')
    story_art: StoryArt = Field(..., alias='storyArt')
    title_logo_branded: TitleLogoBranded = Field(..., alias='titleLogoBranded')
    title_logo_unbranded: TitleLogoUnbranded = Field(..., alias='titleLogoUnbranded')
    is_available: bool = Field(..., alias='isAvailable')
    is_playable: bool = Field(..., alias='isPlayable')
    unplayable_causes: None = Field(..., alias='unplayableCauses')
    tf1_collection_ids: list[None] = Field(..., alias='tf1CollectionIds')
    current_episode: CurrentEpisode | None = Field(None, alias='currentEpisode')
    tagline_messages: list[TaglineMessage] = Field(..., alias='taglineMessages')
    has_recurring_releases: bool = Field(..., alias='hasRecurringReleases')
    is_in_playlist: bool = Field(..., alias='isInPlaylist')
    is_in_remind_me_list: bool = Field(..., alias='isInRemindMeList')
    is_in_rolling_reminders_list: bool = Field(..., alias='isInRollingRemindersList')
    playlist_actions: None = Field(..., alias='playlistActions')
    watch_status: str = Field(..., alias='watchStatus')
    thumb_rating: None = Field(..., alias='thumbRating')
    content_metadata: ContentMetadata = Field(..., alias='contentMetadata')
    content_warning: None = Field(..., alias='contentWarning')
    text_evidence: list[TextEvidenceItem] = Field(..., alias='textEvidence')
    latest_year: int = Field(..., alias='latestYear')
    content_advisory: ContentAdvisory = Field(..., alias='contentAdvisory')
    playback_badges: list[str] = Field(..., alias='playbackBadges')
    num_seasons_label: str | None = Field(None, alias='numSeasonsLabel')
    seasons: Seasons | None = None
    most_liked_messages: list[MostLikedMessage] = Field(..., alias='mostLikedMessages')
    badges: list[str]
    live_event: None = Field(None, alias='liveEvent')
    bookmark: None = Field(None)
    runtime_sec: int | None = Field(None, alias='runtimeSec')
    display_runtime_sec: int | None = Field(None, alias='displayRuntimeSec')

class Data(BaseModel):
    unified_entities: list[UnifiedEntities | None] = Field(..., alias='unifiedEntities')

class MiniModalModel(BaseModel):
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
