import pytest
from ..base_model_test import BaseModelTest
from .sample_response import virtual_account_payment_response
from xendit.models import VirtualAccount


# fmt: off
class TestGetVirtualAccountPayment(BaseModelTest):
    @pytest.fixture
    def default_virtual_account_data(self):
        tested_class = VirtualAccount
        class_name = "VirtualAccount"
        method_name = "get_payment"
        http_method_name = "get"
        params = ("1502450097080",)
        expected_correct_result = virtual_account_payment_response()
        return (tested_class, class_name, method_name, http_method_name, params, expected_correct_result)

    @pytest.mark.parametrize("mock_correct_response", [virtual_account_payment_response()], indirect=True)
    def test_return_virtual_account_on_correct_params(
        self, mocker, mock_correct_response, default_virtual_account_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_virtual_account_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_virtual_account_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_virtual_account_data)

    @pytest.mark.parametrize("mock_correct_response", [virtual_account_payment_response()], indirect=True)
    def test_return_virtual_account_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_virtual_account_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_virtual_account_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_virtual_account_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_virtual_account_data)
# fmt: on
