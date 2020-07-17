import pytest
from ..model_base_test import ModelBaseTest
from tests.sampleresponse.direct_debit import accessible_accounts_response
from xendit.models import DirectDebit


# fmt: off
class TestGetAccessibleAccountsByToken(ModelBaseTest):
    @pytest.fixture
    def default_linked_account_token_data(self):
        tested_class = DirectDebit
        class_name = "DirectDebit"
        method_name = "get_accessible_accounts_by_token"
        http_method_name = "get"
        args = ()
        kwargs = {
            "linked_account_token_id": "lat-afcfde47-18e0-4d68-bf1b-c729a5d8e54a",
        }
        params = (args, kwargs)
        url = f"/linked_account_tokens/{kwargs['linked_account_token_id']}/accounts"
        expected_correct_result = accessible_accounts_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data(self, default_linked_account_token_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_linked_account_token_data
        headers = {}
        body = {}
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.mark.parametrize("mock_correct_response", [accessible_accounts_response()], indirect=True)
    def test_return_accessible_accounts_on_correct_params(
        self, mocker, mock_correct_response, default_linked_account_token_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_linked_account_token_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_linked_account_token_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_linked_account_token_data)

    @pytest.mark.parametrize("mock_correct_response", [accessible_accounts_response()], indirect=True)
    def test_return_accessible_accounts_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_linked_account_token_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_linked_account_token_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_linked_account_token_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_linked_account_token_data)

    @pytest.mark.parametrize("mock_correct_response", [accessible_accounts_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        self.run_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)
# fmt: on
