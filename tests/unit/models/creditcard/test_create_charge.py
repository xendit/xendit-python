import pytest
from ..model_base_test import ModelBaseTest
from tests.sampleresponse.credit_card import charge_response
from xendit.models import CreditCard


# fmt: off
class TestCreateCharge(ModelBaseTest):
    def helper(self):
        address = CreditCard.helper_create_address(country="Indonesia")
        billing_details = CreditCard.helper_create_billing_details(
            given_names="Adyaksa", address=address
        )
        installment = CreditCard.helper_create_installment(count=1, interval="month")
        promotion = CreditCard.helper_create_charge_promotion(
            reference_id="Xendit-123", original_amount=75000
        )
        return billing_details, installment, promotion

    @pytest.fixture
    def default_credit_card_data(self):
        tested_class = CreditCard
        class_name = "CreditCard"
        method_name = "create_charge"
        http_method_name = "post"
        billing_details, installment, promotion = self.helper()
        args = ()
        kwargs = {
            "token_id": "mock_token-id-123",
            "external_id": "mock_card_charge-123",
            "amount": 75000,
            "card_cvn": "123",
            "x_idempotency_key": "test-idemp_123",
            "billing_details": billing_details,
            "installment": installment,
            "promotion": promotion,
        }
        params = (args, kwargs)
        url = "/credit_card_charges"
        expected_correct_result = charge_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data(self, default_credit_card_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_credit_card_data
        headers = {"X-IDEMPOTENCY-KEY": "test-idemp_123"}
        body = {
            "token_id": "mock_token-id-123",
            "capture": True,
            "external_id": "mock_card_charge-123",
            "amount": 75000,
            "card_cvn": "123",
            "billing_details": {
                "given_names": "Adyaksa",
                "address": {
                    "country": "Indonesia"
                }
            },
            "installment": {
                "count": 1,
                "interval": "month",
            },
            "promotion": {
                "reference_id": "Xendit-123",
                "original_amount": 75000
            },
        }
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.mark.parametrize("mock_correct_response", [charge_response()], indirect=True)
    def test_return_charge_on_correct_params(
        self, mocker, mock_correct_response, default_credit_card_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_credit_card_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_credit_card_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_credit_card_data)

    @pytest.mark.parametrize("mock_correct_response", [charge_response()], indirect=True)
    def test_return_charge_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_credit_card_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_credit_card_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_credit_card_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_credit_card_data)

    @pytest.mark.parametrize("mock_correct_response", [charge_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        super().test_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)
# fmt: on
