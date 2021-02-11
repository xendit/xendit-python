import pytest
from ..model_base_test import ModelBaseTest
from tests.sampleresponse.ewallet import ewallet_charge_response
from xendit.models import EWallet


# fmt: off
class TestCreateEWalletCharge(ModelBaseTest):
    @pytest.fixture
    def default_ewallet_charge_data(self):
        tested_class = EWallet
        class_name = "EWallet"
        method_name = "create_ewallet_charge"
        http_method_name = "post"
        basket = []
        basket_item = EWallet.helper_create_basket_item(
            reference_id = "basket-product-ref-id",
            name = "product_name",
            category = "mechanics",
            currency = "IDR",
            price = 50000,
            quantity = 5,
            type = "wht",
            sub_category = "evr",
            metadata = {
                "meta": "data"
            }
        )
        basket.append(basket_item)

        args = ()
        kwargs = {
            "reference_id": "test-reference-id",
            "currency": "IDR",
            "amount": 1688,
            "checkout_method": "ONE_TIME_PAYMENT",
            "channel_code": "ID_SHOPEEPAY",
            "channel_properties": {
                "success_redirect_url": "https://yourwebsite.com/order/123",
            },
            "basket": basket,
            "metadata": {
                "meta2": "data2",
            },
        }
        params = (args, kwargs)
        url = "/ewallets/charges"
        expected_correct_result = ewallet_charge_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data(self, default_ewallet_charge_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_ewallet_charge_data
        headers = {}
        body = {
            "reference_id": "test-reference-id",
            "currency": "IDR",
            "amount": 1688,
            "checkout_method": "ONE_TIME_PAYMENT",
            "channel_code": "ID_SHOPEEPAY",
            "channel_properties": {
                "success_redirect_url": "https://yourwebsite.com/order/123",
            },
            "basket": [
                {
                    "reference_id": "basket-product-ref-id",
                    "name": "product_name",
                    "category": "mechanics",
                    "currency": "IDR",
                    "price": 50000,
                    "quantity": 5,
                    "type": "wht",
                    "sub_category": "evr",
                    "metadata": {
                        "meta": "data"
                    },
                },
            ],
            "metadata": {
                "meta2": "data2",
            },
        }
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.mark.parametrize("mock_correct_response", [ewallet_charge_response()], indirect=True)
    def test_return_ewallet_charge_on_correct_params(
        self, mocker, mock_correct_response, default_ewallet_charge_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_ewallet_charge_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_ewallet_charge_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_ewallet_charge_data)

    @pytest.mark.parametrize("mock_correct_response", [ewallet_charge_response()], indirect=True)
    def test_return_ewallet_charge_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_ewallet_charge_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_ewallet_charge_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_ewallet_charge_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_ewallet_charge_data)

    @pytest.mark.parametrize("mock_correct_response", [ewallet_charge_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        self.run_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)
# fmt: on
