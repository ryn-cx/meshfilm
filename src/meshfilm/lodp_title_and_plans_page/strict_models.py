from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, Field
from typing import Any

class Price(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    price_formatted: str = Field(..., alias='priceFormatted')
    price_in_cents: int = Field(..., alias='priceInCents')
    price_tier: str = Field(..., alias='priceTier')

class Attributes(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    audio_quality: str = Field(..., alias='audioQuality')
    has_ads: bool = Field(..., alias='hasAds')
    video_quality: str = Field(..., alias='videoQuality')

class Plan(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    plan_id: str = Field(..., alias='planId')
    price: Price
    attributes: Attributes
    name: str
    tag: None

class Plans(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    offer: None
    plans: list[Plan]

class Boxshot300(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    available: bool
    focal_point: None = Field(..., alias='focalPoint')
    height: int
    key: str
    status: str
    url: str
    width: int

class Video(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    video_id: int = Field(..., alias='videoId')
    title: str
    boxshot300: Boxshot300

class Collection(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    videos: list[Video]

class TrifectaRows(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    collections: list[Collection]

class FocalPoint(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    x: float
    y: float

class MerchStill300(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    available: bool
    focal_point: FocalPoint = Field(..., alias='focalPoint')
    height: int
    key: str
    status: str
    url: str
    width: int

class Node1(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    video_id: int = Field(..., alias='videoId')
    number: int
    runtime_sec: int = Field(..., alias='runtimeSec')
    short_synopsis: str = Field(..., alias='shortSynopsis')
    title: str
    merch_still300: MerchStill300 = Field(..., alias='merchStill300')

class Edge1(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    node: Node1

class PageInfo(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    has_next_page: bool = Field(..., alias='hasNextPage')

class Episodes(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    edges: list[Edge1]
    page_info: PageInfo = Field(..., alias='pageInfo')

class Node(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    episodes: Episodes
    number_label_v2: str = Field(..., alias='numberLabelV2')
    short_title: str = Field(..., alias='shortTitle')
    show_member_type: str = Field(..., alias='showMemberType')
    title: str
    total_display_runtime_in_sec: int = Field(..., alias='totalDisplayRuntimeInSec')
    video_id: int = Field(..., alias='videoId')

class Edge(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    node: Node

class Seasons(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    edges: list[Edge]
    page_info: PageInfo = Field(..., alias='pageInfo')
    total_count: int = Field(..., alias='totalCount')

class BrandLogoCropped48h(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    available: bool
    focal_point: None = Field(..., alias='focalPoint')
    height: int
    key: str
    status: str
    url: str
    width: int

class LogoStackCropped350(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    available: bool
    focal_point: None = Field(..., alias='focalPoint')
    height: int
    key: str
    status: str
    url: str
    width: int

class TaglineMessage(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    badge_prefix: None = Field(..., alias='badgePrefix')
    render_countdown_timer: bool = Field(..., alias='renderCountdownTimer')
    tagline: str

class BillboardOrStoryArt960(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    available: bool
    focal_point: FocalPoint = Field(..., alias='focalPoint')
    height: int
    key: str
    status: str
    url: str
    width: int

class EclipseBillboardRedux1280(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    available: bool
    focal_point: FocalPoint = Field(..., alias='focalPoint')
    height: int
    key: str
    status: str
    url: str
    width: int

class EclipseBillboardRedux1920(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    available: bool
    focal_point: FocalPoint = Field(..., alias='focalPoint')
    height: int
    key: str
    status: str
    url: str
    width: int

class PlayableVideo(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    url: str

class BillboardOrStoryArt1280(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    available: bool
    focal_point: FocalPoint = Field(..., alias='focalPoint')
    height: int
    key: str
    status: str
    url: str
    width: int

class Video2(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    video_id: int = Field(..., alias='videoId')
    playable_video: PlayableVideo = Field(..., alias='playableVideo')
    title: str
    availability_start_time: AwareDatetime = Field(..., alias='availabilityStartTime')
    short_synopsis: str = Field(..., alias='shortSynopsis')
    billboard_or_story_art1280: BillboardOrStoryArt1280 = Field(..., alias='billboardOrStoryArt1280')
    display_runtime_ms: int = Field(..., alias='displayRuntimeMs')

class PromoVideo(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    id: int
    video: Video2

class ShareTaglineMessage(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    tagline: str
    typed_classification: str = Field(..., alias='typedClassification')

class Artwork(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    url: str

class Node2(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    artwork: Artwork
    playable_video: PlayableVideo = Field(..., alias='playableVideo')
    runtime_sec: int = Field(..., alias='runtimeSec')
    title: str
    type: str
    video_id: int = Field(..., alias='videoId')

class Edge2(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    node: Node2

class Trailers(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    edges: list[Edge2]
    page_info: PageInfo = Field(..., alias='pageInfo')

class ContentAdvisory(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    certification_value: str = Field(..., alias='certificationValue')

class Node3(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    genre_id: int = Field(..., alias='genreId')
    name: str

class Edge3(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    node: Node3

class PrimaryGenres(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    edges: list[Edge3]
    page_info: PageInfo = Field(..., alias='pageInfo')

class Node4(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    name: str
    person_id: int = Field(..., alias='personId')

class Edge4(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    node: Node4

class Actors(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    edges: list[Edge4]
    page_info: PageInfo = Field(..., alias='pageInfo')

class Edge5(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    node: Node4

class Creators(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    edges: list[Edge5]
    page_info: PageInfo = Field(..., alias='pageInfo')

class AudioTrack(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    language: str

class Subtitle(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    language: str

class MediaTracks(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    audio_tracks: list[AudioTrack] = Field(..., alias='audioTracks')
    subtitles: list[Subtitle]

class Node6(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    genre_id: int = Field(..., alias='genreId')
    title: str

class Edge6(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    node: Node6

class Genres(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    edges: list[Edge6]
    page_info: PageInfo = Field(..., alias='pageInfo')

class Tag(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    display_name: str = Field(..., alias='displayName')
    id: int
    is_displayable: bool = Field(..., alias='isDisplayable')

class TudumTitle(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    slug: str

class SimilarVideo(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    video_id: int = Field(..., alias='videoId')
    title: str
    boxshot300: Boxshot300

class BillboardOrStoryArt12801(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    available: bool
    focal_point: FocalPoint = Field(..., alias='focalPoint')
    height: int
    key: str
    status: str
    url: str
    width: int

class Node7(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    genre_id: int = Field(..., alias='genreId')
    name: str

class Edge7(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    node: Node7

class CoreGenres(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    edges: list[Edge7]
    page_info: PageInfo = Field(..., alias='pageInfo')

class Node8(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    name: str
    person_id: int = Field(..., alias='personId')

class Edge8(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    node: Node8

class Directors(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    edges: list[Edge8]
    page_info: PageInfo = Field(..., alias='pageInfo')

class ThumbnailClips(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    edges: list[None]

class Video1(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    title: str
    video_id: int = Field(..., alias='videoId')
    seasons: Seasons | None = None
    all_tagline_messages_by_event_state: None = Field(..., alias='allTaglineMessagesByEventState')
    next_event_window: None = Field(None, alias='nextEventWindow')
    is_available: bool = Field(..., alias='isAvailable')
    next_live_event: None = Field(None, alias='nextLiveEvent')
    brand_logo_cropped48h: BrandLogoCropped48h = Field(..., alias='brandLogoCropped48h')
    logo_stack_cropped350: LogoStackCropped350 = Field(..., alias='logoStackCropped350')
    tagline_messages: list[TaglineMessage] = Field(..., alias='taglineMessages')
    logged_out_taglines: None = Field(..., alias='loggedOutTaglines')
    billboard_or_story_art960: BillboardOrStoryArt960 = Field(..., alias='billboardOrStoryArt960')
    eclipse_billboard_redux1280: EclipseBillboardRedux1280 = Field(..., alias='eclipseBillboardRedux1280')
    eclipse_billboard_redux1920: EclipseBillboardRedux1920 = Field(..., alias='eclipseBillboardRedux1920')
    promo_video: PromoVideo = Field(..., alias='promoVideo')
    share_tagline_messages: list[ShareTaglineMessage] = Field(..., alias='shareTaglineMessages')
    trailers: Trailers
    content_advisory: ContentAdvisory = Field(..., alias='contentAdvisory')
    latest_year: int = Field(..., alias='latestYear')
    primary_genres: PrimaryGenres = Field(..., alias='primaryGenres')
    short_synopsis: str = Field(..., alias='shortSynopsis')
    content_warning: None = Field(..., alias='contentWarning')
    actors: Actors
    creators: Creators
    num_seasons_label: str | None = Field(None, alias='numSeasonsLabel')
    media_tracks: MediaTracks = Field(..., alias='mediaTracks')
    is_available_for_download: bool = Field(..., alias='isAvailableForDownload')
    genres: Genres
    tags: list[Tag]
    tudum_title: TudumTitle | None = Field(..., alias='tudumTitle')
    similar_videos: list[SimilarVideo] = Field(..., alias='similarVideos')
    has_original_treatment: bool = Field(..., alias='hasOriginalTreatment')
    billboard_or_story_art1280: BillboardOrStoryArt12801 = Field(..., alias='billboardOrStoryArt1280')
    availability_start_time: AwareDatetime = Field(..., alias='availabilityStartTime')
    core_genres: CoreGenres = Field(..., alias='coreGenres')
    directors: Directors
    thumbnail_clips: ThumbnailClips = Field(..., alias='thumbnailClips')
    event_window: None = Field(None, alias='eventWindow')
    live_event: None = Field(None, alias='liveEvent')

class Data(BaseModel):
    plans: Plans
    trifecta_rows: TrifectaRows = Field(..., alias='trifectaRows')
    videos: list[Video1]

class LodpTitleAndPlansPageModel(BaseModel):
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
