from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import AwareDatetime, BaseModel, Field
from typing import Any

class BroadcastInfo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    distributor_name: None = Field(..., alias='distributorName')
    release_date: AwareDatetime | None = Field(..., alias='releaseDate')

class Node(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    name: str
    person_id: int = Field(..., alias='personId')

class Edge(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    cursor: str
    node: Node

class PageInfo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    has_next_page: bool = Field(..., alias='hasNextPage')

class Cast(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    edges: list[Edge]
    page_info: PageInfo = Field(..., alias='pageInfo')

class Edge1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    cursor: str
    node: Node

class Creators(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    edges: list[Edge1]
    page_info: PageInfo = Field(..., alias='pageInfo')

class Edge2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    cursor: str
    node: Node

class Directors(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    edges: list[Edge2]
    page_info: PageInfo = Field(..., alias='pageInfo')

class Edge3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    cursor: str
    node: Node

class Writers(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    edges: list[Edge3]
    page_info: PageInfo = Field(..., alias='pageInfo')

class Node4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    genre_id: int = Field(..., alias='genreId')
    name: str

class Edge4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    cursor: str
    node: Node4

class GenreTags(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    edges: list[Edge4]
    page_info: PageInfo = Field(..., alias='pageInfo')

class Reason(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    icon_id: int = Field(..., alias='iconId')
    level: str
    text: str

class ContentAdvisory(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    board_id: int = Field(..., alias='boardId')
    board_name: str = Field(..., alias='boardName')
    certification_rating_id: int = Field(..., alias='certificationRatingId')
    certification_value: str = Field(..., alias='certificationValue')
    i18n_reasons_text: str | None = Field(..., alias='i18nReasonsText')
    maturity_description: str = Field(..., alias='maturityDescription')
    maturity_level: int = Field(..., alias='maturityLevel')
    reasons: list[Reason]
    video_specific_rating_reason: str | None = Field(..., alias='videoSpecificRatingReason')

class MoodTag(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    display_name: str = Field(..., alias='displayName')
    id: int
    is_displayable: bool = Field(..., alias='isDisplayable')
    is_mood: bool = Field(..., alias='isMood')

class ContextualSynopsis(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    evidence_key: str = Field(..., alias='evidenceKey')
    text: str

class Episodes(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    total_count: int = Field(..., alias='totalCount')

class ParentSeason(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    episodes: Episodes
    video_id: int = Field(..., alias='videoId')
    hide_episode_numbers: bool = Field(..., alias='hideEpisodeNumbers')
    number: int
    number_label: str = Field(..., alias='numberLabel')
    title: str

class CurrentEpisode(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    parent_season: ParentSeason = Field(..., alias='parentSeason')
    video_id: int = Field(..., alias='videoId')
    hide_episode_numbers: bool = Field(..., alias='hideEpisodeNumbers')
    number: int
    title: str
    badges: list[str]
    watch_status: str = Field(..., alias='watchStatus')
    contextual_synopsis: ContextualSynopsis = Field(..., alias='contextualSynopsis')
    runtime_sec: int = Field(..., alias='runtimeSec')
    bookmark: None

class Seasons(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    total_count: int = Field(..., alias='totalCount')

class MostLikedMessage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    tagline: str
    typed_classification: str = Field(..., alias='typedClassification')

class TaglineMessage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    cta_message: None = Field(..., alias='ctaMessage')
    tagline: str
    typed_classification: str = Field(..., alias='typedClassification')

class Similar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    video_id: int = Field(..., alias='videoId')

class Node5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    video_id: int = Field(..., alias='videoId')

class Edge5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    node: Node5

class SupplementalVideosList(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    edges: list[Edge5]
    page_info: PageInfo = Field(..., alias='pageInfo')

class Sibling(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    video_id: int = Field(..., alias='videoId')

class TitleGroupMembership(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    id: str
    kind: str
    siblings: list[Sibling] | None
    title: str

class Boxart(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    available: bool
    focal_point: None = Field(..., alias='focalPoint')
    height: int
    key: str
    status: str
    url: str
    width: int

class BoxartHighRes(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    available: bool
    focal_point: None = Field(..., alias='focalPoint')
    height: int
    key: str
    status: str
    url: str
    width: int

class BrandLogoSmall(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    available: bool
    focal_point: None = Field(..., alias='focalPoint')
    height: int
    key: str
    status: str
    url: str
    width: int

class FocalPoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    x: float
    y: float

class StoryArt(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    available: bool
    focal_point: FocalPoint | None = Field(..., alias='focalPoint')
    height: int
    key: str
    status: str
    url: str
    width: int

class TitleLogoBranded(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    available: bool
    focal_point: None = Field(..., alias='focalPoint')
    height: int
    key: str
    status: str
    url: str
    width: int

class TitleLogoUnbranded(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    available: bool
    focal_point: None = Field(..., alias='focalPoint')
    height: int
    key: str
    status: str
    url: str
    width: int

class DetailModalModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    video_id: int = Field(..., alias='videoId')
    is_available: bool = Field(..., alias='isAvailable')
    is_playable: bool = Field(..., alias='isPlayable')
    unplayable_causes: None = Field(..., alias='unplayableCauses')
    title: str
    next_live_event: None = Field(None, alias='nextLiveEvent')
    broadcast_info: BroadcastInfo = Field(..., alias='broadcastInfo')
    copyright: None
    cast: Cast
    creators: Creators
    directors: Directors
    writers: Writers
    genre_tags: GenreTags = Field(..., alias='genreTags')
    content_advisory: ContentAdvisory = Field(..., alias='contentAdvisory')
    mood_tags: list[MoodTag] = Field(..., alias='moodTags')
    content_warning: None = Field(..., alias='contentWarning')
    unified_entity_id: str = Field(..., alias='unifiedEntityId')
    contextual_synopsis: ContextualSynopsis = Field(..., alias='contextualSynopsis')
    latest_year: int = Field(..., alias='latestYear')
    playback_badges: list[str] = Field(..., alias='playbackBadges')
    has_recurring_releases: bool = Field(..., alias='hasRecurringReleases')
    is_in_playlist: bool = Field(..., alias='isInPlaylist')
    is_in_remind_me_list: bool = Field(..., alias='isInRemindMeList')
    is_in_rolling_reminders_list: bool = Field(..., alias='isInRollingRemindersList')
    playlist_actions: None = Field(..., alias='playlistActions')
    current_episode: CurrentEpisode | None = Field(None, alias='currentEpisode')
    num_seasons_label: str | None = Field(None, alias='numSeasonsLabel')
    seasons: Seasons | None = None
    most_liked_messages: list[MostLikedMessage] = Field(..., alias='mostLikedMessages')
    tagline_messages: list[TaglineMessage] = Field(..., alias='taglineMessages')
    similars: list[Similar]
    ryan_murphy_collection_ids: list[None] = Field(..., alias='ryanMurphyCollectionIds')
    shonda_rhimes_collection_ids: list[None] = Field(..., alias='shondaRhimesCollectionIds')
    supplemental_videos_list: SupplementalVideosList = Field(..., alias='supplementalVideosList')
    title_group_memberships: list[TitleGroupMembership] = Field(..., alias='titleGroupMemberships')
    thumbs_rating: None = Field(..., alias='thumbsRating')
    boxart: Boxart
    boxart_high_res: BoxartHighRes = Field(..., alias='boxartHighRes')
    brand_logo_small: BrandLogoSmall | None = Field(..., alias='brandLogoSmall')
    live_now: None = Field(..., alias='liveNow')
    story_art: StoryArt = Field(..., alias='storyArt')
    title_logo_branded: TitleLogoBranded = Field(..., alias='titleLogoBranded')
    title_logo_unbranded: TitleLogoUnbranded = Field(..., alias='titleLogoUnbranded')
    tf1_collection_ids: list[None] = Field(..., alias='tf1CollectionIds')
    watch_status: str = Field(..., alias='watchStatus')
    thumb_rating: None = Field(..., alias='thumbRating')
    live_event: None = Field(None, alias='liveEvent')
    display_runtime_sec: int | None = Field(None, alias='displayRuntimeSec')
    badges: list[str] | None = None
    bookmark: None = Field(None)
    runtime_sec: int | None = Field(None, alias='runtimeSec')
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
