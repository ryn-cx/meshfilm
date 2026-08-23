# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from meshfilm.mini_modal.models import MiniModalModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from collections.abc import Sequence

    from meshfilm import Meshfilm

# The endpoint is asked about a batch of titles at a time, and every id in the
# batch is part of the name the response is recorded under.
VIDEO_ID_BATCHES = [
    pytest.param((80095697, 81458424), id="disenchantment and wake up dead man"),
    # An id nothing is under keeps its place in the answer as a null.
    pytest.param((80095697, 1), id="disenchantment and a video that does not exist"),
]


# TODO: Validate
class MiniModalTest(RecordedEndpoint):
    MODEL = MiniModalModel


# TODO: Validate
def recorded_name(video_ids: Sequence[int]) -> str:
    """Return the name the response for a batch of ids is recorded under."""
    return "_".join(str(video_id) for video_id in video_ids)


# TODO: Validate
@pytest.mark.parametrize("video_ids", VIDEO_ID_BATCHES)
def test_download(client: Meshfilm, video_ids: Sequence[int]) -> None:
    MiniModalTest.download_test(
        recorded_name(video_ids),
        lambda: client.mini_modal.download(video_ids),
    )


# TODO: Validate
@pytest.mark.parametrize("video_ids", VIDEO_ID_BATCHES)
def test_parse(client: Meshfilm, video_ids: Sequence[int]) -> None:
    data = client.mini_modal.load(
        MiniModalTest.recorded_content(recorded_name(video_ids)),
    )
    # Every id keeps its place in the answer, whether or not it was found.
    assert len(data.data.unified_entities) == len(video_ids)
