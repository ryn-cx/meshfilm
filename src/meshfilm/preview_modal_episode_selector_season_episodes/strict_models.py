from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, Field

class Extensions(BaseModel):
    error_type: str = Field(..., alias='errorType')
    origin: str

class Error(BaseModel):
    message: str
    path: list[int | str]
    extensions: Extensions

class Artwork(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    height: int
    key: str
    url: str
    width: int

class ContextualSynopsis(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    evidence_key: str = Field(..., alias='evidenceKey')
    text: str

class Node(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    number: int
    video_id: int = Field(..., alias='videoId')
    artwork: Artwork
    availability_date_messaging: None = Field(..., alias='availabilityDateMessaging')
    display_runtime_sec: int = Field(..., alias='displayRuntimeSec')
    is_in_remind_me_list: bool = Field(..., alias='isInRemindMeList')
    title: str
    bookmark: None
    runtime_sec: int = Field(..., alias='runtimeSec')
    live_event: None = Field(..., alias='liveEvent')
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
    field__typename: str = Field(..., alias='__typename')
    cursor: str
    node: Node

class PageInfo(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    end_cursor: str = Field(..., alias='endCursor')
    has_next_page: bool = Field(..., alias='hasNextPage')

class Episodes(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    edges: list[Edge]
    page_info: PageInfo = Field(..., alias='pageInfo')

class CurrentEpisode(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    video_id: int = Field(..., alias='videoId')

class ParentShow(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    current_episode: CurrentEpisode = Field(..., alias='currentEpisode')
    has_recurring_releases: bool = Field(..., alias='hasRecurringReleases')
    video_id: int = Field(..., alias='videoId')
    is_available: bool = Field(..., alias='isAvailable')
    is_playable: bool = Field(..., alias='isPlayable')
    unplayable_causes: None = Field(..., alias='unplayableCauses')

class Video(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    video_id: int = Field(..., alias='videoId')
    episodes: Episodes | None = None
    hide_episode_numbers: bool | None = Field(None, alias='hideEpisodeNumbers')
    number: int | None = None
    parent_show: ParentShow | None = Field(None, alias='parentShow')
    title: str | None = None

class Data(BaseModel):
    videos: list[Video]

class PreviewModalEpisodeSelectorSeasonEpisodesModel(BaseModel):
    errors: list[Error] | None = None
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
