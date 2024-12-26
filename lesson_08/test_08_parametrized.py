import  pytest

def test_multiply_two_positive_ints():
    assert  2*3==6


def test_multiply_zero():
    assert 0 * 100==0

test_data=[(2,3,6), (0,100,0)]

@pytest.mark.parametrize("num_1, num_2 , result", test_data)
def test_sum_parameters(num_1, num_2, result):
    assert  num_1 * num_2 == result

