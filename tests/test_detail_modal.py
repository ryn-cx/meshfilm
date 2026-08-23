# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from meshfilm.detail_modal.models import DetailModalModel
from meshfilm.exceptions import VideoNotFoundError
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from meshfilm import Meshfilm

VIDEO_IDS = [
    # https://www.netflix.com/title/80095697
    pytest.param(80095697, id="disenchantment show"),
    # https://www.netflix.com/title/80117711
    pytest.param(80117711, id="disenchantment first episode"),
    # https://www.netflix.com/title/81458424
    pytest.param(81458424, id="wake up dead man movie"),
]


# TODO: Validate
class DetailModalTest(RecordedEndpoint):
    MODEL = DetailModalModel


# TODO: Validate
@pytest.mark.parametrize("video_id", VIDEO_IDS)
def test_download(client: Meshfilm, video_id: int) -> None:
    DetailModalTest.download_test(
        video_id,
        lambda: client.detail_modal.download(video_id),
    )


# TODO: Validate
@pytest.mark.parametrize("video_id", VIDEO_IDS)
def test_parse(client: Meshfilm, video_id: int) -> None:
    data = client.detail_modal.load(DetailModalTest.recorded_content(video_id))
    assert data.data.unified_entities[0].video_id == video_id


# TODO: Validate
@pytest.mark.parametrize(
    "video_id",
    [pytest.param(1, id="video that does not exist")],
)
def test_download_invalid(client: Meshfilm, video_id: int) -> None:
    DetailModalTest.error_test(
        video_id,
        lambda: client.detail_modal.download(video_id),
        VideoNotFoundError,
    )
