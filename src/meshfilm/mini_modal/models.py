# TODO: Validate
# ruff: noqa: TC003
from typing import Any
from uuid import UUID

from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict, Field


class Extensions(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    error_type: str = Field(..., alias="errorType")
    origin: str


class Error(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    message: str
    path: list[int | str]
    extensions: Extensions


class Boxart(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    available: bool
    focal_point: None = Field(..., alias="focalPoint")
    height: int
    key: str
    status: str
    url: str
    width: int


class BoxartHighRes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    available: bool
    focal_point: None = Field(..., alias="focalPoint")
    height: int
    key: str
    status: str
    url: str
    width: int


class BrandLogoSmall(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    available: bool
    focal_point: None = Field(..., alias="focalPoint")
    height: int
    key: str
    status: str
    url: str
    width: int


class FocalPoint(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    x: float
    y: float


class StoryArt(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    available: bool
    focal_point: FocalPoint = Field(..., alias="focalPoint")
    height: int
    key: str
    status: str
    url: str
    width: int


class TitleLogoBranded(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    available: bool
    focal_point: None = Field(..., alias="focalPoint")
    height: int
    key: str
    status: str
    url: str
    width: int


class TitleLogoUnbranded(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    available: bool
    focal_point: None = Field(..., alias="focalPoint")
    height: int
    key: str
    status: str
    url: str
    width: int


class TaglineMessage(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    cta_message: None = Field(..., alias="ctaMessage")
    tagline: str
    typed_classification: str = Field(..., alias="typedClassification")


class PrimaryCoreGenreMetadata(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    primary_core_genre: str = Field(..., alias="primaryCoreGenre")


class ContentMetadata(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    content_label: str = Field(..., alias="contentLabel")
    primary_core_genre_metadata: PrimaryCoreGenreMetadata = Field(
        ...,
        alias="primaryCoreGenreMetadata",
    )


class TextEvidenceItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    key: str
    text: str


class Reason(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    icon_id: int = Field(..., alias="iconId")
    level: str
    text: str


class ContentAdvisory(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    board_id: int = Field(..., alias="boardId")
    board_name: str = Field(..., alias="boardName")
    certification_rating_id: int = Field(..., alias="certificationRatingId")
    certification_value: str = Field(..., alias="certificationValue")
    i18n_reasons_text: str = Field(..., alias="i18nReasonsText")
    maturity_description: str = Field(..., alias="maturityDescription")
    maturity_level: int = Field(..., alias="maturityLevel")
    reasons: list[Reason]
    video_specific_rating_reason: str | None = Field(
        ...,
        alias="videoSpecificRatingReason",
    )


class MostLikedMessage(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    tagline: str
    typed_classification: str = Field(..., alias="typedClassification")


class Episodes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    total_count: int = Field(..., alias="totalCount")


class ParentSeason(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    episodes: Episodes
    video_id: int = Field(..., alias="videoId")
    hide_episode_numbers: bool | None = Field(None, alias="hideEpisodeNumbers")
    number: int | None = None
    number_label: str | None = Field(None, alias="numberLabel")
    title: str | None = None


class CurrentEpisode(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    parent_season: ParentSeason = Field(..., alias="parentSeason")
    video_id: int = Field(..., alias="videoId")
    runtime_sec: int | None = Field(None, alias="runtimeSec")
    bookmark: None = Field(None)
    title: str | None = None
    watch_status: str | None = Field(None, alias="watchStatus")
    hide_episode_numbers: bool | None = Field(None, alias="hideEpisodeNumbers")
    number: int | None = None
    badges: list[str] | None = None


class Seasons(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    total_count: int = Field(..., alias="totalCount")


class ParentShow(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    current_episode: CurrentEpisode = Field(..., alias="currentEpisode")
    num_seasons_label: str = Field(..., alias="numSeasonsLabel")
    seasons: Seasons
    video_id: int = Field(..., alias="videoId")


class ParentSeason1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    hide_episode_numbers: bool = Field(..., alias="hideEpisodeNumbers")
    number: int
    number_label: str = Field(..., alias="numberLabel")
    title: str
    video_id: int = Field(..., alias="videoId")


class ParentSeason2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    episodes: Episodes
    video_id: int = Field(..., alias="videoId")
    hide_episode_numbers: bool = Field(..., alias="hideEpisodeNumbers")
    number: int
    number_label: str = Field(..., alias="numberLabel")
    title: str


class CurrentEpisode1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    video_id: int = Field(..., alias="videoId")
    runtime_sec: int = Field(..., alias="runtimeSec")
    bookmark: None
    title: str
    watch_status: str = Field(..., alias="watchStatus")
    parent_season: ParentSeason2 = Field(..., alias="parentSeason")
    hide_episode_numbers: bool = Field(..., alias="hideEpisodeNumbers")
    number: int
    badges: list[str]


class UnifiedEntity(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    video_id: int = Field(..., alias="videoId")
    thumbs_rating: None = Field(..., alias="thumbsRating")
    title: str
    unified_entity_id: str = Field(..., alias="unifiedEntityId")
    live_event: None = Field(None, alias="liveEvent")
    boxart: Boxart
    boxart_high_res: BoxartHighRes = Field(..., alias="boxartHighRes")
    brand_logo_small: BrandLogoSmall = Field(..., alias="brandLogoSmall")
    live_now: None = Field(None, alias="liveNow")
    story_art: StoryArt = Field(..., alias="storyArt")
    title_logo_branded: TitleLogoBranded = Field(..., alias="titleLogoBranded")
    title_logo_unbranded: TitleLogoUnbranded = Field(..., alias="titleLogoUnbranded")
    is_available: bool = Field(..., alias="isAvailable")
    is_playable: bool = Field(..., alias="isPlayable")
    unplayable_causes: None = Field(..., alias="unplayableCauses")
    bookmark: None = Field(None)
    tf1_collection_ids: list[None] | None = Field(..., alias="tf1CollectionIds")
    tagline_messages: list[TaglineMessage] = Field(..., alias="taglineMessages")
    has_recurring_releases: bool = Field(..., alias="hasRecurringReleases")
    is_in_playlist: bool = Field(..., alias="isInPlaylist")
    is_in_remind_me_list: bool = Field(..., alias="isInRemindMeList")
    is_in_rolling_reminders_list: bool = Field(..., alias="isInRollingRemindersList")
    playlist_actions: None = Field(..., alias="playlistActions")
    watch_status: str = Field(..., alias="watchStatus")
    runtime_sec: int | None = Field(None, alias="runtimeSec")
    thumb_rating: None = Field(..., alias="thumbRating")
    content_metadata: ContentMetadata = Field(..., alias="contentMetadata")
    content_warning: None = Field(..., alias="contentWarning")
    text_evidence: list[TextEvidenceItem] = Field(..., alias="textEvidence")
    latest_year: int = Field(..., alias="latestYear")
    content_advisory: ContentAdvisory = Field(..., alias="contentAdvisory")
    playback_badges: list[str] = Field(..., alias="playbackBadges")
    display_runtime_sec: int | None = Field(None, alias="displayRuntimeSec")
    most_liked_messages: list[MostLikedMessage] = Field(..., alias="mostLikedMessages")
    badges: list[str]
    parent_show: ParentShow | None = Field(None, alias="parentShow")
    hide_episode_numbers: bool | None = Field(None, alias="hideEpisodeNumbers")
    number: int | None = None
    parent_season: ParentSeason1 | None = Field(None, alias="parentSeason")
    next_live_event: None = Field(None, alias="nextLiveEvent")
    current_episode: CurrentEpisode1 | None = Field(None, alias="currentEpisode")
    num_seasons_label: str | None = Field(None, alias="numSeasonsLabel")
    seasons: Seasons | None = None


class Data(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    unified_entities: list[UnifiedEntity] = Field(..., alias="unifiedEntities")


class Headers(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    user_agent: str = Field(..., alias="User-Agent")
    accept: str = Field(..., alias="Accept")
    accept_language: str = Field(..., alias="Accept-Language")
    accept_encoding: str = Field(..., alias="Accept-Encoding")
    content_type: str = Field(..., alias="Content-Type")
    origin: str = Field(..., alias="Origin")
    referer: str = Field(..., alias="Referer")
    x_netflix_context_ui_flavor: str = Field(..., alias="x-netflix.context.ui-flavor")
    x_netflix_context_app_version: str = Field(
        ...,
        alias="x-netflix.context.app-version",
    )
    x_netflix_context_locales: str = Field(..., alias="x-netflix.context.locales")
    x_netflix_context_operation_name: str = Field(
        ...,
        alias="x-netflix.context.operation-name",
    )
    x_netflix_request_attempt: str = Field(..., alias="x-netflix.request.attempt")
    x_netflix_request_client_context: str = Field(
        ...,
        alias="x-netflix.request.client.context",
    )


class Variables(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    opaque_image_format: str = Field(..., alias="opaqueImageFormat")
    transparent_image_format: str = Field(..., alias="transparentImageFormat")
    video_merch_enabled: bool = Field(..., alias="videoMerchEnabled")
    fetch_promo_video_override: bool = Field(..., alias="fetchPromoVideoOverride")
    has_promo_video_override: bool = Field(..., alias="hasPromoVideoOverride")
    promo_video_id: int = Field(..., alias="promoVideoId")
    video_merch_context: str = Field(..., alias="videoMerchContext")
    is_live_episodic: bool = Field(..., alias="isLiveEpisodic")
    artwork_context: dict[str, Any] = Field(..., alias="artworkContext")
    text_evidence_ui_context: str = Field(..., alias="textEvidenceUiContext")
    unified_entity_ids: list[str] = Field(..., alias="unifiedEntityIds")


class PersistedQuery(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: UUID
    version: int


class Extensions1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    persisted_query: PersistedQuery = Field(..., alias="persistedQuery")


class Body(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    operation_name: str = Field(..., alias="operationName")
    variables: Variables
    extensions: Extensions1


class Meshfilm(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    headers: Headers
    body: Body


class MiniModalModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    errors: list[Error]
    data: Data
    meshfilm: Meshfilm | None = None
