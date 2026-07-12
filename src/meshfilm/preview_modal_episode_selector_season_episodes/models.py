# TODO: Validate
# ruff: noqa: TC003
from typing import Any
from uuid import UUID

from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict, Field


class Extensions(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    error_type: str = Field(..., alias="errorType")
    origin: str


class Error(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    message: str
    path: list[int | str]
    extensions: Extensions


class Artwork(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    height: int
    key: str
    url: str
    width: int


class ContextualSynopsis(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    evidence_key: str = Field(..., alias="evidenceKey")
    text: str


class Node(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    number: int
    video_id: int = Field(..., alias="videoId")
    artwork: Artwork
    availability_date_messaging: None = Field(..., alias="availabilityDateMessaging")
    display_runtime_sec: int = Field(..., alias="displayRuntimeSec")
    is_in_remind_me_list: bool = Field(..., alias="isInRemindMeList")
    title: str
    bookmark: None
    runtime_sec: int = Field(..., alias="runtimeSec")
    live_event: None = Field(..., alias="liveEvent")
    contextual_synopsis: ContextualSynopsis = Field(..., alias="contextualSynopsis")
    unified_entity_id: str = Field(..., alias="unifiedEntityId")
    is_available: bool = Field(..., alias="isAvailable")
    is_playable: bool = Field(..., alias="isPlayable")
    unplayable_causes: None = Field(..., alias="unplayableCauses")
    badges: list[str]
    has_recurring_releases: bool = Field(..., alias="hasRecurringReleases")
    is_in_playlist: bool = Field(..., alias="isInPlaylist")
    is_in_rolling_reminders_list: bool = Field(..., alias="isInRollingRemindersList")
    playlist_actions: None = Field(..., alias="playlistActions")


class Edge(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    cursor: str
    node: Node


class PageInfo(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    end_cursor: str = Field(..., alias="endCursor")
    has_next_page: bool = Field(..., alias="hasNextPage")


class Episodes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge]
    page_info: PageInfo = Field(..., alias="pageInfo")


class CurrentEpisode(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    video_id: int = Field(..., alias="videoId")


class ParentShow(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    current_episode: CurrentEpisode = Field(..., alias="currentEpisode")
    has_recurring_releases: bool = Field(..., alias="hasRecurringReleases")
    video_id: int = Field(..., alias="videoId")
    is_available: bool = Field(..., alias="isAvailable")
    is_playable: bool = Field(..., alias="isPlayable")
    unplayable_causes: None = Field(..., alias="unplayableCauses")


class Video(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    video_id: int = Field(..., alias="videoId")
    episodes: Episodes
    hide_episode_numbers: bool = Field(..., alias="hideEpisodeNumbers")
    number: int
    parent_show: ParentShow = Field(..., alias="parentShow")
    title: str


class Data(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    videos: list[Video]


class Headers(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    user_agent: str = Field(..., alias="User-Agent")
    accept: str = Field(..., alias="Accept")
    accept_language: str = Field(..., alias="Accept-Language")
    accept_encoding: str = Field(..., alias="Accept-Encoding")
    content_type: str = Field(..., alias="Content-Type")
    origin: str = Field(..., alias="Origin")
    referer: str = Field(..., alias="Referer")
    x_netflix_context_ui_flavor: str = Field(..., alias="x-netflix.context.ui-flavor")
    x_netflix_context_app_version: str = Field(
        ...,
        alias="x-netflix.context.app-version",
    )
    x_netflix_context_locales: str = Field(..., alias="x-netflix.context.locales")
    x_netflix_context_operation_name: str = Field(
        ...,
        alias="x-netflix.context.operation-name",
    )
    x_netflix_request_attempt: str = Field(..., alias="x-netflix.request.attempt")
    x_netflix_request_client_context: str = Field(
        ...,
        alias="x-netflix.request.client.context",
    )


class Variables(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    season_id: int = Field(..., alias="seasonId")
    count: int
    opaque_image_format: str = Field(..., alias="opaqueImageFormat")
    artwork_context: dict[str, Any] = Field(..., alias="artworkContext")


class PersistedQuery(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: UUID
    version: int


class Extensions1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    persisted_query: PersistedQuery = Field(..., alias="persistedQuery")


class Body(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    operation_name: str = Field(..., alias="operationName")
    variables: Variables
    extensions: Extensions1


class Meshfilm(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    headers: Headers
    body: Body


class PreviewModalEpisodeSelectorSeasonEpisodesModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    errors: list[Error]
    data: Data
    meshfilm: Meshfilm | None = None
