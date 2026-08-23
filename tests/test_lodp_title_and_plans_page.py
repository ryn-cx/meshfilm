# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from meshfilm.exceptions import VideoNotFoundError
from meshfilm.lodp_title_and_plans_page.models import LodpTitleAndPlansPageModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from meshfilm import Meshfilm

VIDEO_IDS = [
    # https://www.netflix.com/title/80095697
    pytest.param(80095697, id="disenchantment show"),
    # https://www.netflix.com/title/81458424
    pytest.param(81458424, id="wake up dead man movie"),
]


# TODO: Validate
class LodpTitleAndPlansPageTest(RecordedEndpoint):
    MODEL = LodpTitleAndPlansPageModel


# TODO: Validate
@pytest.mark.parametrize("video_id", VIDEO_IDS)
def test_download(client: Meshfilm, video_id: int) -> None:
    LodpTitleAndPlansPageTest.download_test(
        video_id,
        lambda: client.lodp_title_and_plans_page.download(video_id),
    )


# TODO: Validate
@pytest.mark.parametrize("video_id", VIDEO_IDS)
def test_parse(client: Meshfilm, video_id: int) -> None:
    data = client.lodp_title_and_plans_page.load(
        LodpTitleAndPlansPageTest.recorded_content(video_id),
    )
    assert data.data.videos[0].video_id == video_id


# TODO: Validate
@pytest.mark.parametrize(
    "video_id",
    [pytest.param(1, id="video that does not exist")],
)
def test_download_invalid(client: Meshfilm, video_id: int) -> None:
    LodpTitleAndPlansPageTest.error_test(
        video_id,
        lambda: client.lodp_title_and_plans_page.download(video_id),
        VideoNotFoundError,
    )
