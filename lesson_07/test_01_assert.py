import pytest


def test_one_plus_one():
    assert 1+1 ==2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as  e:
        num =2 / 0
    assert 'division by zero' in str(e.value)
