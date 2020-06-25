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
        args = ("5ef18efca7d10d1b4d61fb52",)
        kwargs = {}
        params = (args, kwargs)
        url = f"/callback_virtual_account_payments/payment_id={args[0]}"
        expected_correct_result = virtual_account_payment_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data(self, default_virtual_account_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_virtual_account_data
        headers = {}
        body = {}
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

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

    @pytest.mark.parametrize("mock_correct_response", [virtual_account_payment_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        super().test_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)
# fmt: on
