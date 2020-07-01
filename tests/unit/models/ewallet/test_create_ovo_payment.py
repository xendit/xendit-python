import pytest
from ..base_model_test import BaseModelTest
from tests.sampleresponse.ewallet import ovo_payment_response
from xendit.models import EWallet


# fmt: off
class TestCreateOVOPayment(BaseModelTest):
    @pytest.fixture
    def default_ovo_payment_data(self):
        tested_class = EWallet
        class_name = "EWallet"
        method_name = "create_ovo_payment"
        http_method_name = "post"
        args = ("ovo-ewallet-testing-id-123321131114", "8888", "08123123123")
        kwargs = {"x_idempotency_key": "test-idemp_123"}
        params = (args, kwargs)
        url = "/ewallets"
        expected_correct_result = ovo_payment_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data(self, default_ovo_payment_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_ovo_payment_data
        headers = {"X-IDEMPOTENCY-KEY": "test-idemp_123"}
        body = {
            "external_id": "ovo-ewallet-testing-id-123321131114",
            "amount": "8888",
            "phone": "08123123123",
            "ewallet_type": "OVO",
        }
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.mark.parametrize("mock_correct_response", [ovo_payment_response()], indirect=True)
    def test_return_ovo_payment_on_correct_params(
        self, mocker, mock_correct_response, default_ovo_payment_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_ovo_payment_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_ovo_payment_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_ovo_payment_data)

    @pytest.mark.parametrize("mock_correct_response", [ovo_payment_response()], indirect=True)
    def test_return_ovo_payment_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_ovo_payment_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_ovo_payment_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_ovo_payment_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_ovo_payment_data)

    @pytest.mark.parametrize("mock_correct_response", [ovo_payment_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        super().test_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)

    @pytest.mark.oldversion
    @pytest.mark.parametrize("mock_correct_response", [ovo_payment_response("2019-02-04")], indirect=True)
    def test_return_ovo_payment_on_correct_params_and_old_version(
        self, mocker, mock_correct_response, default_ovo_payment_data
    ):
        (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result) = default_ovo_payment_data
        params[1]["x_api_version"] = "2019-02-04"
        expected_correct_result = ovo_payment_response("2019-02-04")
        default_ovo_payment_data = (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_ovo_payment_data)
# fmt: on
