import pytest
from ..model_base_test import ModelBaseTest
from tests.sampleresponse.direct_debit import multi_payment_method_response
from xendit.models import DirectDebit


# fmt: off
class TestCreatePaymentMethod(ModelBaseTest):
    @pytest.fixture
    def default_payment_method_data(self):
        tested_class = DirectDebit
        class_name = "DirectDebit"
        method_name = "get_payment_methods_by_customer_id"
        http_method_name = "get"
        args = ()
        kwargs = {
            "customer_id": "ed20b5db-df04-41fc-8018-8ea4ac4d1030",
        }
        params = (args, kwargs)
        url = f"/payment_methods?customer_id={kwargs['customer_id']}"
        expected_correct_result = multi_payment_method_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data(self, default_payment_method_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_payment_method_data
        headers = {}
        body = {}
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.mark.parametrize("mock_correct_response", [multi_payment_method_response()], indirect=True)
    def test_return_payment_method_on_correct_params(
        self, mocker, mock_correct_response, default_payment_method_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_payment_method_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_payment_method_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_payment_method_data)

    @pytest.mark.parametrize("mock_correct_response", [multi_payment_method_response()], indirect=True)
    def test_return_payment_method_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_payment_method_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_payment_method_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_payment_method_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_payment_method_data)

    @pytest.mark.parametrize("mock_correct_response", [multi_payment_method_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        self.run_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)
# fmt: on
