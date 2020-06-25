import pytest
from ..base_model_test import BaseModelTest
from tests.sampleresponse.balance import balance_response
from xendit.models import Balance, BalanceAccountType


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

    @pytest.fixture
    def api_requestor_request_data(self, default_balance_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_balance_data
        headers = {'for-user-id': 'test-123'}
        body = {}
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

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
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        super().test_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)

# fmt: on
