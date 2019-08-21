import pytest
from protocol import validate_request


@pytest.fixture
def invalid_action():
    return 'no_action'


@pytest.fixture
def invalid_time():
    return 'no_time'


@pytest.fixture
def valid_action():
    return 'action'


@pytest.fixture
def valid_time():
    return 'time'


@pytest.fixture
def valid_request(valid_action, valid_time):
    return {
            valid_action: 'something',
            valid_time: 'something_else',
            }


@pytest.fixture
def invalid_request(invalid_action, invalid_time):
    return {
            invalid_action: 'something',
            invalid_time: 'something',
            }


def test_validate_request_valid(valid_request):
    assert validate_request(valid_request)


def test_validate_request_invalid(invalid_request):
    assert not validate_request(invalid_request)
    
