import pytest
from ..model_base_test import ModelBaseTest
from tests.sampleresponse.payment_request import payment_request_response
from xendit.models import PaymentRequest

class TestGetPaymentRequest(ModelBaseTest):
    @pytest.fixture
    def default_payment_method_data(self):
        tested_class = PaymentRequest
        class_name = "PaymentRequest"
        method_name = "confirm"
        http_method_name = "post"
        args = ()
        kwargs = {
            "payment_request_id": "pr-1c229762-c21a-433d-8da5-f02240387e34",
            "auth_code": "00000"
        }
        params = (args, kwargs)
        url = f"/payment_requests/{kwargs['payment_request_id']}/auth"
        expected_correct_result = payment_request_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data(self, default_payment_method_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_payment_method_data
        headers = {}
        body = {
            "auth_code": "00000"
        }
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.mark.parametrize("mock_correct_response", [payment_request_response()], indirect=True)
    def test_return_payment_method_on_correct_params(
        self, mocker, mock_correct_response, default_payment_method_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_payment_method_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_payment_method_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_payment_method_data)

    @pytest.mark.parametrize("mock_correct_response", [payment_request_response()], indirect=True)
    def test_return_payment_method_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_payment_method_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_payment_method_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_payment_method_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_payment_method_data)

    @pytest.mark.parametrize("mock_correct_response", [payment_request_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        self.run_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)