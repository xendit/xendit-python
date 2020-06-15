import pytest
from xendit import Balance, XenditError
from xendit.api_requestor import APIRequestor


@pytest.fixture
def substitute_correct_get(mocker):
    resp = mocker.Mock()
    resp.status_code = 200
    resp.body = {"balance": 1000}
    return resp


@pytest.fixture
def substitute_incorrect_get(mocker):
    resp = mocker.Mock()
    resp.status_code = 404
    resp.headers = ""
    resp.body = {"error_code": "error_code", "message": "Wrong message"}
    return resp


def test_return_balance_on_correct_params(mocker, substitute_correct_get):
    mocker.patch.object(APIRequestor, "get")
    APIRequestor.get.return_value = substitute_correct_get
    assert Balance.get("CASH").balance == 1000


def test_raise_error_on_wrong_params(mocker, substitute_incorrect_get):
    mocker.patch.object(APIRequestor, "get")
    APIRequestor.get.return_value = substitute_incorrect_get
    with pytest.raises(XenditError):
        print(Balance.get("money").balance)
