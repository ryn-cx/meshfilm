# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from meshfilm.exceptions import ShowNotFoundError
from meshfilm.preview_modal_episode_selector.models import (
    PreviewModalEpisodeSelectorModel,
)
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from meshfilm import Meshfilm

SHOW_IDS = [
    # https://www.netflix.com/title/80095697
    pytest.param(80095697, id="disenchantment show"),
    # A movie has no seasons, and is answered with itself rather than refused.
    # https://www.netflix.com/title/81458424
    pytest.param(81458424, id="wake up dead man movie"),
]


# TODO: Validate
class PreviewModalEpisodeSelectorTest(RecordedEndpoint):
    MODEL = PreviewModalEpisodeSelectorModel


# TODO: Validate
@pytest.mark.parametrize("show_id", SHOW_IDS)
def test_download(client: Meshfilm, show_id: int) -> None:
    PreviewModalEpisodeSelectorTest.download_test(
        show_id,
        lambda: client.preview_modal_episode_selector.download(show_id),
    )


# TODO: Validate
@pytest.mark.parametrize("show_id", SHOW_IDS)
def test_parse(client: Meshfilm, show_id: int) -> None:
    data = client.preview_modal_episode_selector.load(
        PreviewModalEpisodeSelectorTest.recorded_content(show_id),
    )
    assert data.data.videos[0].video_id == show_id


# TODO: Validate
@pytest.mark.parametrize(
    "show_id",
    [pytest.param(1, id="show that does not exist")],
)
def test_download_invalid(client: Meshfilm, show_id: int) -> None:
    PreviewModalEpisodeSelectorTest.error_test(
        show_id,
        lambda: client.preview_modal_episode_selector.download(show_id),
        ShowNotFoundError,
    )
