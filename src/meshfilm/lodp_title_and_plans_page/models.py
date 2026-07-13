# ruff: noqa: TC003
from uuid import UUID

from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field


class Price(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    price_formatted: str = Field(..., alias="priceFormatted")
    price_in_cents: int = Field(..., alias="priceInCents")
    price_tier: str = Field(..., alias="priceTier")


class Attributes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    audio_quality: str = Field(..., alias="audioQuality")
    has_ads: bool = Field(..., alias="hasAds")
    video_quality: str = Field(..., alias="videoQuality")


class Plan(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    plan_id: str = Field(..., alias="planId")
    price: Price
    attributes: Attributes
    name: str
    tag: None


class Plans(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    offer: None
    plans: list[Plan]


class Boxshot300(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    available: bool
    focal_point: None = Field(..., alias="focalPoint")
    height: int
    key: str
    status: str
    url: str
    width: int


class Video(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    video_id: int = Field(..., alias="videoId")
    title: str
    boxshot300: Boxshot300


class Collection(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    videos: list[Video]


class TrifectaRows(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    collections: list[Collection]


class BrandLogoCropped48h(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    available: bool
    focal_point: None = Field(..., alias="focalPoint")
    height: int
    key: str
    status: str
    url: str
    width: int


class LogoStackCropped350(GAPIBaseModel):
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
    badge_prefix: None = Field(..., alias="badgePrefix")
    render_countdown_timer: bool = Field(..., alias="renderCountdownTimer")
    tagline: str


class FocalPoint(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    x: float
    y: float


class BillboardOrStoryArt960(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    available: bool
    focal_point: FocalPoint = Field(..., alias="focalPoint")
    height: int
    key: str
    status: str
    url: str
    width: int


class EclipseBillboardRedux1280(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    available: bool
    focal_point: FocalPoint = Field(..., alias="focalPoint")
    height: int
    key: str
    status: str
    url: str
    width: int


class EclipseBillboardRedux1920(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    available: bool
    focal_point: FocalPoint = Field(..., alias="focalPoint")
    height: int
    key: str
    status: str
    url: str
    width: int


class PlayableVideo(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    url: str


class BillboardOrStoryArt1280(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    available: bool
    focal_point: FocalPoint = Field(..., alias="focalPoint")
    height: int
    key: str
    status: str
    url: str
    width: int


class Video2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    video_id: int = Field(..., alias="videoId")
    playable_video: PlayableVideo = Field(..., alias="playableVideo")
    title: str
    availability_start_time: AwareDatetime = Field(..., alias="availabilityStartTime")
    short_synopsis: str = Field(..., alias="shortSynopsis")
    billboard_or_story_art1280: BillboardOrStoryArt1280 = Field(
        ...,
        alias="billboardOrStoryArt1280",
    )
    display_runtime_ms: int = Field(..., alias="displayRuntimeMs")


class PromoVideo(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    id: int
    video: Video2


class ShareTaglineMessage(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    tagline: str
    typed_classification: str = Field(..., alias="typedClassification")


class Artwork(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    url: str


class Node(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    artwork: Artwork
    playable_video: PlayableVideo = Field(..., alias="playableVideo")
    runtime_sec: int = Field(..., alias="runtimeSec")
    title: str
    type: str
    video_id: int = Field(..., alias="videoId")


class Edge(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    node: Node


class PageInfo(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    has_next_page: bool = Field(..., alias="hasNextPage")


class Trailers(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge]
    page_info: PageInfo = Field(..., alias="pageInfo")


class ContentAdvisory(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    certification_value: str = Field(..., alias="certificationValue")


class Node1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    genre_id: int = Field(..., alias="genreId")
    name: str


class Edge1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    node: Node1


class PrimaryGenres(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge1]
    page_info: PageInfo = Field(..., alias="pageInfo")


class Node2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    name: str
    person_id: int = Field(..., alias="personId")


class Edge2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    node: Node2


class Actors(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge2]
    page_info: PageInfo = Field(..., alias="pageInfo")


class Edge3(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    node: Node2


class Creators(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge3]
    page_info: PageInfo = Field(..., alias="pageInfo")


class AudioTrack(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    language: str


class Subtitle(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    language: str


class MediaTracks(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    audio_tracks: list[AudioTrack] = Field(..., alias="audioTracks")
    subtitles: list[Subtitle]


class Node4(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    genre_id: int = Field(..., alias="genreId")
    title: str


class Edge4(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    node: Node4


class Genres(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge4]
    page_info: PageInfo = Field(..., alias="pageInfo")


class Tag(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    display_name: str = Field(..., alias="displayName")
    id: int
    is_displayable: bool = Field(..., alias="isDisplayable")


class SimilarVideo(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    video_id: int = Field(..., alias="videoId")
    title: str
    boxshot300: Boxshot300


class BillboardOrStoryArt12801(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    available: bool
    focal_point: FocalPoint = Field(..., alias="focalPoint")
    height: int
    key: str
    status: str
    url: str
    width: int


class Node5(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    genre_id: int = Field(..., alias="genreId")
    name: str


class Edge5(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    node: Node5


class CoreGenres(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge5]
    page_info: PageInfo = Field(..., alias="pageInfo")


class Node6(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    name: str
    person_id: int = Field(..., alias="personId")


class Edge6(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    node: Node6


class Directors(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge6]
    page_info: PageInfo = Field(..., alias="pageInfo")


class ThumbnailClips(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    edges: list[None]


class TudumTitle(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    slug: str


class MerchStill300(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    available: bool
    focal_point: FocalPoint = Field(..., alias="focalPoint")
    height: int
    key: str
    status: str
    url: str
    width: int


class Node8(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    video_id: int = Field(..., alias="videoId")
    number: int
    runtime_sec: int = Field(..., alias="runtimeSec")
    short_synopsis: str = Field(..., alias="shortSynopsis")
    title: str
    merch_still300: MerchStill300 = Field(..., alias="merchStill300")


class Edge8(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    node: Node8


class Episodes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge8]
    page_info: PageInfo = Field(..., alias="pageInfo")


class Node7(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    episodes: Episodes
    number_label_v2: str = Field(..., alias="numberLabelV2")
    short_title: str = Field(..., alias="shortTitle")
    show_member_type: str = Field(..., alias="showMemberType")
    title: str
    total_display_runtime_in_sec: int = Field(..., alias="totalDisplayRuntimeInSec")
    video_id: int = Field(..., alias="videoId")


class Edge7(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    node: Node7


class Seasons(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge7]
    page_info: PageInfo = Field(..., alias="pageInfo")
    total_count: int = Field(..., alias="totalCount")


class Video1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    title: str
    video_id: int = Field(..., alias="videoId")
    all_tagline_messages_by_event_state: None = Field(
        ...,
        alias="allTaglineMessagesByEventState",
    )
    event_window: None = Field(None, alias="eventWindow")
    is_available: bool = Field(..., alias="isAvailable")
    live_event: None = Field(None, alias="liveEvent")
    brand_logo_cropped48h: BrandLogoCropped48h = Field(..., alias="brandLogoCropped48h")
    logo_stack_cropped350: LogoStackCropped350 = Field(..., alias="logoStackCropped350")
    tagline_messages: list[TaglineMessage] = Field(..., alias="taglineMessages")
    logged_out_taglines: None = Field(..., alias="loggedOutTaglines")
    billboard_or_story_art960: BillboardOrStoryArt960 = Field(
        ...,
        alias="billboardOrStoryArt960",
    )
    eclipse_billboard_redux1280: EclipseBillboardRedux1280 = Field(
        ...,
        alias="eclipseBillboardRedux1280",
    )
    eclipse_billboard_redux1920: EclipseBillboardRedux1920 = Field(
        ...,
        alias="eclipseBillboardRedux1920",
    )
    promo_video: PromoVideo = Field(..., alias="promoVideo")
    share_tagline_messages: list[ShareTaglineMessage] = Field(
        ...,
        alias="shareTaglineMessages",
    )
    trailers: Trailers
    content_advisory: ContentAdvisory = Field(..., alias="contentAdvisory")
    latest_year: int = Field(..., alias="latestYear")
    primary_genres: PrimaryGenres = Field(..., alias="primaryGenres")
    short_synopsis: str = Field(..., alias="shortSynopsis")
    content_warning: None = Field(..., alias="contentWarning")
    actors: Actors
    creators: Creators
    media_tracks: MediaTracks = Field(..., alias="mediaTracks")
    is_available_for_download: bool = Field(..., alias="isAvailableForDownload")
    genres: Genres
    tags: list[Tag]
    similar_videos: list[SimilarVideo] = Field(..., alias="similarVideos")
    has_original_treatment: bool = Field(..., alias="hasOriginalTreatment")
    billboard_or_story_art1280: BillboardOrStoryArt12801 = Field(
        ...,
        alias="billboardOrStoryArt1280",
    )
    availability_start_time: AwareDatetime = Field(..., alias="availabilityStartTime")
    core_genres: CoreGenres | None = Field(..., alias="coreGenres")
    directors: Directors
    thumbnail_clips: ThumbnailClips = Field(..., alias="thumbnailClips")
    tudum_title: TudumTitle | None = Field(None, alias="tudumTitle")
    seasons: Seasons | None = None
    next_event_window: None = Field(None, alias="nextEventWindow")
    next_live_event: None = Field(None, alias="nextLiveEvent")
    num_seasons_label: str | None = Field(None, alias="numSeasonsLabel")


class Data(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    plans: Plans
    trifecta_rows: TrifectaRows = Field(..., alias="trifectaRows")
    videos: list[Video1]


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
    video_id: int = Field(..., alias="videoId")
    opaque_image_format: str = Field(..., alias="opaqueImageFormat")
    transparent_image_format: str = Field(..., alias="transparentImageFormat")
    thumbnail_video_id: int = Field(..., alias="thumbnailVideoId")
    has_valid_thumbnail_video_id: bool = Field(..., alias="hasValidThumbnailVideoId")
    use_baked_in_play_thumbnail: bool = Field(..., alias="useBakedInPlayThumbnail")
    use_from_watch_supplements: bool = Field(..., alias="useFromWatchSupplements")


class PersistedQuery(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: UUID
    version: int


class Extensions(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    persisted_query: PersistedQuery = Field(..., alias="persistedQuery")


class Body(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    operation_name: str = Field(..., alias="operationName")
    variables: Variables
    extensions: Extensions


class Meshfilm(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    headers: Headers
    body: Body


class LodpTitleAndPlansPageModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    data: Data
    meshfilm: Meshfilm | None = None
