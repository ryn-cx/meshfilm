# TODO: Validate
"""Contains the SearchPageResults class."""

from __future__ import annotations

import uuid
from typing import Any, override

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.search_page_results.models import SearchPageResultsModel


def _image_params(artwork_type: str, **features: bool) -> dict[str, Any]:
    return {
        "artworkType": artwork_type,
        "dimension": {"width": 342, "height": 192},
        "features": {"fallbackStrategy": "STILL", **features},
    }


_PAGE_CAPABILITIES: dict[str, Any] = {
    "base": {
        "canHandlePlayingCloudGames": False,
        "capabilitiesBySection": {
            "pinotGallery": {
                "base": {
                    "capabilitiesBySectionTreatment": {
                        "pinotCreatorHome": {
                            "base": {
                                "capabilitiesByEntityTreatment": {
                                    "pinotStandardBoxshot": {
                                        "base": {"canHandleEntityKinds": ["VIDEO"]},
                                    },
                                    "pinotStandardCloudAppIcon": {
                                        "base": {"canHandleEntityKinds": ["GAME"]},
                                    },
                                    "pinotStandardMobileAppIcon": {
                                        "base": {"canHandleEntityKinds": ["GAME"]},
                                    },
                                    "pinotStandardDestination": {
                                        "base": {
                                            "canHandleEntityKinds": [
                                                "GENERIC_CONTAINER",
                                            ],
                                        },
                                    },
                                },
                                "maxTotalEntities": 300,
                            },
                        },
                        "pinotStandard": {
                            "base": {
                                "capabilitiesByEntityTreatment": {
                                    "pinotStandardBoxshot": {
                                        "base": {"canHandleEntityKinds": ["VIDEO"]},
                                    },
                                    "pinotStandardCloudAppIcon": {
                                        "base": {"canHandleEntityKinds": ["GAME"]},
                                    },
                                    "pinotStandardMobileAppIcon": {
                                        "base": {"canHandleEntityKinds": ["GAME"]},
                                    },
                                    "pinotStandardDestination": {
                                        "base": {
                                            "canHandleEntityKinds": [
                                                "GENERIC_CONTAINER",
                                            ],
                                        },
                                    },
                                },
                                "maxTotalEntities": 300,
                            },
                        },
                    },
                },
            },
            "pinotList": {
                "base": {
                    "capabilitiesBySectionTreatment": {
                        "pinotSuggestions": {
                            "base": {
                                "capabilitiesByEntityTreatment": {
                                    "pinotSuggestion": {
                                        "base": {
                                            "canHandleEntityKinds": [
                                                "AUTOCOMPLETE",
                                                "VIDEO",
                                                "CHARACTER",
                                                "GENERIC_CONTAINER",
                                                "GENRE",
                                                "PERSON",
                                            ],
                                        },
                                    },
                                },
                                "maxTotalEntities": 100,
                            },
                        },
                    },
                },
            },
        },
        "maxTotalSections": 2,
    },
    "canHandleComplexSectionId": True,
    "canSupportPreLaunchGames": True,
}


class SearchPageResults(BaseEndpoint[SearchPageResultsModel]):
    """Manage the search page results file."""

    _response_model = SearchPageResultsModel

    def _payload(
        self,
        search_term: str,
        end_cursor: str | None,
    ) -> dict[str, Any]:
        return {
            "operationName": "SearchPageQueryResults",
            "variables": {
                "imageParamsForStandardBoxart": _image_params("SDP"),
                "imageParamsForCloudGameBoxart": _image_params(
                    "GAME_CLOUD_BOXART_HORIZONTAL_INCOMPATIBLE",
                    topContentTypeBadge=True,
                ),
                "imageParamsForMobileGameBoxart": _image_params(
                    "GAME_ICON_BOXART_HORIZONTAL_CARD",
                    topContentTypeBadge=True,
                ),
                "pageSize": 48,
                "options": {
                    "pageCapabilities": _PAGE_CAPABILITIES,
                    "session": {"id": str(uuid.uuid4())},
                },
                "searchTerm": search_term,
                "endCursor": end_cursor,
            },
            "extensions": {
                "persistedQuery": {
                    "id": "8d902979-56f2-4886-8c16-f8910f6b52ee",
                    "version": 102,
                },
            },
        }

    def download(
        self,
        search_term: str,
        end_cursor: str | None = None,
    ) -> dict[str, Any]:
        """Downloads the search page results file."""
        return self._client.download(
            self._payload(search_term, end_cursor),
            log_id=f"{self.__class__.__name__} {search_term}",
        )

    @staticmethod
    @override
    def has_content(response: dict[str, Any]) -> bool:
        # Results usually still include recommendations even when nothing
        # matches, so a present page isn't enough -- check for real edges.
        page = response["data"]["page"]
        sections = page["sections"] if page else None
        if not sections:
            return False
        return any(
            section["node"]["entities"]["edges"] for section in sections["edges"]
        )

    def get(
        self,
        search_term: str,
        end_cursor: str | None = None,
    ) -> SearchPageResultsModel:
        """Downloads and parses the search page results file.

        Raises:
            NoContentError: If the response has no meaningful content. The raw
                response is available on the exception's `response` attribute.
        """
        response = self.download(search_term, end_cursor)
        return self._parse_or_raise(
            response,
            f"{self.__class__.__name__} {search_term}",
        )
