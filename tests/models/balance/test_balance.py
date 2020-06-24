import pytest
from ..base_model_test import BaseModelTest
from .sample_response import balance_response
from xendit.models import Balance, BalanceAccountType
from xendit._api_requestor import _APIRequestor


# fmt: off
class TestGetBalance(BaseModelTest):
    @pytest.fixture
    def default_balance_data(self):
        tested_class = Balance
        class_name = "Balance"
        method_name = "get"
        http_method_name = "get"
        args = (BalanceAccountType.CASH,)
        kwargs = {'for_user_id': 'test-123'}
        params = (args, kwargs)
        url = f"/balance?account_type={args[0].name}"
        expected_correct_result = balance_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.mark.parametrize("mock_correct_response", [balance_response()], indirect=True)
    def test_return_balance_on_correct_params(
        self, mocker, mock_correct_response, default_balance_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_balance_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_balance_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_balance_data)

    @pytest.mark.parametrize("mock_correct_response", [balance_response()], indirect=True)
    def test_return_balance_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_balance_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_balance_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_balance_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_balance_data)

    @pytest.mark.parametrize("mock_correct_response", [balance_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, default_balance_data):
        """It should send correct request to API Requestor

        Args:
            mocker (fixture): Default mocker fixture
            mock_correct_response (function): Mock correct response that sent by APIRequestor
            default_tested_class_data (tuple): Tuple with 7 item that contain:
            - tested_class (class): Class that will be tested
            - class_name (str): String representation for the class
            - method_name (str): Method name that will be tested
            - http_method_name (str): HTTP Method name that will be used in the API Requestor
            - url (str): URL for the request
            - params (tuple): Params with format (args, kwargs)
            - expected_correct_result (dict): Expected Correct Result
        """
        _, _, _, http_method_name, url, params, expected_correct_result = default_balance_data
        args, kwargs = params

        mocker.patch.object(_APIRequestor, http_method_name)
        tested_method = getattr(_APIRequestor, http_method_name)
        setattr(tested_method, "return_value", mock_correct_response)

        Balance.get(*args, **kwargs)
        tested_method.assert_called_with(url, headers={})
# fmt: on
