import pytest
from ..model_base_test import ModelBaseTest
from tests.sampleresponse.direct_debit import linked_account_response
from xendit.models import DirectDebit


# fmt: off
class TestValidateTokenOTP(ModelBaseTest):
    @pytest.fixture
    def default_linked_account_token_data(self):
        tested_class = DirectDebit
        class_name = "DirectDebit"
        method_name = "validate_token_otp"
        http_method_name = "post"
        args = ()
        kwargs = {
            "linked_account_token_id": "lat-afcfde47-18e0-4d68-bf1b-c729a5d8e54a",
            "otp_code": "333000"
        }
        params = (args, kwargs)
        url = f"/linked_account_tokens/{kwargs['linked_account_token_id']}/validate_otp"
        expected_correct_result = linked_account_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data(self, default_linked_account_token_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_linked_account_token_data
        headers = {}
        body = {
            "otp_code": "333000",
        }
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.mark.parametrize("mock_correct_response", [linked_account_response()], indirect=True)
    def test_return_linked_account_token_on_correct_params(
        self, mocker, mock_correct_response, default_linked_account_token_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_linked_account_token_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_linked_account_token_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_linked_account_token_data)

    @pytest.mark.parametrize("mock_correct_response", [linked_account_response()], indirect=True)
    def test_return_linked_account_token_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_linked_account_token_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_linked_account_token_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_linked_account_token_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_linked_account_token_data)

    @pytest.mark.parametrize("mock_correct_response", [linked_account_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        self.run_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)
# fmt: on
