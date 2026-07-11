# ruff: noqa: TC003
from uuid import UUID

from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict, Field


class Episodes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    total_count: int = Field(..., alias="totalCount")


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
    video_specific_rating_reason: None = Field(..., alias="videoSpecificRatingReason")


class Node(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    episodes: Episodes
    hidden_episode_numbers: bool = Field(..., alias="hiddenEpisodeNumbers")
    title: str
    video_id: int = Field(..., alias="videoId")
    content_advisory: ContentAdvisory = Field(..., alias="contentAdvisory")


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
    start_cursor: str = Field(..., alias="startCursor")


class Seasons(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge]
    page_info: PageInfo = Field(..., alias="pageInfo")


class Video(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    video_id: int = Field(..., alias="videoId")
    seasons: Seasons


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
    show_id: int = Field(..., alias="showId")
    season_count: int = Field(..., alias="seasonCount")


class PersistedQuery(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: UUID
    version: int


class Extensions(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    persisted_query: PersistedQuery = Field(..., alias="persistedQuery")


class Body(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    operation_name: str = Field(..., alias="operationName")
    variables: Variables
    extensions: Extensions


class Meshfilm(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    headers: Headers
    body: Body


class PreviewModalEpisodeSelectorModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    data: Data
    meshfilm: Meshfilm
