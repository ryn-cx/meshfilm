from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any

class Artwork(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    key: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')

class Event(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    is_available: bool | Any = Field(None, alias='isAvailable', union_mode='left_to_right')
    video_id: int | Any = Field(None, alias='videoId', union_mode='left_to_right')

class TimeWindow(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    end_time: AwareDatetime | Any = Field(None, alias='endTime', union_mode='left_to_right')

class LiveEvent(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    availability_start_time: AwareDatetime | Any = Field(None, alias='availabilityStartTime', union_mode='left_to_right')
    event: Event | Any = Field(default=None, union_mode='left_to_right')
    time_window: TimeWindow | Any = Field(None, alias='timeWindow', union_mode='left_to_right')

class ContextualSynopsis(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    evidence_key: str | Any = Field(None, alias='evidenceKey', union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')

class Node(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    number: int | Any = Field(default=None, union_mode='left_to_right')
    video_id: int | Any = Field(None, alias='videoId', union_mode='left_to_right')
    artwork: Artwork | Any = Field(default=None, union_mode='left_to_right')
    availability_date_messaging: str | Any = Field(None, alias='availabilityDateMessaging', union_mode='left_to_right')
    display_runtime_sec: int | Any = Field(None, alias='displayRuntimeSec', union_mode='left_to_right')
    is_in_remind_me_list: bool | Any = Field(None, alias='isInRemindMeList', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    bookmark: Any | None = None
    runtime_sec: int | Any = Field(None, alias='runtimeSec', union_mode='left_to_right')
    live_event: LiveEvent | Any = Field(None, alias='liveEvent', union_mode='left_to_right')
    contextual_synopsis: ContextualSynopsis | Any = Field(None, alias='contextualSynopsis', union_mode='left_to_right')
    unified_entity_id: str | Any = Field(None, alias='unifiedEntityId', union_mode='left_to_right')
    is_available: bool | Any = Field(None, alias='isAvailable', union_mode='left_to_right')
    is_playable: bool | Any = Field(None, alias='isPlayable', union_mode='left_to_right')
    unplayable_causes: Any | None = Field(None, alias='unplayableCauses')
    badges: list[str] | Any = Field(default=None, union_mode='left_to_right')
    has_recurring_releases: bool | Any = Field(None, alias='hasRecurringReleases', union_mode='left_to_right')
    is_in_playlist: bool | Any = Field(None, alias='isInPlaylist', union_mode='left_to_right')
    is_in_rolling_reminders_list: bool | Any = Field(None, alias='isInRollingRemindersList', union_mode='left_to_right')
    playlist_actions: Any | None = Field(None, alias='playlistActions')

class Edge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    cursor: str | Any = Field(default=None, union_mode='left_to_right')
    node: Node | Any = Field(default=None, union_mode='left_to_right')

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    end_cursor: str | Any = Field(None, alias='endCursor', union_mode='left_to_right')
    has_next_page: bool | Any = Field(None, alias='hasNextPage', union_mode='left_to_right')

class Episodes(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    edges: list[Edge] | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')

class CurrentEpisode(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    video_id: int | Any = Field(None, alias='videoId', union_mode='left_to_right')

class ParentShow(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    current_episode: CurrentEpisode | Any = Field(None, alias='currentEpisode', union_mode='left_to_right')
    has_recurring_releases: bool | Any = Field(None, alias='hasRecurringReleases', union_mode='left_to_right')
    video_id: int | Any = Field(None, alias='videoId', union_mode='left_to_right')
    is_available: bool | Any = Field(None, alias='isAvailable', union_mode='left_to_right')
    is_playable: bool | Any = Field(None, alias='isPlayable', union_mode='left_to_right')
    unplayable_causes: Any | None = Field(None, alias='unplayableCauses')

class PreviewModalEpisodeSelectorSeasonEpisodesModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    video_id: int | Any = Field(None, alias='videoId', union_mode='left_to_right')
    episodes: Episodes | Any = Field(default=None, union_mode='left_to_right')
    hide_episode_numbers: bool | Any = Field(None, alias='hideEpisodeNumbers', union_mode='left_to_right')
    number: int | Any = Field(default=None, union_mode='left_to_right')
    parent_show: ParentShow | Any = Field(None, alias='parentShow', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
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
