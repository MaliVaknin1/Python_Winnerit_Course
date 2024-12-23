import pytest

from source.accum import Accumulator


@pytest.fixture
def accum():
    return Accumulator()

def test_new_accum(global_accum):
    assert global_accum.count == 0

