from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import Any
from urllib.parse import quote
from uuid import uuid4

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.exceptions import MeshfilmError
from meshfilm.search_page_query_results.models import (
    SearchPageQueryResultsModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())

PAGE_SIZE = 48
"""How many results the site itself asks for."""


def _variables(
    search_term: str,
    end_cursor: str | None,
    page_size: int,
) -> dict[str, Any]:
    """Return the variables the site sends with a search."""
    return {
        "fetchHighResCards": False,
        "imageParamsForStandardBoxart": {
            "artworkType": "SDP",
            "dimension": {"width": 342, "height": 192},
            "features": {"enableLockBadgeChecks": True, "fallbackStrategy": "STILL"},
        },
        "imageParamsForCloudGameBoxart": {
            "artworkType": "GAME_CLOUD_BOXART_HORIZONTAL_INCOMPATIBLE",
            "dimension": {"width": 342, "height": 192},
            "features": {"fallbackStrategy": "STILL", "topContentTypeBadge": True},
        },
        "imageParamsForMobileGameBoxart": {
            "artworkType": "GAME_ICON_BOXART_HORIZONTAL_CARD",
            "dimension": {"width": 342, "height": 192},
            "features": {"fallbackStrategy": "STILL", "topContentTypeBadge": True},
        },
        "imageParamsForStandardBoxartHighRes": {
            "artworkType": "SDP",
            "dimension": {"width": 665, "height": 375},
            "features": {"fallbackStrategy": "STILL", "enableLockBadgeChecks": True},
        },
        "imageParamsForCloudGameBoxartHighRes": {
            "artworkType": "GAME_CLOUD_BOXART_HORIZONTAL_INCOMPATIBLE",
            "dimension": {"width": 665, "height": 375},
            "features": {"fallbackStrategy": "STILL", "topContentTypeBadge": True},
        },
        "pageSize": page_size,
        "options": {
            "pageCapabilities": {
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
                                                    "base": {
                                                        "canHandleEntityKinds": [
                                                            "MOVIE",
                                                            "SHOW",
                                                            "EPISODE",
                                                            "SEASON",
                                                            "SUPPLEMENTAL",
                                                        ],
                                                    },
                                                },
                                                "pinotStandardCloudAppIcon": {
                                                    "base": {
                                                        "canHandleEntityKinds": [
                                                            "GAME",
                                                        ],
                                                    },
                                                },
                                                "pinotStandardMobileAppIcon": {
                                                    "base": {
                                                        "canHandleEntityKinds": [
                                                            "GAME",
                                                        ],
                                                    },
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
                                                    "base": {
                                                        "canHandleEntityKinds": [
                                                            "MOVIE",
                                                            "SHOW",
                                                            "EPISODE",
                                                            "SEASON",
                                                            "SUPPLEMENTAL",
                                                        ],
                                                    },
                                                },
                                                "pinotStandardCloudAppIcon": {
                                                    "base": {
                                                        "canHandleEntityKinds": [
                                                            "GAME",
                                                        ],
                                                    },
                                                },
                                                "pinotStandardMobileAppIcon": {
                                                    "base": {
                                                        "canHandleEntityKinds": [
                                                            "GAME",
                                                        ],
                                                    },
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
                                                            "MOVIE",
                                                            "SHOW",
                                                            "EPISODE",
                                                            "SEASON",
                                                            "SUPPLEMENTAL",
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
            },
            "session": {"id": str(uuid4())},
        },
        "searchTerm": search_term,
        "endCursor": end_cursor,
    }


# TODO: Validate
def extract_results(response: str) -> dict[str, Any]:
    """Extract the results data from the SearchPageQueryResults response."""
    if results := json.loads(response)["data"]["page"]:
        return results

    msg = "The response has no results page in it"
    raise MeshfilmError(msg)


