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


class Boxart(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    available: bool
    focal_point: None = Field(..., alias="focalPoint")
    height: int
    key: str
    status: str
    url: str
    width: int


class ContextualSynopsis(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    evidence_key: str = Field(..., alias="evidenceKey")
    text: str


class Reason(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    icon_id: int = Field(..., alias="iconId")
    level: str
    text: str


class ContentAdvisory(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    board_id: int = Field(..., alias="boardId")
    board_name: str = Field(..., alias="boardName")
    certification_rating_id: int = Field(..., alias="certificationRatingId")
    certification_value: str = Field(..., alias="certificationValue")
    i18n_reasons_text: str = Field(..., alias="i18nReasonsText")
    maturity_description: str = Field(..., alias="maturityDescription")
    maturity_level: int = Field(..., alias="maturityLevel")
    reasons: list[Reason]
    video_specific_rating_reason: str | None = Field(
        ...,
        alias="videoSpecificRatingReason",
    )


class Episodes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    total_count: int = Field(..., alias="totalCount")


class ParentSeason(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    episodes: Episodes
    video_id: int = Field(..., alias="videoId")


class CurrentEpisode(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    parent_season: ParentSeason = Field(..., alias="parentSeason")
    video_id: int = Field(..., alias="videoId")


class Seasons(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    total_count: int = Field(..., alias="totalCount")


class ParentShow(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    current_episode: CurrentEpisode = Field(..., alias="currentEpisode")
    num_seasons_label: str = Field(..., alias="numSeasonsLabel")
    seasons: Seasons
    video_id: int = Field(..., alias="videoId")


class ParentSeason1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    episodes: Episodes
    video_id: int = Field(..., alias="videoId")


class CurrentEpisode1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    parent_season: ParentSeason1 = Field(..., alias="parentSeason")
    video_id: int = Field(..., alias="videoId")


class Video(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    video_id: int = Field(..., alias="videoId")
    boxart: Boxart
    title: str
    unified_entity_id: str = Field(..., alias="unifiedEntityId")
    contextual_synopsis: ContextualSynopsis = Field(..., alias="contextualSynopsis")
    is_available: bool = Field(..., alias="isAvailable")
    is_playable: bool = Field(..., alias="isPlayable")
    unplayable_causes: None = Field(..., alias="unplayableCauses")
    bookmark: None = Field(None)
    latest_year: int = Field(..., alias="latestYear")
    content_advisory: ContentAdvisory = Field(..., alias="contentAdvisory")
    playback_badges: list[str] = Field(..., alias="playbackBadges")
    has_recurring_releases: bool = Field(..., alias="hasRecurringReleases")
    is_in_playlist: bool = Field(..., alias="isInPlaylist")
    is_in_remind_me_list: bool = Field(..., alias="isInRemindMeList")
    is_in_rolling_reminders_list: bool = Field(..., alias="isInRollingRemindersList")
    playlist_actions: None = Field(..., alias="playlistActions")
    display_runtime_sec: int | None = Field(None, alias="displayRuntimeSec")
    parent_show: ParentShow | None = Field(None, alias="parentShow")
    live_image_timeline: None = Field(None, alias="liveImageTimeline")
    current_episode: CurrentEpisode1 | None = Field(None, alias="currentEpisode")
    num_seasons_label: str | None = Field(None, alias="numSeasonsLabel")
    seasons: Seasons | None = None


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
    artwork_context: dict[str, Any] = Field(..., alias="artworkContext")
    video_ids: list[int] = Field(..., alias="videoIds")


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


class PreviewModalVideoTitleGroupModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    errors: list[Error]
    data: Data
    meshfilm: Meshfilm | None = None
