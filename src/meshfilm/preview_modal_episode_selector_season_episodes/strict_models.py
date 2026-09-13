from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import AwareDatetime, BaseModel, Field

class Artwork(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    height: int
    key: str
    url: str
    width: int

class Event(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    is_available: bool = Field(..., alias='isAvailable')
    video_id: int = Field(..., alias='videoId')

class TimeWindow(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    end_time: AwareDatetime = Field(..., alias='endTime')

class LiveEvent(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    availability_start_time: AwareDatetime = Field(..., alias='availabilityStartTime')
    event: Event
    time_window: TimeWindow = Field(..., alias='timeWindow')

class ContextualSynopsis(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    evidence_key: str = Field(..., alias='evidenceKey')
    text: str

class Node(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    number: int
    video_id: int = Field(..., alias='videoId')
    artwork: Artwork
    availability_date_messaging: str | None = Field(..., alias='availabilityDateMessaging')
    display_runtime_sec: int = Field(..., alias='displayRuntimeSec')
    is_in_remind_me_list: bool = Field(..., alias='isInRemindMeList')
    title: str
    bookmark: None
    runtime_sec: int = Field(..., alias='runtimeSec')
    live_event: LiveEvent | None = Field(..., alias='liveEvent')
    contextual_synopsis: ContextualSynopsis = Field(..., alias='contextualSynopsis')
    unified_entity_id: str = Field(..., alias='unifiedEntityId')
    is_available: bool = Field(..., alias='isAvailable')
    is_playable: bool = Field(..., alias='isPlayable')
    unplayable_causes: None = Field(..., alias='unplayableCauses')
    badges: list[str]
    has_recurring_releases: bool = Field(..., alias='hasRecurringReleases')
    is_in_playlist: bool = Field(..., alias='isInPlaylist')
    is_in_rolling_reminders_list: bool = Field(..., alias='isInRollingRemindersList')
    playlist_actions: None = Field(..., alias='playlistActions')

class Edge(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    cursor: str
    node: Node

class PageInfo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    end_cursor: str = Field(..., alias='endCursor')
    has_next_page: bool = Field(..., alias='hasNextPage')

class Episodes(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    edges: list[Edge]
    page_info: PageInfo = Field(..., alias='pageInfo')

class CurrentEpisode(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    video_id: int = Field(..., alias='videoId')

class ParentShow(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    current_episode: CurrentEpisode = Field(..., alias='currentEpisode')
    has_recurring_releases: bool = Field(..., alias='hasRecurringReleases')
    video_id: int = Field(..., alias='videoId')
    is_available: bool = Field(..., alias='isAvailable')
    is_playable: bool = Field(..., alias='isPlayable')
    unplayable_causes: None = Field(..., alias='unplayableCauses')

class PreviewModalEpisodeSelectorSeasonEpisodesModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    video_id: int = Field(..., alias='videoId')
    episodes: Episodes
    hide_episode_numbers: bool = Field(..., alias='hideEpisodeNumbers')
    number: int
    parent_show: ParentShow = Field(..., alias='parentShow')
    title: str
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
