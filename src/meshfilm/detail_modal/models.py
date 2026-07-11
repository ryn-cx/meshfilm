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


class PlaybackEntity(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    video_id: int = Field(..., alias="videoId")


class BroadcastInfo(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    distributor_name: None = Field(..., alias="distributorName")
    release_date: None = Field(..., alias="releaseDate")


class Node(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    name: str
    person_id: int = Field(..., alias="personId")


class Edge(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    cursor: str
    node: Node


class PageInfo(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    has_next_page: bool = Field(..., alias="hasNextPage")


class Cast(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge]
    page_info: PageInfo = Field(..., alias="pageInfo")


class Edge1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    cursor: str
    node: Node


class Creators(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge1]
    page_info: PageInfo = Field(..., alias="pageInfo")


class Edge2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    cursor: str
    node: Node


class Directors(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge2]
    page_info: PageInfo = Field(..., alias="pageInfo")


class Edge3(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    cursor: str
    node: Node


class Writers(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge3]
    page_info: PageInfo = Field(..., alias="pageInfo")


class Node4(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    genre_id: int = Field(..., alias="genreId")
    name: str


class Edge4(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    cursor: str
    node: Node4


class GenreTags(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge4]
    page_info: PageInfo = Field(..., alias="pageInfo")


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


class MoodTag(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    display_name: str = Field(..., alias="displayName")
    id: int
    is_displayable: bool = Field(..., alias="isDisplayable")
    is_mood: bool = Field(..., alias="isMood")


class ContextualSynopsis(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    evidence_key: str = Field(..., alias="evidenceKey")
    text: str


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
    hide_episode_numbers: bool | None = Field(None, alias="hideEpisodeNumbers")
    number: int | None = None
    title: str | None = None
    badges: list[str] | None = None
    watch_status: str | None = Field(None, alias="watchStatus")
    contextual_synopsis: ContextualSynopsis | None = Field(
        None,
        alias="contextualSynopsis",
    )
    runtime_sec: int | None = Field(None, alias="runtimeSec")
    bookmark: None = Field(None)


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
    title_group_memberships: list[None] = Field(..., alias="titleGroupMemberships")


class MostLikedMessage(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    tagline: str
    typed_classification: str = Field(..., alias="typedClassification")


class TaglineMessage(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    cta_message: None = Field(..., alias="ctaMessage")
    tagline: str
    typed_classification: str = Field(..., alias="typedClassification")


class ParentSeason1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    hide_episode_numbers: bool = Field(..., alias="hideEpisodeNumbers")
    number: int
    number_label: str = Field(..., alias="numberLabel")
    title: str
    video_id: int = Field(..., alias="videoId")


class Similar(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    video_id: int = Field(..., alias="videoId")


class Node5(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    video_id: int = Field(..., alias="videoId")


class Edge5(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    node: Node5


class SupplementalVideosList(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge5]
    page_info: PageInfo = Field(..., alias="pageInfo")


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


class Sibling(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    video_id: int = Field(..., alias="videoId")


class TitleGroupMembership(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    id: str
    kind: str
    siblings: list[Sibling]
    title: str


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
    parent_season: ParentSeason2 = Field(..., alias="parentSeason")
    video_id: int = Field(..., alias="videoId")
    hide_episode_numbers: bool = Field(..., alias="hideEpisodeNumbers")
    number: int
    title: str
    badges: list[str]
    watch_status: str = Field(..., alias="watchStatus")
    contextual_synopsis: ContextualSynopsis = Field(..., alias="contextualSynopsis")
    runtime_sec: int = Field(..., alias="runtimeSec")
    bookmark: None


class UnifiedEntity(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    video_id: int = Field(..., alias="videoId")
    is_available: bool = Field(..., alias="isAvailable")
    is_playable: bool = Field(..., alias="isPlayable")
    unplayable_causes: None = Field(..., alias="unplayableCauses")
    title: str
    live_event: None = Field(None, alias="liveEvent")
    broadcast_info: BroadcastInfo = Field(..., alias="broadcastInfo")
    copyright: None
    cast: Cast
    creators: Creators
    directors: Directors
    writers: Writers
    genre_tags: GenreTags = Field(..., alias="genreTags")
    content_advisory: ContentAdvisory = Field(..., alias="contentAdvisory")
    mood_tags: list[MoodTag] = Field(..., alias="moodTags")
    content_warning: None = Field(..., alias="contentWarning")
    unified_entity_id: str = Field(..., alias="unifiedEntityId")
    contextual_synopsis: ContextualSynopsis = Field(..., alias="contextualSynopsis")
    latest_year: int = Field(..., alias="latestYear")
    playback_badges: list[str] = Field(..., alias="playbackBadges")
    has_recurring_releases: bool = Field(..., alias="hasRecurringReleases")
    is_in_playlist: bool = Field(..., alias="isInPlaylist")
    is_in_remind_me_list: bool = Field(..., alias="isInRemindMeList")
    is_in_rolling_reminders_list: bool = Field(..., alias="isInRollingRemindersList")
    playlist_actions: None = Field(..., alias="playlistActions")
    parent_show: ParentShow | None = Field(None, alias="parentShow")
    display_runtime_sec: int | None = Field(None, alias="displayRuntimeSec")
    most_liked_messages: list[MostLikedMessage] = Field(..., alias="mostLikedMessages")
    tagline_messages: list[TaglineMessage] = Field(..., alias="taglineMessages")
    hide_episode_numbers: bool | None = Field(None, alias="hideEpisodeNumbers")
    number: int | None = None
    parent_season: ParentSeason1 | None = Field(None, alias="parentSeason")
    badges: list[str] | None = None
    watch_status: str = Field(..., alias="watchStatus")
    similars: list[Similar]
    ryan_murphy_collection_ids: list[None] | None = Field(
        ...,
        alias="ryanMurphyCollectionIds",
    )
    shonda_rhimes_collection_ids: list[None] | None = Field(
        ...,
        alias="shondaRhimesCollectionIds",
    )
    supplemental_videos_list: SupplementalVideosList = Field(
        ...,
        alias="supplementalVideosList",
    )
    thumbs_rating: None = Field(..., alias="thumbsRating")
    boxart: Boxart
    boxart_high_res: BoxartHighRes = Field(..., alias="boxartHighRes")
    brand_logo_small: BrandLogoSmall = Field(..., alias="brandLogoSmall")
    story_art: StoryArt = Field(..., alias="storyArt")
    title_logo_branded: TitleLogoBranded = Field(..., alias="titleLogoBranded")
    title_logo_unbranded: TitleLogoUnbranded = Field(..., alias="titleLogoUnbranded")
    bookmark: None = Field(None)
    tf1_collection_ids: list[None] | None = Field(..., alias="tf1CollectionIds")
    runtime_sec: int | None = Field(None, alias="runtimeSec")
    thumb_rating: None = Field(..., alias="thumbRating")
    title_group_memberships: list[TitleGroupMembership] | None = Field(
        None,
        alias="titleGroupMemberships",
    )
    live_now: None = Field(None, alias="liveNow")
    next_live_event: None = Field(None, alias="nextLiveEvent")
    current_episode: CurrentEpisode1 | None = Field(None, alias="currentEpisode")
    num_seasons_label: str | None = Field(None, alias="numSeasonsLabel")
    seasons: Seasons | None = None


class Data(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    playback_entities: list[PlaybackEntity] = Field(..., alias="playbackEntities")
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
    unified_entity_id: str = Field(..., alias="unifiedEntityId")
    video_id: int = Field(..., alias="videoId")
    check_linear_channel: bool = Field(..., alias="checkLinearChannel")


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


class DetailModalModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    errors: list[Error]
    data: Data
    meshfilm: Meshfilm
