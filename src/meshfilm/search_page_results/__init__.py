# TODO: Validate
"""Contains the SearchPageResults class."""

from __future__ import annotations

import uuid
from logging import NullHandler, getLogger
from typing import Any

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.search_page_results.models import SearchPageResultsModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


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

    def get_log_id(self, search_term: str, end_cursor: str | None = None) -> str:
        """Build the log id for a download."""
        return self.append_non_default_args(
            f"{self.__class__.__name__} {search_term=}",
            end_cursor=(end_cursor, None),
        )

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
            log_id=self.get_log_id(search_term, end_cursor),
        )

    def download_and_parse(
        self,
        search_term: str,
        end_cursor: str | None = None,
    ) -> SearchPageResultsModel:
        """Downloads and parses the search page results file."""
        return self.parse(self.download(search_term, end_cursor))
