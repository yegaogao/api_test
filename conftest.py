import pytest


@pytest.fixture
def sample_list():
    return [1, 2, 3]


@pytest.fixture
def user_data():
    return {"name": "张三", "age": 20}