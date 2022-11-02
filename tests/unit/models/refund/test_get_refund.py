import pytest
from ..model_base_test import ModelBaseTest
from tests.sampleresponse.refund import refund_response
from xendit.models import Refund

class TestCreateRefund(ModelBaseTest):
    @pytest.fixture
    def default_refund_data(self):
        tested_class = Refund
        class_name = "Refund"
        method_name = "get"
        http_method_name = "get"
        args = ()
        kwargs = {
            "refund_id": "rfd-6f4a377d-a201-437f-9119-f8b00cbbe857"
        }
        params = (args, kwargs)
        url = f"/refunds/{kwargs['refund_id']}"
        expected_correct_result = refund_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data(self, default_refund_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_refund_data
        headers = {}
        body = {}
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.mark.parametrize("mock_correct_response", [refund_response()], indirect=True)
    def test_return_payment_method_on_correct_params(
        self, mocker, mock_correct_response, default_refund_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_refund_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_refund_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_refund_data)

    @pytest.mark.parametrize("mock_correct_response", [refund_response()], indirect=True)
    def test_return_payment_method_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_refund_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_refund_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_refund_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_refund_data)

    @pytest.mark.parametrize("mock_correct_response", [refund_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        self.run_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)