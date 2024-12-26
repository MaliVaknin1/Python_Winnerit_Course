import pytest
from source import calculator_08

data= [(2,4,8), (5,7,9), (6,7,13), (0,0,0)]
@pytest.mark.parametrize("x, y, expected", data)
def test_calculator(x , y, expected):
    assert calculator_08.add_sum(x, y) == expected
