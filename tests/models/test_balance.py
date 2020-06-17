import pytest
from xendit import XenditError, Xendit, Balance
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
    xendit = Xendit(api_key="mock_key")
    Balance = xendit.Balance
    mocker.patch.object(APIRequestor, "get")
    APIRequestor.get.return_value = substitute_correct_get
    assert Balance.get(Balance.AccountType.CASH).balance == 1000


def test_raise_xendit_error_on_response_error(mocker, substitute_incorrect_get):
    xendit = Xendit(api_key="mock_key")
    Balance = xendit.Balance
    mocker.patch.object(APIRequestor, "get")
    APIRequestor.get.return_value = substitute_incorrect_get
    with pytest.raises(XenditError):
        print(Balance.get(Balance.AccountType.CASH).balance)


def test_return_balance_on_correct_params_and_global_xendit(
    mocker, substitute_correct_get
):
    mocker.patch.object(APIRequestor, "get")
    APIRequestor.get.return_value = substitute_correct_get
    assert Balance.get(Balance.AccountType.CASH).balance == 1000


def test_raise_xendit_error_on_response_error_and_global_xendit(
    mocker, substitute_incorrect_get
):
    mocker.patch.object(APIRequestor, "get")
    APIRequestor.get.return_value = substitute_incorrect_get
    with pytest.raises(XenditError):
        print(Balance.get(Balance.AccountType.CASH).balance)
