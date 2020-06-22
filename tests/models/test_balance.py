import pytest
from xendit import XenditError, Xendit
from xendit.models import Balance, BalanceAccountType
from xendit._api_requestor import _APIRequestor


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
    mocker.patch.object(_APIRequestor, "get")
    _APIRequestor.get.return_value = substitute_correct_get
    assert Balance.get(BalanceAccountType.CASH).balance == 1000


def test_raise_xendit_error_on_response_error(mocker, substitute_incorrect_get):
    xendit = Xendit(api_key="mock_key")
    Balance = xendit.Balance
    mocker.patch.object(_APIRequestor, "get")
    _APIRequestor.get.return_value = substitute_incorrect_get
    with pytest.raises(XenditError):
        print(Balance.get(BalanceAccountType.CASH).balance)


def test_return_balance_on_correct_params_and_global_xendit(
    mocker, substitute_correct_get
):
    mocker.patch.object(_APIRequestor, "get")
    _APIRequestor.get.return_value = substitute_correct_get
    assert Balance.get(BalanceAccountType.CASH).balance == 1000


def test_raise_xendit_error_on_response_error_and_global_xendit(
    mocker, substitute_incorrect_get
):
    mocker.patch.object(_APIRequestor, "get")
    _APIRequestor.get.return_value = substitute_incorrect_get
    with pytest.raises(XenditError):
        print(Balance.get(BalanceAccountType.CASH).balance)
