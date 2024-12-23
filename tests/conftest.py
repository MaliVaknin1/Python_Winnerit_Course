import pytest
from source.accum import Accumulator


@pytest.fixture
def sample_data():
    return {"name": "pytest", "version": 7.1}


@pytest.fixture(scope="function")
def global_accum():
    return Accumulator