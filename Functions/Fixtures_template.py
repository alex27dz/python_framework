import pytest


@pytest.fixture
def fixture_func_hi():
    return 'hi'


@pytest.fixture
def fixture_func_bye():
    return 'bye'


# def test_somthing(fixture_func_hi, fixture_func_bye):
    # assert fixture_func_hi == 'hi', 'Was expected to get hi'
    # assert fixture_func_bye == 'hello', 'Was expected to get bye'