class SearchPageQueryResults(BaseEndpoint):
    """Contains the results of one search, a page at a time.

    - Example Request:
        - URL: https://www.netflix.com/search?q=gintama

        - Headers:
            - POST /graphql HTTP/2
            - Host: web.prod.cloud.netflix.com
            - User-Agent: __REDACTED__
            - Accept: */*
            - Accept-Language: en-US,en;q=0.9
            - Accept-Encoding: gzip, deflate, br, zstd
            - Referer: https://www.netflix.com/
            - x-netflix.request.id: __REDACTED__
            - content-type: application/json
            - x-netflix.request.toplevel.uuid: __REDACTED__
            - x-netflix.context.ui-flavor: akira
            - x-netflix.request.originating.url:
              https://www.netflix.com/search?q=gintama
            - x-netflix.context.hawkins-version: 5.29.0
            - x-netflix.context.app-version: ve2565e1a
            - x-netflix.context.locales: en-US
            - x-netflix.context.operation-name: SearchPageQueryResults
            - x-netflix.request.attempt: 1
            - x-netflix.request.client.context: {"appstate":"foreground"}
            - Content-Length: 2607
            - Origin: https://www.netflix.com
            - Connection: keep-alive
            - Cookie: __REDACTED__
            - Sec-Fetch-Dest: empty
            - Sec-Fetch-Mode: cors
            - Sec-Fetch-Site: same-site

        - Request:
        {
          "operationName": "SearchPageQueryResults",
          "variables": {
            "fetchHighResCards": false,
            "imageParamsForStandardBoxart": {
              "artworkType": "SDP",
              "dimension": {
                "width": 342,
                "height": 192
              },
              "features": {
                "fallbackStrategy": "STILL",
                "enableLockBadgeChecks": true
              }
            },
            "imageParamsForCloudGameBoxart": {
              "artworkType": "GAME_CLOUD_BOXART_HORIZONTAL_INCOMPATIBLE",
              "dimension": {
                "width": 342,
                "height": 192
              },
              "features": {
                "fallbackStrategy": "STILL",
                "topContentTypeBadge": true
              }
            },
            "imageParamsForMobileGameBoxart": {
              "artworkType": "GAME_ICON_BOXART_HORIZONTAL_CARD",
              "dimension": {
                "width": 342,
                "height": 192
              },
              "features": {
                "fallbackStrategy": "STILL",
                "topContentTypeBadge": true
              }
            },
            "imageParamsForStandardBoxartHighRes": {
              "artworkType": "SDP",
              "dimension": {
                "width": 665,
                "height": 375
              },
              "features": {
                "fallbackStrategy": "STILL",
                "enableLockBadgeChecks": true
              }
            },
            "imageParamsForCloudGameBoxartHighRes": {
              "artworkType": "GAME_CLOUD_BOXART_HORIZONTAL_INCOMPATIBLE",
              "dimension": {
                "width": 665,
                "height": 375
              },
              "features": {
                "fallbackStrategy": "STILL",
                "topContentTypeBadge": true
              }
            },
            "pageSize": 48,
            "options": {
              "pageCapabilities": {
                "base": {
                  "canHandlePlayingCloudGames": false,
                  "capabilitiesBySection": {
                    "pinotGallery": {
                      "base": {
                        "capabilitiesBySectionTreatment": {
                          "pinotCreatorHome": {
                            "base": {
                              "capabilitiesByEntityTreatment": {
                                "pinotStandardBoxshot": {
                                  "base": {
                                    "canHandleEntityKinds": [
                                      "MOVIE",
                                      "SHOW",
                                      "EPISODE",
                                      "SEASON",
                                      "SUPPLEMENTAL"
                                    ]
                                  }
                                },
                                "pinotStandardCloudAppIcon": {
                                  "base": {
                                    "canHandleEntityKinds": [
                                      "GAME"
                                    ]
                                  }
                                },
                                "pinotStandardMobileAppIcon": {
                                  "base": {
                                    "canHandleEntityKinds": [
                                      "GAME"
                                    ]
                                  }
                                },
                                "pinotStandardDestination": {
                                  "base": {
                                    "canHandleEntityKinds": [
                                      "GENERIC_CONTAINER"
                                    ]
                                  }
                                }
                              },
                              "maxTotalEntities": 300
                            }
                          },
                          "pinotStandard": {
                            "base": {
                              "capabilitiesByEntityTreatment": {
                                "pinotStandardBoxshot": {
                                  "base": {
                                    "canHandleEntityKinds": [
                                      "MOVIE",
                                      "SHOW",
                                      "EPISODE",
                                      "SEASON",
                                      "SUPPLEMENTAL"
                                    ]
                                  }
                                },
                                "pinotStandardCloudAppIcon": {
                                  "base": {
                                    "canHandleEntityKinds": [
                                      "GAME"
                                    ]
                                  }
                                },
                                "pinotStandardMobileAppIcon": {
                                  "base": {
                                    "canHandleEntityKinds": [
                                      "GAME"
                                    ]
                                  }
                                },
                                "pinotStandardDestination": {
                                  "base": {
                                    "canHandleEntityKinds": [
                                      "GENERIC_CONTAINER"
                                    ]
                                  }
                                }
                              },
                              "maxTotalEntities": 300
                            }
                          }
                        }
                      }
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
                                      "MOVIE",
                                      "SHOW",
                                      "EPISODE",
                                      "SEASON",
                                      "SUPPLEMENTAL",
                                      "CHARACTER",
                                      "GENERIC_CONTAINER",
                                      "GENRE",
                                      "PERSON"
                                    ]
                                  }
                                }
                              },
                              "maxTotalEntities": 100
                            }
                          }
                        }
                      }
                    }
                  },
                  "maxTotalSections": 2
                },
                "canHandleComplexSectionId": true,
                "canSupportPreLaunchGames": true
              },
              "session": {
                "id": "__REDACTED__"
              }
            },
            "searchTerm": "gintama",
            "endCursor": null
          },
          "extensions": {
            "persistedQuery": {
              "id": "133460a2-c529-40a4-8c78-374acb51e918",
              "version": 102
            }
          }
        }
    """

    def __call__(
        self,
        search_term: str,
        end_cursor: str | None = None,
        page_size: int = PAGE_SIZE,
    ) -> SearchPageQueryResultsModel:
        """Download and parse the SearchPageQueryResults file."""
        log_id = self.get_log_id(self.__call__, locals())
        download_response = self.download(search_term, end_cursor, page_size)
        return self.load(download_response, log_id)

    def download(
        self,
        search_term: str,
        end_cursor: str | None = None,
        page_size: int = PAGE_SIZE,
    ) -> str:
        """Download the SearchPageQueryResults file."""
        log_id = self.get_log_id(self.download, locals())
        payload: dict[str, Any] = {
            "operationName": "SearchPageQueryResults",
            "variables": _variables(search_term, end_cursor, page_size),
            "extensions": {
                "persistedQuery": {
                    "id": "133460a2-c529-40a4-8c78-374acb51e918",
                    "version": 102,
                },
            },
        }
        headers = {
            "x-netflix.request.originating.url": (
                f"https://www.netflix.com/search?q={quote(search_term)}"
            ),
        }
        # No meaningful way to validate the response.
        return self._client.download(payload, log_id, headers)

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> SearchPageQueryResultsModel:
        """Load the results page of a SearchPageQueryResults file into its model."""
        return model_validate_json(extract_results(data), log_id or self.default_log_id)
