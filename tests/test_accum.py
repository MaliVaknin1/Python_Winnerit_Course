import pytest

from source.accum import Accumulator

def test_accum_creation():
    accum = Accumulator()
    assert accum.count == 0

@pytest.mark.ui
def test_add_counts_twice():
    accum = Accumulator()
    accum.add_counts()
    accum.add_counts()
    assert accum.count == 2