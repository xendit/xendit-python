import pytest


@pytest.fixture
def mock_correct_response(mocker, request):
    resp = mocker.Mock()
    resp.status_code = 200
    resp.body = request.param
    return resp


@pytest.fixture
def mock_error_request_response(mocker):
    resp = mocker.Mock()
    resp.status_code = 404
    resp.headers = ""
    resp.body = {"error_code": "error_code", "message": "Wrong message"}
    return resp
