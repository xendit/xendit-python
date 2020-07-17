import pytest
from ..model_base_test import ModelBaseTest
from tests.sampleresponse.retail_outlet import retail_outlet_response
from xendit.models import RetailOutlet


# fmt: off
class TestCreateFixedPaymentCode(ModelBaseTest):
    @pytest.fixture
    def default_retail_outlet_data(self):
        tested_class = RetailOutlet
        class_name = "RetailOutlet"
        method_name = "create_fixed_payment_code"
        http_method_name = "post"
        args = ()
        kwargs = {
            "external_id": "demo_fixed_payment_code_123",
            "retail_outlet_name": "ALFAMART",
            "name": "Rika Sutanto",
            "expected_amount": 10000,
            "x_idempotency_key": "test-idemp_123",
        }
        params = (args, kwargs)
        url = "/fixed_payment_code"
        expected_correct_result = retail_outlet_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data(self, default_retail_outlet_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_retail_outlet_data
        headers = {"X-IDEMPOTENCY-KEY": "test-idemp_123"}
        body = {
            "expected_amount": 10000,
            "external_id": "demo_fixed_payment_code_123",
            "name": "Rika Sutanto",
            "retail_outlet_name": "ALFAMART",
        }
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.mark.parametrize("mock_correct_response", [retail_outlet_response()], indirect=True)
    def test_return_retail_outlet_on_correct_params(
        self, mocker, mock_correct_response, default_retail_outlet_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_retail_outlet_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_retail_outlet_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_retail_outlet_data)

    @pytest.mark.parametrize("mock_correct_response", [retail_outlet_response()], indirect=True)
    def test_return_retail_outlet_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_retail_outlet_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_retail_outlet_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_retail_outlet_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_retail_outlet_data)

    @pytest.mark.parametrize("mock_correct_response", [retail_outlet_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        self.run_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)
# fmt: on
