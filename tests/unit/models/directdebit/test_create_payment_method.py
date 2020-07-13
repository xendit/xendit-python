import pytest
from ..model_base_test import ModelBaseTest
from tests.sampleresponse.direct_debit import payment_method_response
from xendit.models import DirectDebit, DirectDebitPaymentMethodType


# fmt: off
class TestCreatePaymentMethod(ModelBaseTest):
    @pytest.fixture
    def default_payment_method_data(self):
        tested_class = DirectDebit
        class_name = "DirectDebit"
        method_name = "create_payment_method"
        http_method_name = "post"
        args = ()
        kwargs = {
            "customer_id": "ed20b5db-df04-41fc-8018-8ea4ac4d1030",
            "type": DirectDebitPaymentMethodType.DEBIT_CARD,
            "properties": {
                'id': 'la-fac7e744-ab40-4100-a447-cbbb16f29ded'
            },
        }
        params = (args, kwargs)
        url = "/payment_methods"
        expected_correct_result = payment_method_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data(self, default_payment_method_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_payment_method_data
        headers = {}
        body = {
            "customer_id": "ed20b5db-df04-41fc-8018-8ea4ac4d1030",
            "type": "DEBIT_CARD",
            "properties": {
                'id': 'la-fac7e744-ab40-4100-a447-cbbb16f29ded'
            },
        }
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.mark.parametrize("mock_correct_response", [payment_method_response()], indirect=True)
    def test_return_payment_method_on_correct_params(
        self, mocker, mock_correct_response, default_payment_method_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_payment_method_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_payment_method_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_payment_method_data)

    @pytest.mark.parametrize("mock_correct_response", [payment_method_response()], indirect=True)
    def test_return_payment_method_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_payment_method_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_payment_method_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_payment_method_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_payment_method_data)

    @pytest.mark.parametrize("mock_correct_response", [payment_method_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        self.run_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)
# fmt: on
