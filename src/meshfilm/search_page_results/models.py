# TODO: Validate
# ruff: noqa: TC003
from uuid import UUID

from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict, Field


class ContentAdvisory(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    maturity_level: int = Field(..., alias="maturityLevel")


class UnifiedEntity(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    unified_entity_id: str = Field(..., alias="unifiedEntityId")
    content_advisory: ContentAdvisory = Field(..., alias="contentAdvisory")
    video_id: int = Field(..., alias="videoId")


class Artwork(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    height: int
    key: str
    url: str
    width: int


class ContextualArtwork(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    field_id: str = Field(..., alias="_id")
    artwork: Artwork
    image_congruence_context: None = Field(..., alias="imageCongruenceContext")


class Node1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    display_string: str = Field(..., alias="displayString")
    unified_entity: UnifiedEntity = Field(..., alias="unifiedEntity")
    contextual_artwork: ContextualArtwork = Field(..., alias="contextualArtwork")


class Edge1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    node: Node1


class PageInfo(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    end_cursor: str = Field(..., alias="endCursor")
    has_next_page: bool = Field(..., alias="hasNextPage")


class Entities(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge1]
    page_info: PageInfo = Field(..., alias="pageInfo")
    total_count: int = Field(..., alias="totalCount")


class LoggingData(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    section_logging_id: str = Field(..., alias="sectionLoggingId")
    track_id: int = Field(..., alias="trackId")


class SectionTreatment(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")


class Node(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    display_string: str = Field(..., alias="displayString")
    entities: Entities
    id: str
    logging_data: LoggingData = Field(..., alias="loggingData")
    section_treatment: SectionTreatment = Field(..., alias="sectionTreatment")


class Edge(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    node: Node


class Sections(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    edges: list[Edge]
    total_count: int = Field(..., alias="totalCount")


class TrackingInfo(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    request_id: str = Field(..., alias="requestId")


class Page(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    field_id: str = Field(..., alias="_id")
    display_string: None = Field(..., alias="displayString")
    expires: str
    sections: Sections
    tracking_info: TrackingInfo = Field(..., alias="trackingInfo")


class Data(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    page: Page


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


class Dimension(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    width: int
    height: int


class Features(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    fallback_strategy: str = Field(..., alias="fallbackStrategy")


class ImageParamsForStandardBoxart(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    artwork_type: str = Field(..., alias="artworkType")
    dimension: Dimension
    features: Features


class Features1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    fallback_strategy: str = Field(..., alias="fallbackStrategy")
    top_content_type_badge: bool = Field(..., alias="topContentTypeBadge")


class ImageParamsForCloudGameBoxart(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    artwork_type: str = Field(..., alias="artworkType")
    dimension: Dimension
    features: Features1


class ImageParamsForMobileGameBoxart(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    artwork_type: str = Field(..., alias="artworkType")
    dimension: Dimension
    features: Features1


class Base3(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    can_handle_entity_kinds: list[str] = Field(..., alias="canHandleEntityKinds")


class PinotStandardBoxshot(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    base: Base3


class PinotStandardCloudAppIcon(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    base: Base3


class PinotStandardMobileAppIcon(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    base: Base3


class PinotStandardDestination(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    base: Base3


class CapabilitiesByEntityTreatment(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    pinot_standard_boxshot: PinotStandardBoxshot = Field(
        ...,
        alias="pinotStandardBoxshot",
    )
    pinot_standard_cloud_app_icon: PinotStandardCloudAppIcon = Field(
        ...,
        alias="pinotStandardCloudAppIcon",
    )
    pinot_standard_mobile_app_icon: PinotStandardMobileAppIcon = Field(
        ...,
        alias="pinotStandardMobileAppIcon",
    )
    pinot_standard_destination: PinotStandardDestination = Field(
        ...,
        alias="pinotStandardDestination",
    )


class Base2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    capabilities_by_entity_treatment: CapabilitiesByEntityTreatment = Field(
        ...,
        alias="capabilitiesByEntityTreatment",
    )
    max_total_entities: int = Field(..., alias="maxTotalEntities")


class PinotCreatorHome(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    base: Base2


class Base8(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    can_handle_entity_kinds: list[str] = Field(..., alias="canHandleEntityKinds")


class PinotStandardBoxshot1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    base: Base8


class PinotStandardCloudAppIcon1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    base: Base8


class PinotStandardMobileAppIcon1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    base: Base8


class PinotStandardDestination1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    base: Base8


class CapabilitiesByEntityTreatment1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    pinot_standard_boxshot: PinotStandardBoxshot1 = Field(
        ...,
        alias="pinotStandardBoxshot",
    )
    pinot_standard_cloud_app_icon: PinotStandardCloudAppIcon1 = Field(
        ...,
        alias="pinotStandardCloudAppIcon",
    )
    pinot_standard_mobile_app_icon: PinotStandardMobileAppIcon1 = Field(
        ...,
        alias="pinotStandardMobileAppIcon",
    )
    pinot_standard_destination: PinotStandardDestination1 = Field(
        ...,
        alias="pinotStandardDestination",
    )


class Base7(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    capabilities_by_entity_treatment: CapabilitiesByEntityTreatment1 = Field(
        ...,
        alias="capabilitiesByEntityTreatment",
    )
    max_total_entities: int = Field(..., alias="maxTotalEntities")


class PinotStandard(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    base: Base7


class CapabilitiesBySectionTreatment(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    pinot_creator_home: PinotCreatorHome = Field(..., alias="pinotCreatorHome")
    pinot_standard: PinotStandard = Field(..., alias="pinotStandard")


class Base1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    capabilities_by_section_treatment: CapabilitiesBySectionTreatment = Field(
        ...,
        alias="capabilitiesBySectionTreatment",
    )


class PinotGallery(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    base: Base1


class Base14(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    can_handle_entity_kinds: list[str] = Field(..., alias="canHandleEntityKinds")


class PinotSuggestion(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    base: Base14


class CapabilitiesByEntityTreatment2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    pinot_suggestion: PinotSuggestion = Field(..., alias="pinotSuggestion")


class Base13(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    capabilities_by_entity_treatment: CapabilitiesByEntityTreatment2 = Field(
        ...,
        alias="capabilitiesByEntityTreatment",
    )
    max_total_entities: int = Field(..., alias="maxTotalEntities")


class PinotSuggestions(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    base: Base13


class CapabilitiesBySectionTreatment1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    pinot_suggestions: PinotSuggestions = Field(..., alias="pinotSuggestions")


class Base12(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    capabilities_by_section_treatment: CapabilitiesBySectionTreatment1 = Field(
        ...,
        alias="capabilitiesBySectionTreatment",
    )


class PinotList(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    base: Base12


class CapabilitiesBySection(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    pinot_gallery: PinotGallery = Field(..., alias="pinotGallery")
    pinot_list: PinotList = Field(..., alias="pinotList")


class Base(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    can_handle_playing_cloud_games: bool = Field(
        ...,
        alias="canHandlePlayingCloudGames",
    )
    capabilities_by_section: CapabilitiesBySection = Field(
        ...,
        alias="capabilitiesBySection",
    )
    max_total_sections: int = Field(..., alias="maxTotalSections")


class PageCapabilities(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    base: Base
    can_handle_complex_section_id: bool = Field(..., alias="canHandleComplexSectionId")
    can_support_pre_launch_games: bool = Field(..., alias="canSupportPreLaunchGames")


class Session(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: UUID


class Options(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    page_capabilities: PageCapabilities = Field(..., alias="pageCapabilities")
    session: Session


class Variables(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    image_params_for_standard_boxart: ImageParamsForStandardBoxart = Field(
        ...,
        alias="imageParamsForStandardBoxart",
    )
    image_params_for_cloud_game_boxart: ImageParamsForCloudGameBoxart = Field(
        ...,
        alias="imageParamsForCloudGameBoxart",
    )
    image_params_for_mobile_game_boxart: ImageParamsForMobileGameBoxart = Field(
        ...,
        alias="imageParamsForMobileGameBoxart",
    )
    page_size: int = Field(..., alias="pageSize")
    options: Options
    search_term: str = Field(..., alias="searchTerm")
    end_cursor: None = Field(..., alias="endCursor")


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


class SearchPageResultsModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    data: Data
    meshfilm: Meshfilm | None = None
