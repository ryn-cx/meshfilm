from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from meshfilm.exceptions import NotATitleError, TitleNotFoundError

if TYPE_CHECKING:
    from meshfilm import Meshfilm

TITLES = [
    pytest.param(80095697, id="Show"),
    pytest.param(81458424, id="Movie"),
    pytest.param(81415953, id="Deleted Show"),
]

NOT_TITLES = [
    pytest.param(81159306, id="Season"),
    pytest.param(81159422, id="Episode"),
]


# TODO: Validate
@pytest.mark.parametrize("title_id", TITLES)
def test_download(client: Meshfilm, title_id: int) -> None:
    detail_modal = client.detail_modal(title_id)
    assert detail_modal.video_id == title_id


def test_download_invalid(client: Meshfilm) -> None:
    with pytest.raises(TitleNotFoundError):
        client.detail_modal.download(1)


# TODO: Validate
@pytest.mark.parametrize("title_id", NOT_TITLES)
def test_download_not_a_title(client: Meshfilm, title_id: int) -> None:
    with pytest.raises(NotATitleError):
        client.detail_modal.download(title_id)
