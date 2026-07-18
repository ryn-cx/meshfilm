# TODO: Validate
import pytest
from get_around import build_client_automatically

from meshfilm import Meshfilm


@pytest.fixture(scope="session")
def client() -> Meshfilm:
    return Meshfilm(build_client_automatically())
