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

class PlaybackEntity(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    video_id: int | None = Field(None, alias='videoId')

class BroadcastInfo(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    distributor_name: Any | None = Field(None, alias='distributorName')
    release_date: Any | None = Field(None, alias='releaseDate')

class Node(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    name: str | None = None
    person_id: int | None = Field(None, alias='personId')

class Edge(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    cursor: str | None = None
    node: Node | None = None

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    has_next_page: bool | None = Field(None, alias='hasNextPage')

class Cast(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    edges: list[Edge] | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')

class Edge1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    cursor: str | None = None
    node: Node | None = None

class Creators(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    edges: list[Edge1] | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')

class Edge2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    cursor: str | None = None
    node: Node | None = None

class Directors(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    edges: list[Edge2] | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')

class Edge3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    cursor: str | None = None
    node: Node | None = None

class Writers(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    edges: list[Edge3] | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')

class Node4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    genre_id: int | None = Field(None, alias='genreId')
    name: str | None = None

class Edge4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    cursor: str | None = None
    node: Node4 | None = None

class GenreTags(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    edges: list[Edge4] | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')

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

class MoodTag(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    display_name: str | None = Field(None, alias='displayName')
    id: int | None = None
    is_displayable: bool | None = Field(None, alias='isDisplayable')
    is_mood: bool | None = Field(None, alias='isMood')

class ContextualSynopsis(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    evidence_key: str | None = Field(None, alias='evidenceKey')
    text: str | None = None

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
    parent_season: ParentSeason | None = Field(None, alias='parentSeason')
    video_id: int | None = Field(None, alias='videoId')
    hide_episode_numbers: bool | None = Field(None, alias='hideEpisodeNumbers')
    number: int | None = None
    title: str | None = None
    badges: list[str] | None = None
    watch_status: str | None = Field(None, alias='watchStatus')
    contextual_synopsis: ContextualSynopsis | None = Field(None, alias='contextualSynopsis')
    runtime_sec: int | None = Field(None, alias='runtimeSec')
    bookmark: Any | None = None

class Seasons(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    total_count: int | None = Field(None, alias='totalCount')

class MostLikedMessage(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    tagline: str | None = None
    typed_classification: str | None = Field(None, alias='typedClassification')

class TaglineMessage(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    cta_message: Any | None = Field(None, alias='ctaMessage')
    tagline: str | None = None
    typed_classification: str | None = Field(None, alias='typedClassification')

class Similar(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    video_id: int | None = Field(None, alias='videoId')

class Node5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    video_id: int | None = Field(None, alias='videoId')

class Edge5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    node: Node5 | None = None

class SupplementalVideosList(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    edges: list[Edge5] | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')

class Sibling(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    video_id: int | None = Field(None, alias='videoId')

class TitleGroupMembership(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    id: str | None = None
    kind: str | None = None
    siblings: list[Sibling] | None = None
    title: str | None = None

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

class ParentSeason1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    episodes: Episodes | None = None
    video_id: int | None = Field(None, alias='videoId')

class CurrentEpisode1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    parent_season: ParentSeason1 | None = Field(None, alias='parentSeason')
    video_id: int | None = Field(None, alias='videoId')

class ParentShow(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    current_episode: CurrentEpisode1 | None = Field(None, alias='currentEpisode')
    num_seasons_label: str | None = Field(None, alias='numSeasonsLabel')
    seasons: Seasons | None = None
    video_id: int | None = Field(None, alias='videoId')
    title_group_memberships: list[Any] | None = Field(None, alias='titleGroupMemberships')

class ParentSeason2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    hide_episode_numbers: bool | None = Field(None, alias='hideEpisodeNumbers')
    number: int | None = None
    number_label: str | None = Field(None, alias='numberLabel')
    title: str | None = None
    video_id: int | None = Field(None, alias='videoId')

class UnifiedEntity(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    video_id: int | None = Field(None, alias='videoId')
    is_available: bool | None = Field(None, alias='isAvailable')
    is_playable: bool | None = Field(None, alias='isPlayable')
    unplayable_causes: Any | None = Field(None, alias='unplayableCauses')
    title: str | None = None
    next_live_event: Any | None = Field(None, alias='nextLiveEvent')
    broadcast_info: BroadcastInfo | None = Field(None, alias='broadcastInfo')
    copyright: Any | None = None
    cast: Cast | None = None
    creators: Creators | None = None
    directors: Directors | None = None
    writers: Writers | None = None
    genre_tags: GenreTags | None = Field(None, alias='genreTags')
    content_advisory: ContentAdvisory | None = Field(None, alias='contentAdvisory')
    mood_tags: list[MoodTag] | None = Field(None, alias='moodTags')
    content_warning: Any | None = Field(None, alias='contentWarning')
    unified_entity_id: str | None = Field(None, alias='unifiedEntityId')
    contextual_synopsis: ContextualSynopsis | None = Field(None, alias='contextualSynopsis')
    latest_year: int | None = Field(None, alias='latestYear')
    playback_badges: list[str] | None = Field(None, alias='playbackBadges')
    has_recurring_releases: bool | None = Field(None, alias='hasRecurringReleases')
    is_in_playlist: bool | None = Field(None, alias='isInPlaylist')
    is_in_remind_me_list: bool | None = Field(None, alias='isInRemindMeList')
    is_in_rolling_reminders_list: bool | None = Field(None, alias='isInRollingRemindersList')
    playlist_actions: Any | None = Field(None, alias='playlistActions')
    current_episode: CurrentEpisode | None = Field(None, alias='currentEpisode')
    num_seasons_label: str | None = Field(None, alias='numSeasonsLabel')
    seasons: Seasons | None = None
    most_liked_messages: list[MostLikedMessage] | None = Field(None, alias='mostLikedMessages')
    tagline_messages: list[TaglineMessage] | None = Field(None, alias='taglineMessages')
    similars: list[Similar] | None = None
    ryan_murphy_collection_ids: list[Any] | None = Field(None, alias='ryanMurphyCollectionIds')
    shonda_rhimes_collection_ids: list[Any] | None = Field(None, alias='shondaRhimesCollectionIds')
    supplemental_videos_list: SupplementalVideosList | None = Field(None, alias='supplementalVideosList')
    title_group_memberships: list[TitleGroupMembership] | None = Field(None, alias='titleGroupMemberships')
    thumbs_rating: Any | None = Field(None, alias='thumbsRating')
    boxart: Boxart | None = None
    boxart_high_res: BoxartHighRes | None = Field(None, alias='boxartHighRes')
    brand_logo_small: BrandLogoSmall | None = Field(None, alias='brandLogoSmall')
    live_now: Any | None = Field(None, alias='liveNow')
    story_art: StoryArt | None = Field(None, alias='storyArt')
    title_logo_branded: TitleLogoBranded | None = Field(None, alias='titleLogoBranded')
    title_logo_unbranded: TitleLogoUnbranded | None = Field(None, alias='titleLogoUnbranded')
    tf1_collection_ids: list[Any] | None = Field(None, alias='tf1CollectionIds')
    watch_status: str | None = Field(None, alias='watchStatus')
    thumb_rating: Any | None = Field(None, alias='thumbRating')
    live_event: Any | None = Field(None, alias='liveEvent')
    parent_show: ParentShow | None = Field(None, alias='parentShow')
    display_runtime_sec: int | None = Field(None, alias='displayRuntimeSec')
    hide_episode_numbers: bool | None = Field(None, alias='hideEpisodeNumbers')
    number: int | None = None
    parent_season: ParentSeason2 | None = Field(None, alias='parentSeason')
    badges: list[str] | None = None
    bookmark: Any | None = None
    runtime_sec: int | None = Field(None, alias='runtimeSec')

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore')
    playback_entities: list[PlaybackEntity] | None = Field(None, alias='playbackEntities')
    unified_entities: list[UnifiedEntity] | None = Field(None, alias='unifiedEntities')

class DetailModalModel(BaseModel):
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
