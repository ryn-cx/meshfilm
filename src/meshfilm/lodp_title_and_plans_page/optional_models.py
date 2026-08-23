from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any

class Price(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    price_formatted: str | None = Field(None, alias='priceFormatted')
    price_in_cents: int | None = Field(None, alias='priceInCents')
    price_tier: str | None = Field(None, alias='priceTier')

class Attributes(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    audio_quality: str | None = Field(None, alias='audioQuality')
    has_ads: bool | None = Field(None, alias='hasAds')
    video_quality: str | None = Field(None, alias='videoQuality')

class Plan(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    plan_id: str | None = Field(None, alias='planId')
    price: Price | None = None
    attributes: Attributes | None = None
    name: str | None = None
    tag: Any | None = None

class Plans(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    offer: Any | None = None
    plans: list[Plan] | None = None

class Boxshot300(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    available: bool | None = None
    focal_point: Any | None = Field(None, alias='focalPoint')
    height: int | None = None
    key: str | None = None
    status: str | None = None
    url: str | None = None
    width: int | None = None

class Video(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    video_id: int | None = Field(None, alias='videoId')
    title: str | None = None
    boxshot300: Boxshot300 | None = None

class Collection(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    videos: list[Video] | None = None

class TrifectaRows(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    collections: list[Collection] | None = None

class FocalPoint(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    x: float | None = None
    y: float | None = None

class MerchStill300(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    available: bool | None = None
    focal_point: FocalPoint | None = Field(None, alias='focalPoint')
    height: int | None = None
    key: str | None = None
    status: str | None = None
    url: str | None = None
    width: int | None = None

class Node1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    video_id: int | None = Field(None, alias='videoId')
    number: int | None = None
    runtime_sec: int | None = Field(None, alias='runtimeSec')
    short_synopsis: str | None = Field(None, alias='shortSynopsis')
    title: str | None = None
    merch_still300: MerchStill300 | None = Field(None, alias='merchStill300')

class Edge1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    node: Node1 | None = None

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    has_next_page: bool | None = Field(None, alias='hasNextPage')

class Episodes(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    edges: list[Edge1] | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')

class Node(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    episodes: Episodes | None = None
    number_label_v2: str | None = Field(None, alias='numberLabelV2')
    short_title: str | None = Field(None, alias='shortTitle')
    show_member_type: str | None = Field(None, alias='showMemberType')
    title: str | None = None
    total_display_runtime_in_sec: int | None = Field(None, alias='totalDisplayRuntimeInSec')
    video_id: int | None = Field(None, alias='videoId')

class Edge(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    node: Node | None = None

class Seasons(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    edges: list[Edge] | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')
    total_count: int | None = Field(None, alias='totalCount')

class BrandLogoCropped48h(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    available: bool | None = None
    focal_point: Any | None = Field(None, alias='focalPoint')
    height: int | None = None
    key: str | None = None
    status: str | None = None
    url: str | None = None
    width: int | None = None

class LogoStackCropped350(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    available: bool | None = None
    focal_point: Any | None = Field(None, alias='focalPoint')
    height: int | None = None
    key: str | None = None
    status: str | None = None
    url: str | None = None
    width: int | None = None

class TaglineMessage(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    badge_prefix: Any | None = Field(None, alias='badgePrefix')
    render_countdown_timer: bool | None = Field(None, alias='renderCountdownTimer')
    tagline: str | None = None

class BillboardOrStoryArt960(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    available: bool | None = None
    focal_point: FocalPoint | None = Field(None, alias='focalPoint')
    height: int | None = None
    key: str | None = None
    status: str | None = None
    url: str | None = None
    width: int | None = None

class EclipseBillboardRedux1280(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    available: bool | None = None
    focal_point: FocalPoint | None = Field(None, alias='focalPoint')
    height: int | None = None
    key: str | None = None
    status: str | None = None
    url: str | None = None
    width: int | None = None

class EclipseBillboardRedux1920(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    available: bool | None = None
    focal_point: FocalPoint | None = Field(None, alias='focalPoint')
    height: int | None = None
    key: str | None = None
    status: str | None = None
    url: str | None = None
    width: int | None = None

class PlayableVideo(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    url: str | None = None

class BillboardOrStoryArt1280(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    available: bool | None = None
    focal_point: FocalPoint | None = Field(None, alias='focalPoint')
    height: int | None = None
    key: str | None = None
    status: str | None = None
    url: str | None = None
    width: int | None = None

class Video2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    video_id: int | None = Field(None, alias='videoId')
    playable_video: PlayableVideo | None = Field(None, alias='playableVideo')
    title: str | None = None
    availability_start_time: AwareDatetime | None = Field(None, alias='availabilityStartTime')
    short_synopsis: str | None = Field(None, alias='shortSynopsis')
    billboard_or_story_art1280: BillboardOrStoryArt1280 | None = Field(None, alias='billboardOrStoryArt1280')
    display_runtime_ms: int | None = Field(None, alias='displayRuntimeMs')

class PromoVideo(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    id: int | None = None
    video: Video2 | None = None

class ShareTaglineMessage(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    tagline: str | None = None
    typed_classification: str | None = Field(None, alias='typedClassification')

class Artwork(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    url: str | None = None

class Node2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    artwork: Artwork | None = None
    playable_video: PlayableVideo | None = Field(None, alias='playableVideo')
    runtime_sec: int | None = Field(None, alias='runtimeSec')
    title: str | None = None
    type: str | None = None
    video_id: int | None = Field(None, alias='videoId')

class Edge2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    node: Node2 | None = None

class Trailers(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    edges: list[Edge2] | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')

class ContentAdvisory(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    certification_value: str | None = Field(None, alias='certificationValue')

class Node3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    genre_id: int | None = Field(None, alias='genreId')
    name: str | None = None

class Edge3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    node: Node3 | None = None

class PrimaryGenres(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    edges: list[Edge3] | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')

class Node4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    name: str | None = None
    person_id: int | None = Field(None, alias='personId')

class Edge4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    node: Node4 | None = None

class Actors(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    edges: list[Edge4] | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')

class Edge5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    node: Node4 | None = None

class Creators(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    edges: list[Edge5] | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')

class AudioTrack(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    language: str | None = None

class Subtitle(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    language: str | None = None

class MediaTracks(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    audio_tracks: list[AudioTrack] | None = Field(None, alias='audioTracks')
    subtitles: list[Subtitle] | None = None

class Node6(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    genre_id: int | None = Field(None, alias='genreId')
    title: str | None = None

class Edge6(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    node: Node6 | None = None

class Genres(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    edges: list[Edge6] | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')

class Tag(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    display_name: str | None = Field(None, alias='displayName')
    id: int | None = None
    is_displayable: bool | None = Field(None, alias='isDisplayable')

class TudumTitle(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    slug: str | None = None

class SimilarVideo(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    video_id: int | None = Field(None, alias='videoId')
    title: str | None = None
    boxshot300: Boxshot300 | None = None

class BillboardOrStoryArt12801(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    available: bool | None = None
    focal_point: FocalPoint | None = Field(None, alias='focalPoint')
    height: int | None = None
    key: str | None = None
    status: str | None = None
    url: str | None = None
    width: int | None = None

class Node7(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    genre_id: int | None = Field(None, alias='genreId')
    name: str | None = None

class Edge7(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    node: Node7 | None = None

class CoreGenres(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    edges: list[Edge7] | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')

class Node8(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    name: str | None = None
    person_id: int | None = Field(None, alias='personId')

class Edge8(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    node: Node8 | None = None

class Directors(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    edges: list[Edge8] | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')

class ThumbnailClips(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    edges: list[Any] | None = None

class Video1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    title: str | None = None
    video_id: int | None = Field(None, alias='videoId')
    seasons: Seasons | None = None
    all_tagline_messages_by_event_state: Any | None = Field(None, alias='allTaglineMessagesByEventState')
    next_event_window: Any | None = Field(None, alias='nextEventWindow')
    is_available: bool | None = Field(None, alias='isAvailable')
    next_live_event: Any | None = Field(None, alias='nextLiveEvent')
    brand_logo_cropped48h: BrandLogoCropped48h | None = Field(None, alias='brandLogoCropped48h')
    logo_stack_cropped350: LogoStackCropped350 | None = Field(None, alias='logoStackCropped350')
    tagline_messages: list[TaglineMessage] | None = Field(None, alias='taglineMessages')
    logged_out_taglines: Any | None = Field(None, alias='loggedOutTaglines')
    billboard_or_story_art960: BillboardOrStoryArt960 | None = Field(None, alias='billboardOrStoryArt960')
    eclipse_billboard_redux1280: EclipseBillboardRedux1280 | None = Field(None, alias='eclipseBillboardRedux1280')
    eclipse_billboard_redux1920: EclipseBillboardRedux1920 | None = Field(None, alias='eclipseBillboardRedux1920')
    promo_video: PromoVideo | None = Field(None, alias='promoVideo')
    share_tagline_messages: list[ShareTaglineMessage] | None = Field(None, alias='shareTaglineMessages')
    trailers: Trailers | None = None
    content_advisory: ContentAdvisory | None = Field(None, alias='contentAdvisory')
    latest_year: int | None = Field(None, alias='latestYear')
    primary_genres: PrimaryGenres | None = Field(None, alias='primaryGenres')
    short_synopsis: str | None = Field(None, alias='shortSynopsis')
    content_warning: Any | None = Field(None, alias='contentWarning')
    actors: Actors | None = None
    creators: Creators | None = None
    num_seasons_label: str | None = Field(None, alias='numSeasonsLabel')
    media_tracks: MediaTracks | None = Field(None, alias='mediaTracks')
    is_available_for_download: bool | None = Field(None, alias='isAvailableForDownload')
    genres: Genres | None = None
    tags: list[Tag] | None = None
    tudum_title: Any | TudumTitle | None = Field(None, alias='tudumTitle')
    similar_videos: list[SimilarVideo] | None = Field(None, alias='similarVideos')
    has_original_treatment: bool | None = Field(None, alias='hasOriginalTreatment')
    billboard_or_story_art1280: BillboardOrStoryArt12801 | None = Field(None, alias='billboardOrStoryArt1280')
    availability_start_time: AwareDatetime | None = Field(None, alias='availabilityStartTime')
    core_genres: CoreGenres | None = Field(None, alias='coreGenres')
    directors: Directors | None = None
    thumbnail_clips: ThumbnailClips | None = Field(None, alias='thumbnailClips')
    event_window: Any | None = Field(None, alias='eventWindow')
    live_event: Any | None = Field(None, alias='liveEvent')

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore')
    plans: Plans | None = None
    trifecta_rows: TrifectaRows | None = Field(None, alias='trifectaRows')
    videos: list[Video1] | None = None

class LodpTitleAndPlansPageModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
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
