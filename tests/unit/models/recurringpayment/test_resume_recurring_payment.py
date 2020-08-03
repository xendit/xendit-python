import pytest
from ..model_base_test import ModelBaseTest
from tests.sampleresponse.recurring_payment import recurring_payment_response
from xendit.models import RecurringPayment


# fmt: off
class TestResumeRecurringPayment(ModelBaseTest):
    @pytest.fixture
    def default_recurring_payment_data(self):
        tested_class = RecurringPayment
        class_name = "RecurringPayment"
        method_name = "resume"
        http_method_name = "post"
        args = ()
        kwargs = {
            "id": "mock_id-123",
        }
        params = (args, kwargs)
        url = f"/recurring_payments/{kwargs['id']}/resume!"
        expected_correct_result = recurring_payment_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data(self, default_recurring_payment_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_recurring_payment_data
        headers = {}
        body = {}
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.mark.parametrize("mock_correct_response", [recurring_payment_response()], indirect=True)
    def test_return_recurring_payment_on_correct_params(
        self, mocker, mock_correct_response, default_recurring_payment_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_recurring_payment_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_recurring_payment_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_recurring_payment_data)

    @pytest.mark.parametrize("mock_correct_response", [recurring_payment_response()], indirect=True)
    def test_return_recurring_payment_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_recurring_payment_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_recurring_payment_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_recurring_payment_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_recurring_payment_data)

    @pytest.mark.parametrize("mock_correct_response", [recurring_payment_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        self.run_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)
# fmt: on
