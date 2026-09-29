from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any

class BroadcastInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    distributor_name: Any | None = Field(None, alias='distributorName')
    release_date: AwareDatetime | Any = Field(None, alias='releaseDate', union_mode='left_to_right')

class Node(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    person_id: int | Any = Field(None, alias='personId', union_mode='left_to_right')

class Edge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    cursor: str | Any = Field(default=None, union_mode='left_to_right')
    node: Node | Any = Field(default=None, union_mode='left_to_right')

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    has_next_page: bool | Any = Field(None, alias='hasNextPage', union_mode='left_to_right')

class Cast(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    edges: list[Edge] | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')

class Edge1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    cursor: str | Any = Field(default=None, union_mode='left_to_right')
    node: Node | Any = Field(default=None, union_mode='left_to_right')

class Creators(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    edges: list[Edge1] | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')

class Edge2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    cursor: str | Any = Field(default=None, union_mode='left_to_right')
    node: Node | Any = Field(default=None, union_mode='left_to_right')

class Directors(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    edges: list[Edge2] | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')

class Edge3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    cursor: str | Any = Field(default=None, union_mode='left_to_right')
    node: Node | Any = Field(default=None, union_mode='left_to_right')

class Writers(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    edges: list[Edge3] | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')

class Node4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    genre_id: int | Any = Field(None, alias='genreId', union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')

class Edge4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    cursor: str | Any = Field(default=None, union_mode='left_to_right')
    node: Node4 | Any = Field(default=None, union_mode='left_to_right')

class GenreTags(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    edges: list[Edge4] | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')

class Reason(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    icon_id: int | Any = Field(None, alias='iconId', union_mode='left_to_right')
    level: str | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')

class ContentAdvisory(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    board_id: int | Any = Field(None, alias='boardId', union_mode='left_to_right')
    board_name: str | Any = Field(None, alias='boardName', union_mode='left_to_right')
    certification_rating_id: int | Any = Field(None, alias='certificationRatingId', union_mode='left_to_right')
    certification_value: str | Any = Field(None, alias='certificationValue', union_mode='left_to_right')
    i18n_reasons_text: str | Any = Field(None, alias='i18nReasonsText', union_mode='left_to_right')
    maturity_description: str | Any = Field(None, alias='maturityDescription', union_mode='left_to_right')
    maturity_level: int | Any = Field(None, alias='maturityLevel', union_mode='left_to_right')
    reasons: list[Reason] | Any = Field(default=None, union_mode='left_to_right')
    video_specific_rating_reason: str | Any = Field(None, alias='videoSpecificRatingReason', union_mode='left_to_right')

class MoodTag(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    display_name: str | Any = Field(None, alias='displayName', union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')
    is_displayable: bool | Any = Field(None, alias='isDisplayable', union_mode='left_to_right')
    is_mood: bool | Any = Field(None, alias='isMood', union_mode='left_to_right')

class ContentWarning(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    message: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    url_substitution_string: str | Any = Field(None, alias='urlSubstitutionString', union_mode='left_to_right')

class ContextualSynopsis(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    evidence_key: str | Any = Field(None, alias='evidenceKey', union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')

class MostLikedMessage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    tagline: str | Any = Field(default=None, union_mode='left_to_right')
    typed_classification: str | Any = Field(None, alias='typedClassification', union_mode='left_to_right')

class TaglineMessage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    cta_message: Any | None = Field(None, alias='ctaMessage')
    tagline: str | Any = Field(default=None, union_mode='left_to_right')
    typed_classification: str | Any = Field(None, alias='typedClassification', union_mode='left_to_right')

class Similar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    video_id: int | Any = Field(None, alias='videoId', union_mode='left_to_right')

class Node5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    video_id: int | Any = Field(None, alias='videoId', union_mode='left_to_right')

class Edge5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    node: Node5 | Any = Field(default=None, union_mode='left_to_right')

class SupplementalVideosList(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    edges: list[Edge5] | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')

class Sibling(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    video_id: int | Any = Field(None, alias='videoId', union_mode='left_to_right')

class TitleGroupMembership(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    kind: str | Any = Field(default=None, union_mode='left_to_right')
    siblings: list[Sibling] | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')

class Boxart(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    available: bool | Any = Field(default=None, union_mode='left_to_right')
    focal_point: Any | None = Field(None, alias='focalPoint')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    key: str | Any = Field(default=None, union_mode='left_to_right')
    status: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')

class BoxartHighRes(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    available: bool | Any = Field(default=None, union_mode='left_to_right')
    focal_point: Any | None = Field(None, alias='focalPoint')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    key: str | Any = Field(default=None, union_mode='left_to_right')
    status: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')

class BrandLogoSmall(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    available: bool | Any = Field(default=None, union_mode='left_to_right')
    focal_point: Any | None = Field(None, alias='focalPoint')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    key: str | Any = Field(default=None, union_mode='left_to_right')
    status: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')

class FocalPoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    x: float | Any = Field(default=None, union_mode='left_to_right')
    y: float | Any = Field(default=None, union_mode='left_to_right')

class StoryArt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    available: bool | Any = Field(default=None, union_mode='left_to_right')
    focal_point: FocalPoint | Any = Field(None, alias='focalPoint', union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    key: str | Any = Field(default=None, union_mode='left_to_right')
    status: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')

class TitleLogoBranded(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    available: bool | Any = Field(default=None, union_mode='left_to_right')
    focal_point: Any | None = Field(None, alias='focalPoint')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    key: str | Any = Field(default=None, union_mode='left_to_right')
    status: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')

class TitleLogoUnbranded(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    available: bool | Any = Field(default=None, union_mode='left_to_right')
    focal_point: Any | None = Field(None, alias='focalPoint')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    key: str | Any = Field(default=None, union_mode='left_to_right')
    status: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')

class Episodes(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    total_count: int | Any = Field(None, alias='totalCount', union_mode='left_to_right')

class ParentSeason(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    episodes: Episodes | Any = Field(default=None, union_mode='left_to_right')
    video_id: int | Any = Field(None, alias='videoId', union_mode='left_to_right')
    hide_episode_numbers: bool | Any = Field(None, alias='hideEpisodeNumbers', union_mode='left_to_right')
    number: int | Any = Field(default=None, union_mode='left_to_right')
    number_label: str | Any = Field(None, alias='numberLabel', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')

class CurrentEpisode(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    parent_season: ParentSeason | Any = Field(None, alias='parentSeason', union_mode='left_to_right')
    video_id: int | Any = Field(None, alias='videoId', union_mode='left_to_right')
    hide_episode_numbers: bool | Any = Field(None, alias='hideEpisodeNumbers', union_mode='left_to_right')
    number: int | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    badges: list[str] | Any = Field(default=None, union_mode='left_to_right')
    watch_status: str | Any = Field(None, alias='watchStatus', union_mode='left_to_right')
    contextual_synopsis: ContextualSynopsis | Any = Field(None, alias='contextualSynopsis', union_mode='left_to_right')
    runtime_sec: int | Any = Field(None, alias='runtimeSec', union_mode='left_to_right')
    bookmark: Any | None = None

class Seasons(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    total_count: int | Any = Field(None, alias='totalCount', union_mode='left_to_right')

class DetailModalModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    video_id: int | Any = Field(None, alias='videoId', union_mode='left_to_right')
    is_available: bool | Any = Field(None, alias='isAvailable', union_mode='left_to_right')
    is_playable: bool | Any = Field(None, alias='isPlayable', union_mode='left_to_right')
    unplayable_causes: Any | None = Field(None, alias='unplayableCauses')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    live_event: Any | None = Field(None, alias='liveEvent')
    broadcast_info: BroadcastInfo | Any = Field(None, alias='broadcastInfo', union_mode='left_to_right')
    copyright: Any | None = None
    cast: Cast | Any = Field(default=None, union_mode='left_to_right')
    creators: Creators | Any = Field(default=None, union_mode='left_to_right')
    directors: Directors | Any = Field(default=None, union_mode='left_to_right')
    writers: Writers | Any = Field(default=None, union_mode='left_to_right')
    genre_tags: GenreTags | Any = Field(None, alias='genreTags', union_mode='left_to_right')
    content_advisory: ContentAdvisory | Any = Field(None, alias='contentAdvisory', union_mode='left_to_right')
    mood_tags: list[MoodTag] | Any = Field(None, alias='moodTags', union_mode='left_to_right')
    content_warning: ContentWarning | Any = Field(None, alias='contentWarning', union_mode='left_to_right')
    unified_entity_id: str | Any = Field(None, alias='unifiedEntityId', union_mode='left_to_right')
    contextual_synopsis: ContextualSynopsis | Any = Field(None, alias='contextualSynopsis', union_mode='left_to_right')
    latest_year: int | Any = Field(None, alias='latestYear', union_mode='left_to_right')
    playback_badges: list[str] | Any = Field(None, alias='playbackBadges', union_mode='left_to_right')
    has_recurring_releases: bool | Any = Field(None, alias='hasRecurringReleases', union_mode='left_to_right')
    is_in_playlist: bool | Any = Field(None, alias='isInPlaylist', union_mode='left_to_right')
    is_in_remind_me_list: bool | Any = Field(None, alias='isInRemindMeList', union_mode='left_to_right')
    is_in_rolling_reminders_list: bool | Any = Field(None, alias='isInRollingRemindersList', union_mode='left_to_right')
    playlist_actions: Any | None = Field(None, alias='playlistActions')
    display_runtime_sec: int | Any = Field(None, alias='displayRuntimeSec', union_mode='left_to_right')
    most_liked_messages: list[MostLikedMessage] | Any = Field(None, alias='mostLikedMessages', union_mode='left_to_right')
    tagline_messages: list[TaglineMessage] | Any = Field(None, alias='taglineMessages', union_mode='left_to_right')
    badges: list[str] | Any = Field(default=None, union_mode='left_to_right')
    watch_status: str | Any = Field(None, alias='watchStatus', union_mode='left_to_right')
    similars: list[Similar] | Any = Field(default=None, union_mode='left_to_right')
    ryan_murphy_collection_ids: list[int] | Any = Field(None, alias='ryanMurphyCollectionIds', union_mode='left_to_right')
    shonda_rhimes_collection_ids: list[int] | Any = Field(None, alias='shondaRhimesCollectionIds', union_mode='left_to_right')
    supplemental_videos_list: SupplementalVideosList | Any = Field(None, alias='supplementalVideosList', union_mode='left_to_right')
    title_group_memberships: list[TitleGroupMembership] | Any = Field(None, alias='titleGroupMemberships', union_mode='left_to_right')
    thumbs_rating: Any | None = Field(None, alias='thumbsRating')
    boxart: Boxart | Any = Field(default=None, union_mode='left_to_right')
    boxart_high_res: BoxartHighRes | Any = Field(None, alias='boxartHighRes', union_mode='left_to_right')
    brand_logo_small: BrandLogoSmall | Any = Field(None, alias='brandLogoSmall', union_mode='left_to_right')
    live_now: Any | None = Field(None, alias='liveNow')
    story_art: StoryArt | Any = Field(None, alias='storyArt', union_mode='left_to_right')
    title_logo_branded: TitleLogoBranded | Any = Field(None, alias='titleLogoBranded', union_mode='left_to_right')
    title_logo_unbranded: TitleLogoUnbranded | Any = Field(None, alias='titleLogoUnbranded', union_mode='left_to_right')
    bookmark: Any | None = None
    tf1_collection_ids: list[Any] | Any = Field(None, alias='tf1CollectionIds', union_mode='left_to_right')
    runtime_sec: int | Any = Field(None, alias='runtimeSec', union_mode='left_to_right')
    thumb_rating: Any | None = Field(None, alias='thumbRating')
    next_live_event: Any | None = Field(None, alias='nextLiveEvent')
    current_episode: CurrentEpisode | Any = Field(None, alias='currentEpisode', union_mode='left_to_right')
    num_seasons_label: str | Any = Field(None, alias='numSeasonsLabel', union_mode='left_to_right')
    seasons: Seasons | Any = Field(default=None, union_mode='left_to_right')
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
