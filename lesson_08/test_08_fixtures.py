import pytest


@pytest.fixture
def sample_data():
    return {"name": "pytest", "version": 8.9}

def test_sample_data(sample_data):
    assert sample_data["name"]=="pytest"