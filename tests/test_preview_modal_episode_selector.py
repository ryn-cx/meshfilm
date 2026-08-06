# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parsed_json

if TYPE_CHECKING:
    from meshfilm import Meshfilm
    from meshfilm.preview_modal_episode_selector import PreviewModalEpisodeSelector

SHOW_ID = 80095697
"""show_id of Disenchantment."""


@pytest.fixture(scope="session")
def endpoint(client: Meshfilm) -> PreviewModalEpisodeSelector:
    return client.preview_modal_episode_selector


class TestPreviewModalEpisodeSelector:
    def test_alias(self, client: Meshfilm) -> None:
        assert client.seasons is client.preview_modal_episode_selector

    def test_download(self, endpoint: PreviewModalEpisodeSelector) -> None:
        download_and_save(
            endpoint,
            str(SHOW_ID),
            lambda: endpoint.download(SHOW_ID),
        )

    def test_parse(self, endpoint: PreviewModalEpisodeSelector) -> None:
        parsed_json(endpoint, str(SHOW_ID))
        # TODO: assert expected value (needs live data)
