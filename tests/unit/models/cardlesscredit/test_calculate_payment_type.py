import pytest
from ..model_base_test import ModelBaseTest
from tests.sampleresponse.cardless_credit import cardless_credit_payment_response
from xendit.models import CardlessCredit, CardlessCreditType


# fmt: off
class TestCalculatePaymentType(ModelBaseTest):
    @pytest.fixture
    def default_cardless_credit_data(self):
        tested_class = CardlessCredit
        class_name = "CardlessCredit"
        method_name = "calculate_payment_type"
        http_method_name = "post"

        cardless_credit_items = []
        cardless_credit_items.append(
            CardlessCredit.helper_create_item(
                id="item-123",
                name="Phone Case",
                price=200000,
                type="Smartphone",
                url="http://example.com/phone/phone_case",
                quantity=2,
            )
        )
        args = ()
        kwargs = {
            "cardless_credit_type": CardlessCreditType.KREDIVO,
            "amount": 10000,
            "items": cardless_credit_items,
            "x_idempotency_key": "test_idemp_123"
        }
        params = (args, kwargs)
        url = "/cardless-credit/payment-types"
        expected_correct_result = cardless_credit_payment_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data(self, default_cardless_credit_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_cardless_credit_data
        headers = {"X-IDEMPOTENCY-KEY": "test_idemp_123"}
        body = {
            "cardless_credit_type": "KREDIVO",
            "amount": 10000,
            "items": [
                {
                    "id": "item-123",
                    "name": "Phone Case",
                    "price": 200000,
                    "type": "Smartphone",
                    "url": "http://example.com/phone/phone_case",
                    "quantity": 2,
                }
            ],
        }
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.mark.parametrize("mock_correct_response", [cardless_credit_payment_response()], indirect=True)
    def test_return_cardless_credit_payment_types_on_correct_params(
        self, mocker, mock_correct_response, default_cardless_credit_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_cardless_credit_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_cardless_credit_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_cardless_credit_data)

    @pytest.mark.parametrize("mock_correct_response", [cardless_credit_payment_response()], indirect=True)
    def test_return_cardless_credit_payment_types_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_cardless_credit_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_cardless_credit_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_cardless_credit_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_cardless_credit_data)

    @pytest.mark.parametrize("mock_correct_response", [cardless_credit_payment_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        self.run_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)

# fmt: on
