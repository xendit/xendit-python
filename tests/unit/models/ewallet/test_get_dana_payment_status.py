import pytest
from ..model_base_test import ModelBaseTest
from tests.sampleresponse.ewallet import dana_payment_status_response
from xendit.models import EWallet, EWalletType


# fmt: off
class TestGetDANAPaymentStatus(ModelBaseTest):
    @pytest.fixture
    def default_dana_payment_status_data(self):
        tested_class = EWallet
        class_name = "EWallet"
        method_name = "get_payment_status"
        http_method_name = "get"
        args = ()
        kwargs = {
            "external_id": "dana-ewallet-test-33312",
            "ewallet_type": EWalletType.DANA,
        }
        params = (args, kwargs)
        url = f"/ewallets?external_id={kwargs['external_id']}&ewallet_type={kwargs['ewallet_type'].name}"
        expected_correct_result = dana_payment_status_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data(self, default_dana_payment_status_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_dana_payment_status_data
        headers = {}
        body = {}
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.mark.parametrize("mock_correct_response", [dana_payment_status_response()], indirect=True)
    def test_return_dana_payment_status_on_correct_params(
        self, mocker, mock_correct_response, default_dana_payment_status_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_dana_payment_status_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_dana_payment_status_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_dana_payment_status_data)

    @pytest.mark.parametrize("mock_correct_response", [dana_payment_status_response()], indirect=True)
    def test_return_dana_payment_status_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_dana_payment_status_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_dana_payment_status_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_dana_payment_status_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_dana_payment_status_data)

    @pytest.mark.parametrize("mock_correct_response", [dana_payment_status_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        super().test_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)
# fmt: on
