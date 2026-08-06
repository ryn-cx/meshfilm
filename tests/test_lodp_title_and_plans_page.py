# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parsed_json

if TYPE_CHECKING:
    from meshfilm import Meshfilm
    from meshfilm.lodp_title_and_plans_page import LodpTitleAndPlansPage

VIDEO_IDS = [80095697, 80117711, 81458424, 81726714]


@pytest.fixture(scope="session")
def endpoint(client: Meshfilm) -> LodpTitleAndPlansPage:
    return client.lodp_title_and_plans_page


class TestLodpTitleAndPlansPage:
    def test_alias(self, client: Meshfilm) -> None:
        assert client.title_page is client.lodp_title_and_plans_page

    @pytest.mark.parametrize("video_id", VIDEO_IDS)
    def test_download(self, endpoint: LodpTitleAndPlansPage, video_id: int) -> None:
        download_and_save(
            endpoint,
            str(video_id),
            lambda: endpoint.download(video_id),
        )

    @pytest.mark.parametrize("video_id", VIDEO_IDS)
    def test_parse(self, endpoint: LodpTitleAndPlansPage, video_id: int) -> None:
        parsed_json(endpoint, str(video_id))
        # TODO: assert expected value (needs live data)
