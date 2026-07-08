# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field


class ArtworkBoxshot300Jpg(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    key: str
    url: str
    width: int
    height: int
    available: bool
    status: str
    focal_point: None = Field(..., alias="focalPoint")


class Movie(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    video_id: int = Field(..., alias="videoId")
    title: str
    artwork_boxshot_300_jpg: ArtworkBoxshot300Jpg


class FocalPoint(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    x: float
    y: float


class ArtworkBillboard1280StoryArtJpg(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    key: str
    url: str
    width: int
    height: int
    available: bool
    status: str
    focal_point: FocalPoint = Field(..., alias="focalPoint")


class PromoVideoBillboard(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__ref: str = Field(..., alias="__ref")


class Node(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__ref: str = Field(..., alias="__ref")


class Edge(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    node: Node


class PageInfo(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    has_next_page: bool = Field(..., alias="hasNextPage")
    has_previous_page: bool = Field(..., alias="hasPreviousPage")
    start_cursor: str = Field(..., alias="startCursor")
    end_cursor: str = Field(..., alias="endCursor")


class PersonsActor(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    total_count: int = Field(..., alias="totalCount")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge]
    page_info: PageInfo = Field(..., alias="pageInfo")


class PersonsDirector(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    total_count: int = Field(..., alias="totalCount")
    field__typename: str = Field(..., alias="__typename")
    edges: list[None]
    page_info: PageInfo = Field(..., alias="pageInfo")


class Edge1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    node: Node


class PersonsCreator(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    total_count: int = Field(..., alias="totalCount")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge1]
    page_info: PageInfo = Field(..., alias="pageInfo")


class PageInfo3(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    has_next_page: bool = Field(..., alias="hasNextPage")


class Edge2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    node: Node


class CoreGenres(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    page_info: PageInfo3 = Field(..., alias="pageInfo")
    edges: list[Edge2]


class ContentAdvisory(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    certification_value: str = Field(..., alias="certificationValue")


class Edge3(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    node: Node


class PageInfo4(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    has_next_page: bool = Field(..., alias="hasNextPage")
    has_previous_page: bool = Field(..., alias="hasPreviousPage")
    start_cursor: str = Field(..., alias="startCursor")
    end_cursor: str = Field(..., alias="endCursor")


class Seasons(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    total_count: int = Field(..., alias="totalCount")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge3]
    page_info: PageInfo4 = Field(..., alias="pageInfo")


class Edge4(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    node: Node


class SupplementalVideosListTrailerTeaserTrailer(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    total_count: int = Field(..., alias="totalCount")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge4]
    page_info: PageInfo4 = Field(..., alias="pageInfo")


class Edge5(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    node: Node


class Genres(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    total_count: int = Field(..., alias="totalCount")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge5]
    page_info: PageInfo4 = Field(..., alias="pageInfo")


class Tag(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__ref: str = Field(..., alias="__ref")


class TudumTitle(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    slug: str


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


class TaglineMessagesLoggedOutDpItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    tagline: str
    badge_prefix: None = Field(..., alias="badgePrefix")
    render_countdown_timer: bool = Field(..., alias="renderCountdownTimer")


class ArtworkLogoHorizontalCropped350Png(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    key: str
    url: str
    width: int
    height: int
    available: bool
    status: str
    focal_point: None = Field(..., alias="focalPoint")


class ArtworkBrandLogoCropped48LightPng(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    key: str
    url: str
    width: int
    height: int
    available: bool
    status: str
    focal_point: None = Field(..., alias="focalPoint")


class ArtworkEclipseBillboardRedux1920Jpg(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    key: str
    url: str
    width: int
    height: int
    available: bool
    status: str
    focal_point: FocalPoint = Field(..., alias="focalPoint")


class ArtworkEclipseBillboardRedux1280Jpg(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    key: str
    url: str
    width: int
    height: int
    available: bool
    status: str
    focal_point: FocalPoint = Field(..., alias="focalPoint")


class ArtworkBillboard960StoryArtJpg(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    key: str
    url: str
    width: int
    height: int
    available: bool
    status: str
    focal_point: FocalPoint = Field(..., alias="focalPoint")


class TaglineMessagesOdpItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    tagline: str
    typed_classification: str = Field(..., alias="typedClassification")


class SimilarVideo(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__ref: str = Field(..., alias="__ref")


class PageInfo7(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    has_next_page: bool = Field(..., alias="hasNextPage")


class Edge6(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    node: Node


class PrimaryGenres(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    page_info: PageInfo7 = Field(..., alias="pageInfo")
    edges: list[Edge6]


class PageInfo8(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    has_previous_page: bool = Field(..., alias="hasPreviousPage")
    has_next_page: bool = Field(..., alias="hasNextPage")
    start_cursor: str = Field(..., alias="startCursor")
    end_cursor: str = Field(..., alias="endCursor")


class SupplementalVideosListClips(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    total_count: int = Field(..., alias="totalCount")
    field__typename: str = Field(..., alias="__typename")
    edges: list[None]
    page_info: PageInfo8 = Field(..., alias="pageInfo")


class Show(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    video_id: int = Field(..., alias="videoId")
    title: str
    artwork_boxshot_300_jpg: ArtworkBoxshot300Jpg | None = None
    short_synopsis: str | None = Field(None, alias="shortSynopsis")
    has_original_treatment: bool | None = Field(None, alias="hasOriginalTreatment")
    artwork_billboard_1280_story_art_jpg: ArtworkBillboard1280StoryArtJpg | None = None
    promo_video_billboard: PromoVideoBillboard | None = Field(
        None,
        alias="promoVideo_billboard",
    )
    availability_start_time: AwareDatetime | None = Field(
        None,
        alias="availabilityStartTime",
    )
    persons_actor: PersonsActor | None = None
    persons_director: PersonsDirector | None = None
    persons_creator: PersonsCreator | None = None
    core_genres: CoreGenres | None = Field(None, alias="coreGenres")
    content_advisory: ContentAdvisory | None = Field(None, alias="contentAdvisory")
    latest_year: int | None = Field(None, alias="latestYear")
    seasons: Seasons | None = None
    supplemental_videos_list_trailer_teaser_trailer: (
        SupplementalVideosListTrailerTeaserTrailer | None
    ) = Field(None, alias="supplementalVideosList_trailer_teaser_trailer")
    genres: Genres | None = None
    is_available_for_download: bool | None = Field(None, alias="isAvailableForDownload")
    tags: list[Tag] | None = None
    tudum_title: TudumTitle | None = Field(None, alias="tudumTitle")
    media_tracks: MediaTracks | None = Field(None, alias="mediaTracks")
    tagline_messages_logged_out_dp: list[TaglineMessagesLoggedOutDpItem] | None = Field(
        None,
        alias="taglineMessages_logged_out_dp",
    )
    all_tagline_messages_by_event_state_logged_out_dp: None = Field(
        None,
        alias="allTaglineMessagesByEventState_logged_out_dp",
    )
    next_event_window: None = Field(None, alias="nextEventWindow")
    artwork_logo_horizontal_cropped_350_png: (
        ArtworkLogoHorizontalCropped350Png | None
    ) = None
    artwork_brand_logo_cropped_48_light_png: (
        ArtworkBrandLogoCropped48LightPng | None
    ) = None
    is_available: bool | None = Field(None, alias="isAvailable")
    next_live_event: None = Field(None, alias="nextLiveEvent")
    all_tagline_messages_by_event_state_episode_list: None = Field(
        None,
        alias="allTaglineMessagesByEventState_episode_list",
    )
    artwork_eclipse_billboard_redux_1920_jpg: (
        ArtworkEclipseBillboardRedux1920Jpg | None
    ) = None
    artwork_eclipse_billboard_redux_1280_jpg: (
        ArtworkEclipseBillboardRedux1280Jpg | None
    ) = None
    artwork_billboard_960_story_art_jpg: ArtworkBillboard960StoryArtJpg | None = None
    tagline_messages_odp: list[TaglineMessagesOdpItem] | None = Field(
        None,
        alias="taglineMessages_odp",
    )
    similar_videos: list[SimilarVideo] | None = Field(None, alias="similarVideos")
    num_seasons_label: str | None = Field(None, alias="numSeasonsLabel")
    primary_genres: PrimaryGenres | None = Field(None, alias="primaryGenres")
    content_warning: None = Field(None, alias="contentWarning")
    supplemental_videos_list_clips: SupplementalVideosListClips | None = Field(
        None,
        alias="supplementalVideosList_clips",
    )


class PlayableVideoNodrmH264mpl31HeaacMp4(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    url: str


class ArtworkBillboard1280StoryArtJpg1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    key: str
    url: str
    width: int
    height: int
    available: bool
    status: str
    focal_point: FocalPoint = Field(..., alias="focalPoint")


class ArtworkMerchStillJpg(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    url: str


class PlayableVideoNodrmH264bpl30HeaacMp4(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    url: str


class Supplemental(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    video_id: int = Field(..., alias="videoId")
    playable_video_nodrm_h264mpl31_heaac_mp4: (
        PlayableVideoNodrmH264mpl31HeaacMp4 | None
    ) = Field(None, alias="playableVideo_nodrm_h264mpl31_heaac_mp4")
    short_synopsis: str | None = Field(None, alias="shortSynopsis")
    title: str
    availability_start_time: AwareDatetime | None = Field(
        None,
        alias="availabilityStartTime",
    )
    artwork_billboard_1280_story_art_jpg: ArtworkBillboard1280StoryArtJpg1 | None = None
    display_runtime_ms: int | None = Field(None, alias="displayRuntimeMs")
    runtime_sec: int | None = Field(None, alias="runtimeSec")
    type: str | None = None
    artwork_merch_still_jpg: ArtworkMerchStillJpg | None = None
    playable_video_nodrm_h264bpl30_heaac_mp4: (
        PlayableVideoNodrmH264bpl30HeaacMp4 | None
    ) = Field(None, alias="playableVideo_nodrm_h264bpl30_heaac_mp4")


class Video(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__ref: str = Field(..., alias="__ref")


class PromoVideo(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    video: Video
    id: int


class Person(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    person_id: int = Field(..., alias="personId")
    name: str


class Genre(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    genre_id: int = Field(..., alias="genreId")
    name: str | None = None
    title: str | None = None


class EntityTag(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    id: int
    display_name: str = Field(..., alias="displayName")
    is_displayable: bool = Field(..., alias="isDisplayable")


class ArtworkMerchStill300Png(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    key: str
    url: str
    width: int
    height: int
    available: bool
    status: str
    focal_point: FocalPoint | None = Field(..., alias="focalPoint")


class Episode(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    video_id: int = Field(..., alias="videoId")
    title: str
    runtime_sec: int = Field(..., alias="runtimeSec")
    short_synopsis: str = Field(..., alias="shortSynopsis")
    number: int
    artwork_merch_still_300_png: ArtworkMerchStill300Png


class Edge7(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    node: Node


class PageInfo9(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    has_next_page: bool = Field(..., alias="hasNextPage")
    has_previous_page: bool = Field(..., alias="hasPreviousPage")
    start_cursor: str = Field(..., alias="startCursor")
    end_cursor: str = Field(..., alias="endCursor")


class Episodes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    total_count: int = Field(..., alias="totalCount")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge7]
    page_info: PageInfo9 = Field(..., alias="pageInfo")


class Season(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    video_id: int = Field(..., alias="videoId")
    number_label_v2_long: str = Field(..., alias="numberLabelV2_long")
    short_title: str = Field(..., alias="shortTitle")
    title: str
    total_display_runtime_in_sec: int = Field(..., alias="totalDisplayRuntimeInSec")
    show_member_type: str = Field(..., alias="showMemberType")
    episodes: Episodes


class MeshFilm(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    timestamp: AwareDatetime


class Title(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    movies: list[Movie]
    shows: list[Show]
    supplementals: list[Supplemental]
    promo_videos: list[PromoVideo] = Field(..., alias="promoVideos")
    persons: list[Person]
    genres: list[Genre]
    entity_tags: list[EntityTag] = Field(..., alias="entityTags")
    episodes: list[Episode]
    seasons: list[Season]
    meshfilm: MeshFilm
