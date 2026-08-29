# TODO: Validate
"""Contains the SearchPageResults class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import Any
from uuid import uuid4

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.exceptions import InvalidFileError
from meshfilm.search_page_results.models import (
    SearchPageResultsModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())

PAGE_SIZE = 48
"""How many results the site itself asks for."""


# TODO: Validate
def _image_params(artwork_type: str, **features: bool) -> dict[str, Any]:
    """Describe the image wanted for one kind of result."""
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
"""What the site tells the API its own page can show, which shapes the answer."""


# TODO: Validate
class SearchPageResults(BaseEndpoint):
    """Manage the search page results file.

    Source: https://www.netflix.com/search?q={search_term}

    Example request:
        - POST /graphql
            - HTTP/2
        - Host: web.prod.cloud.netflix.com
        - User-Agent: __REDACTED__
        - Accept: */*
        - Accept-Language: en-US,en;q=0.9
        - Accept-Encoding: gzip, deflate
        - Content-Type: application/json
        - Origin: https://www.netflix.com
        - Referer: https://www.netflix.com/
        - x-netflix.context.ui-flavor: akira
        - x-netflix.context.app-version: __REDACTED__
        - x-netflix.context.locales: en-us
        - x-netflix.context.operation-name: SearchPageQueryResults
        - x-netflix.request.attempt: 1
        - x-netflix.request.client.context: {"appstate":"foreground"}
        - Body: the persisted query id for SearchPageQueryResults, the search
          term, the page size and the cursor the previous page ended on
    """

    # TODO: Validate
    def __call__(
        self,
        search_term: str,
        end_cursor: str | None = None,
        page_size: int = PAGE_SIZE,
    ) -> SearchPageResultsModel:
        """Run the search and return the model the page is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(search_term, end_cursor, page_size),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        search_term: str,
        end_cursor: str | None = None,
        page_size: int = PAGE_SIZE,
    ) -> str:
        """Download the search page results file."""
        log_id = self.get_log_id(self.download, locals())
        payload: dict[str, Any] = {
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
                "pageSize": page_size,
                "options": {
                    "pageCapabilities": _PAGE_CAPABILITIES,
                    "session": {"id": str(uuid4())},
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
        response = self._client.download(payload, log_id)
        return self._validate_download(response, search_term)

    # TODO: Validate
    def _validate_download(self, response: str, search_term: str) -> str:
        # The response carries no echo of the search term, so only its shape is
        # checked. A term that matches badly is still answered with a full page.
        if json.loads(response)["data"]["page"].get("sections") is None:
            raise InvalidFileError(
                field="search term",
                expected=search_term,
                response=response,
            )
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> SearchPageResultsModel:
        """Read a downloaded search page results file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
