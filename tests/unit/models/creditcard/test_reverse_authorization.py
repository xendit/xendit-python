import pytest
from ..model_base_test import ModelBaseTest
from tests.sampleresponse.credit_card import reverse_auth_response
from xendit.models import CreditCard


# fmt: off
class TestReverseAuthorization(ModelBaseTest):
    @pytest.fixture
    def default_credit_card_data(self):
        tested_class = CreditCard
        class_name = "CreditCard"
        method_name = "reverse_authorization"
        http_method_name = "post"
        args = ()
        kwargs = {
            "credit_card_charge_id": "mock_token-123",
            "external_id": "mock_reverse-authorization-123",
            "x_idempotency_key": "test-idemp_123",
        }
        params = (args, kwargs)
        url = f"/credit_card_charges/{kwargs['credit_card_charge_id']}/auth_reversal"
        expected_correct_result = reverse_auth_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data(self, default_credit_card_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_credit_card_data
        headers = {"X-IDEMPOTENCY-KEY": "test-idemp_123"}
        body = {
            "external_id": "mock_reverse-authorization-123",
        }
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.mark.parametrize("mock_correct_response", [reverse_auth_response()], indirect=True)
    def test_return_reverse_authorization_on_correct_params(
        self, mocker, mock_correct_response, default_credit_card_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_credit_card_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_credit_card_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_credit_card_data)

    @pytest.mark.parametrize("mock_correct_response", [reverse_auth_response()], indirect=True)
    def test_return_reverse_authorization_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_credit_card_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_credit_card_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_credit_card_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_credit_card_data)

    @pytest.mark.parametrize("mock_correct_response", [reverse_auth_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        self.run_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)
# fmt: on
