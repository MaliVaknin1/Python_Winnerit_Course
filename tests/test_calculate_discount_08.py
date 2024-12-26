import pytest

from source.calculate_discount_08 import calculate_discount


@pytest.fixture
def basic_price():
    return 100

data=[(20,80), (15, 85), (35,65), (-30,-70)]
@pytest.mark.parametrize("discount_percent,expected,",data)
def test_calculate_discount(basic_price,discount_percent, expected):
    assert expected==calculate_discount(basic_price,discount_percent)