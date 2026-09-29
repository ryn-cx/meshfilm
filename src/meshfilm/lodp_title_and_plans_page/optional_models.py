from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any

class FocalPoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    x: float | Any = Field(default=None, union_mode='left_to_right')
    y: float | Any = Field(default=None, union_mode='left_to_right')

class MerchStill300(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    available: bool | Any = Field(default=None, union_mode='left_to_right')
    focal_point: FocalPoint | Any = Field(None, alias='focalPoint', union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    key: str | Any = Field(default=None, union_mode='left_to_right')
    status: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')

class Node1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    video_id: int | Any = Field(None, alias='videoId', union_mode='left_to_right')
    number: int | Any = Field(default=None, union_mode='left_to_right')
    runtime_sec: int | Any = Field(None, alias='runtimeSec', union_mode='left_to_right')
    short_synopsis: str | Any = Field(None, alias='shortSynopsis', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    merch_still300: MerchStill300 | Any = Field(None, alias='merchStill300', union_mode='left_to_right')

class Edge1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    node: Node1 | Any = Field(default=None, union_mode='left_to_right')

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    has_next_page: bool | Any = Field(None, alias='hasNextPage', union_mode='left_to_right')

class Episodes(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    edges: list[Edge1] | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')

class Node(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    episodes: Episodes | Any = Field(default=None, union_mode='left_to_right')
    number_label_v2: str | Any = Field(None, alias='numberLabelV2', union_mode='left_to_right')
    short_title: str | Any = Field(None, alias='shortTitle', union_mode='left_to_right')
    show_member_type: str | Any = Field(None, alias='showMemberType', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    total_display_runtime_in_sec: int | Any = Field(None, alias='totalDisplayRuntimeInSec', union_mode='left_to_right')
    video_id: int | Any = Field(None, alias='videoId', union_mode='left_to_right')

class Edge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    node: Node | Any = Field(default=None, union_mode='left_to_right')

class Seasons(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    edges: list[Edge] | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')
    total_count: int | Any = Field(None, alias='totalCount', union_mode='left_to_right')

class BrandLogoCropped48h(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    available: bool | Any = Field(default=None, union_mode='left_to_right')
    focal_point: Any | None = Field(None, alias='focalPoint')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    key: str | Any = Field(default=None, union_mode='left_to_right')
    status: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')

class LogoStackCropped350(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    available: bool | Any = Field(default=None, union_mode='left_to_right')
    focal_point: Any | None = Field(None, alias='focalPoint')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    key: str | Any = Field(default=None, union_mode='left_to_right')
    status: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')

class TaglineMessage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    badge_prefix: Any | None = Field(None, alias='badgePrefix')
    render_countdown_timer: bool | Any = Field(None, alias='renderCountdownTimer', union_mode='left_to_right')
    tagline: str | Any = Field(default=None, union_mode='left_to_right')

class BillboardOrStoryArt960(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    available: bool | Any = Field(default=None, union_mode='left_to_right')
    focal_point: FocalPoint | Any = Field(None, alias='focalPoint', union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    key: str | Any = Field(default=None, union_mode='left_to_right')
    status: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')

class EclipseBillboardRedux1280(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    available: bool | Any = Field(default=None, union_mode='left_to_right')
    focal_point: FocalPoint | Any = Field(None, alias='focalPoint', union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    key: str | Any = Field(default=None, union_mode='left_to_right')
    status: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')

class EclipseBillboardRedux1920(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    available: bool | Any = Field(default=None, union_mode='left_to_right')
    focal_point: FocalPoint | Any = Field(None, alias='focalPoint', union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    key: str | Any = Field(default=None, union_mode='left_to_right')
    status: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')

class PlayableVideo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')

class BillboardOrStoryArt1280(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    available: bool | Any = Field(default=None, union_mode='left_to_right')
    focal_point: FocalPoint | Any = Field(None, alias='focalPoint', union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    key: str | Any = Field(default=None, union_mode='left_to_right')
    status: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')

class Video(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    video_id: int | Any = Field(None, alias='videoId', union_mode='left_to_right')
    playable_video: PlayableVideo | Any = Field(None, alias='playableVideo', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    availability_start_time: AwareDatetime | Any = Field(None, alias='availabilityStartTime', union_mode='left_to_right')
    short_synopsis: str | Any = Field(None, alias='shortSynopsis', union_mode='left_to_right')
    billboard_or_story_art1280: BillboardOrStoryArt1280 | Any = Field(None, alias='billboardOrStoryArt1280', union_mode='left_to_right')
    display_runtime_ms: int | Any = Field(None, alias='displayRuntimeMs', union_mode='left_to_right')

class PromoVideo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')
    video: Video | Any = Field(default=None, union_mode='left_to_right')

class ShareTaglineMessage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    tagline: str | Any = Field(default=None, union_mode='left_to_right')
    typed_classification: str | Any = Field(None, alias='typedClassification', union_mode='left_to_right')

class Artwork(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')

class Node2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    artwork: Artwork | Any = Field(default=None, union_mode='left_to_right')
    playable_video: PlayableVideo | Any = Field(None, alias='playableVideo', union_mode='left_to_right')
    runtime_sec: int | Any = Field(None, alias='runtimeSec', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    video_id: int | Any = Field(None, alias='videoId', union_mode='left_to_right')

class Edge2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    node: Node2 | Any = Field(default=None, union_mode='left_to_right')

class Trailers(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    edges: list[Edge2] | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')

class ContentAdvisory(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    certification_value: str | Any = Field(None, alias='certificationValue', union_mode='left_to_right')

class Node3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    genre_id: int | Any = Field(None, alias='genreId', union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')

class Edge3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    node: Node3 | Any = Field(default=None, union_mode='left_to_right')

class PrimaryGenres(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    edges: list[Edge3] | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')

class Node4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    person_id: int | Any = Field(None, alias='personId', union_mode='left_to_right')

class Edge4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    node: Node4 | Any = Field(default=None, union_mode='left_to_right')

class Actors(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    edges: list[Edge4] | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')

class Edge5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    node: Node4 | Any = Field(default=None, union_mode='left_to_right')

class Creators(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    edges: list[Edge5] | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')

class AudioTrack(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    language: str | Any = Field(default=None, union_mode='left_to_right')

class Subtitle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    language: str | Any = Field(default=None, union_mode='left_to_right')

class MediaTracks(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    audio_tracks: list[AudioTrack] | Any = Field(None, alias='audioTracks', union_mode='left_to_right')
    subtitles: list[Subtitle] | Any = Field(default=None, union_mode='left_to_right')

class Node6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    genre_id: int | Any = Field(None, alias='genreId', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')

class Edge6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    node: Node6 | Any = Field(default=None, union_mode='left_to_right')

class Genres(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    edges: list[Edge6] | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')

class Tag(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    display_name: str | Any = Field(None, alias='displayName', union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')
    is_displayable: bool | Any = Field(None, alias='isDisplayable', union_mode='left_to_right')

class TudumTitle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    slug: str | Any = Field(default=None, union_mode='left_to_right')

class Boxshot300(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    available: bool | Any = Field(default=None, union_mode='left_to_right')
    focal_point: Any | None = Field(None, alias='focalPoint')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    key: str | Any = Field(default=None, union_mode='left_to_right')
    status: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')

class SimilarVideo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    video_id: int | Any = Field(None, alias='videoId', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    boxshot300: Boxshot300 | Any = Field(default=None, union_mode='left_to_right')

class BillboardOrStoryArt12801(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    available: bool | Any = Field(default=None, union_mode='left_to_right')
    focal_point: FocalPoint | Any = Field(None, alias='focalPoint', union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    key: str | Any = Field(default=None, union_mode='left_to_right')
    status: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')

class Node7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    genre_id: int | Any = Field(None, alias='genreId', union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')

class Edge7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    node: Node7 | Any = Field(default=None, union_mode='left_to_right')

class CoreGenres(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    edges: list[Edge7] | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')

class Directors(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    edges: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')

class ThumbnailClips(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    edges: list[Any] | Any = Field(default=None, union_mode='left_to_right')

class LodpTitleAndPlansPageModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    video_id: int | Any = Field(None, alias='videoId', union_mode='left_to_right')
    seasons: Seasons | Any = Field(default=None, union_mode='left_to_right')
    all_tagline_messages_by_event_state: Any | None = Field(None, alias='allTaglineMessagesByEventState')
    next_event_window: Any | None = Field(None, alias='nextEventWindow')
    is_available: bool | Any = Field(None, alias='isAvailable', union_mode='left_to_right')
    next_live_event: Any | None = Field(None, alias='nextLiveEvent')
    brand_logo_cropped48h: BrandLogoCropped48h | Any = Field(None, alias='brandLogoCropped48h', union_mode='left_to_right')
    logo_stack_cropped350: LogoStackCropped350 | Any = Field(None, alias='logoStackCropped350', union_mode='left_to_right')
    tagline_messages: list[TaglineMessage] | Any = Field(None, alias='taglineMessages', union_mode='left_to_right')
    logged_out_taglines: Any | None = Field(None, alias='loggedOutTaglines')
    billboard_or_story_art960: BillboardOrStoryArt960 | Any = Field(None, alias='billboardOrStoryArt960', union_mode='left_to_right')
    eclipse_billboard_redux1280: EclipseBillboardRedux1280 | Any = Field(None, alias='eclipseBillboardRedux1280', union_mode='left_to_right')
    eclipse_billboard_redux1920: EclipseBillboardRedux1920 | Any = Field(None, alias='eclipseBillboardRedux1920', union_mode='left_to_right')
    promo_video: PromoVideo | Any = Field(None, alias='promoVideo', union_mode='left_to_right')
    share_tagline_messages: list[ShareTaglineMessage] | Any = Field(None, alias='shareTaglineMessages', union_mode='left_to_right')
    trailers: Trailers | Any = Field(default=None, union_mode='left_to_right')
    content_advisory: ContentAdvisory | Any = Field(None, alias='contentAdvisory', union_mode='left_to_right')
    latest_year: int | Any = Field(None, alias='latestYear', union_mode='left_to_right')
    primary_genres: PrimaryGenres | Any = Field(None, alias='primaryGenres', union_mode='left_to_right')
    short_synopsis: str | Any = Field(None, alias='shortSynopsis', union_mode='left_to_right')
    content_warning: Any | None = Field(None, alias='contentWarning')
    actors: Actors | Any = Field(default=None, union_mode='left_to_right')
    creators: Creators | Any = Field(default=None, union_mode='left_to_right')
    num_seasons_label: str | Any = Field(None, alias='numSeasonsLabel', union_mode='left_to_right')
    media_tracks: MediaTracks | Any = Field(None, alias='mediaTracks', union_mode='left_to_right')
    is_available_for_download: bool | Any = Field(None, alias='isAvailableForDownload', union_mode='left_to_right')
    genres: Genres | Any = Field(default=None, union_mode='left_to_right')
    tags: list[Tag] | Any = Field(default=None, union_mode='left_to_right')
    tudum_title: TudumTitle | Any = Field(None, alias='tudumTitle', union_mode='left_to_right')
    similar_videos: list[SimilarVideo] | Any = Field(None, alias='similarVideos', union_mode='left_to_right')
    has_original_treatment: bool | Any = Field(None, alias='hasOriginalTreatment', union_mode='left_to_right')
    billboard_or_story_art1280: BillboardOrStoryArt12801 | Any = Field(None, alias='billboardOrStoryArt1280', union_mode='left_to_right')
    availability_start_time: AwareDatetime | Any = Field(None, alias='availabilityStartTime', union_mode='left_to_right')
    core_genres: CoreGenres | Any = Field(None, alias='coreGenres', union_mode='left_to_right')
    directors: Directors | Any = Field(default=None, union_mode='left_to_right')
    thumbnail_clips: ThumbnailClips | Any = Field(None, alias='thumbnailClips', union_mode='left_to_right')
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
