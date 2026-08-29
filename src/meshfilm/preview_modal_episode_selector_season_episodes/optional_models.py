from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from typing import Any

class Extensions(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    error_type: str | None = Field(None, alias='errorType')
    origin: str | None = None

class Error(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    message: str | None = None
    path: list[int | str] | None = None
    extensions: Extensions | None = None

class Artwork(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    height: int | None = None
    key: str | None = None
    url: str | None = None
    width: int | None = None

class ContextualSynopsis(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    evidence_key: str | None = Field(None, alias='evidenceKey')
    text: str | None = None

class Node(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    number: int | None = None
    video_id: int | None = Field(None, alias='videoId')
    artwork: Artwork | None = None
    availability_date_messaging: Any | None = Field(None, alias='availabilityDateMessaging')
    display_runtime_sec: int | None = Field(None, alias='displayRuntimeSec')
    is_in_remind_me_list: bool | None = Field(None, alias='isInRemindMeList')
    title: str | None = None
    bookmark: Any | None = None
    runtime_sec: int | None = Field(None, alias='runtimeSec')
    live_event: Any | None = Field(None, alias='liveEvent')
    contextual_synopsis: ContextualSynopsis | None = Field(None, alias='contextualSynopsis')
    unified_entity_id: str | None = Field(None, alias='unifiedEntityId')
    is_available: bool | None = Field(None, alias='isAvailable')
    is_playable: bool | None = Field(None, alias='isPlayable')
    unplayable_causes: Any | None = Field(None, alias='unplayableCauses')
    badges: list[str] | None = None
    has_recurring_releases: bool | None = Field(None, alias='hasRecurringReleases')
    is_in_playlist: bool | None = Field(None, alias='isInPlaylist')
    is_in_rolling_reminders_list: bool | None = Field(None, alias='isInRollingRemindersList')
    playlist_actions: Any | None = Field(None, alias='playlistActions')

class Edge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    cursor: str | None = None
    node: Node | None = None

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    end_cursor: str | None = Field(None, alias='endCursor')
    has_next_page: bool | None = Field(None, alias='hasNextPage')

class Episodes(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    edges: list[Edge] | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')

class CurrentEpisode(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    video_id: int | None = Field(None, alias='videoId')

class ParentShow(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    current_episode: CurrentEpisode | None = Field(None, alias='currentEpisode')
    has_recurring_releases: bool | None = Field(None, alias='hasRecurringReleases')
    video_id: int | None = Field(None, alias='videoId')
    is_available: bool | None = Field(None, alias='isAvailable')
    is_playable: bool | None = Field(None, alias='isPlayable')
    unplayable_causes: Any | None = Field(None, alias='unplayableCauses')

class Video(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    video_id: int | None = Field(None, alias='videoId')
    episodes: Episodes | None = None
    hide_episode_numbers: bool | None = Field(None, alias='hideEpisodeNumbers')
    number: int | None = None
    parent_show: ParentShow | None = Field(None, alias='parentShow')
    title: str | None = None

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    videos: list[Video] | None = None

class PreviewModalEpisodeSelectorSeasonEpisodesModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
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
