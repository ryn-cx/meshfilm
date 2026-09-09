import pytest
from get_around import GetAround, get_credential

from meshfilm import Meshfilm


@pytest.fixture(scope="session")
def client() -> Meshfilm:
    return Meshfilm(GetAround(proxy=get_credential("PROXY")))
