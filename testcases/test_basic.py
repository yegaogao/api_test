import pytest


def test_add():
    assert 1 + 1 == 2


def test_string():
    assert "hello".upper() == "HELLO"


def test_list(sample_list):
    assert len(sample_list) == 3
    assert 2 in sample_list


def test_dict(user_data):
    assert user_data["name"] == "张三"
    assert user_data["age"] == 20


def test_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 2),
        (2, 3, 5),
        (-1, 1, 0),
    ],
)
def test_add_param(a, b, expected):
    assert a + b == expected


def test_string_length():
    s = "hello"
    assert len(s) == 5

def test_sort_list():
    nums = [3, 1, 2]
    result = sorted(nums)
    assert result == [1, 2, 3]

def test_dict_value():
    my_dict = {"name": "李四", "age": 25}
    age = my_dict["age"]
    assert age == 25

def test_value_error():
    "abc"
    with pytest.raises(ValueError):
        int("abc")

@pytest.mark.parametrize(
    "num, expected",
    [
        (1,  "奇数"),
        (2, "偶数"),
    ],
)
def test_odd_even(num, expected):
    result = "奇数" if num % 2 == 1 else "偶数"
    assert result == expected


