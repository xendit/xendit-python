import pytest
from ..base_model_test import BaseModelTest
from .sample_response import balance_response
from xendit import XenditError
from xendit.models import Balance, BalanceAccountType
from xendit._api_requestor import _APIRequestor


class TestGetBalance(BaseModelTest):
    @pytest.mark.parametrize(
        "mock_correct_response", [balance_response()], indirect=True
    )
    def test_return_balance_on_correct_params(self, mocker, mock_correct_response):
        mocker.patch.object(_APIRequestor, "get")
        _APIRequestor.get.return_value = mock_correct_response
        super().base_test_return_class_on_correct_params(
            tested_method_name="get",
            tested_class_name="Balance",
            params=(BalanceAccountType.CASH,),
            expected_result=balance_response(),
        )

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response
    ):
        mocker.patch.object(_APIRequestor, "get")
        _APIRequestor.get.return_value = mock_error_request_response
        super().base_test_raises_error_on_response_error(
            tested_method_name="get",
            tested_class_name="Balance",
            params=(BalanceAccountType.CASH,),
        )

    @pytest.mark.parametrize(
        "mock_correct_response", [balance_response()], indirect=True
    )
    def test_return_balance_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response
    ):
        mocker.patch.object(_APIRequestor, "get")
        _APIRequestor.get.return_value = mock_correct_response
        balance = Balance.get(BalanceAccountType.CASH)
        assert vars(balance) == balance_response()

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response
    ):
        mocker.patch.object(_APIRequestor, "get")
        _APIRequestor.get.return_value = mock_error_request_response
        with pytest.raises(XenditError):
            balance = Balance.get(BalanceAccountType.CASH)
            print(balance)
