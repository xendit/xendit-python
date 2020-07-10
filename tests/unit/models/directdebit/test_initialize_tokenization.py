import pytest
from ..model_base_test import ModelBaseTest
from tests.sampleresponse.direct_debit import linked_account_response
from xendit.models import DirectDebit


# fmt: off
class TestInitializeTokenization(ModelBaseTest):
    @pytest.fixture
    def default_linked_account_data(self):
        tested_class = DirectDebit
        class_name = "DirectDebit"
        method_name = "initialize_tokenization"
        http_method_name = "post"
        card_linking = DirectDebit.helper_create_card_link(
            account_mobile_number="+62818555988",
            card_last_four="8888",
            card_expiry="06/24",
            account_email="test.email@xendit.co",
        )

        args = ()
        kwargs = {
            "customer_id": "ed20b5db-df04-41fc-8018-8ea4ac4d1030",
            "channel_code": "DC_BRI",
            "properties": card_linking,
        }
        params = (args, kwargs)
        url = "/linked_account_tokens/auth"
        expected_correct_result = linked_account_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data_card(self, default_linked_account_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_linked_account_data
        headers = {}
        body = {
            "customer_id": "ed20b5db-df04-41fc-8018-8ea4ac4d1030",
            "channel_code": "DC_BRI",
            "properties": {
                "account_mobile_number": "+62818555988",
                "card_last_four": "8888",
                "card_expiry": "06/24",
                "account_email": "test.email@xendit.co",
            },
        }
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.fixture
    def api_requestor_request_data_online_bank(self, default_linked_account_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_linked_account_data
        online_bank_linking = DirectDebit.helper_create_online_banking_link(
            success_redirect_url="https://mock-test.co",
            failure_redirect_url="https://mock-test.co",
        )
        params[1]['properties'] = online_bank_linking
        headers = {}
        body = {
            "customer_id": "ed20b5db-df04-41fc-8018-8ea4ac4d1030",
            "channel_code": "DC_BRI",
            "properties": {
                "success_redirect_url": "https://mock-test.co",
                "failure_redirect_url": "https://mock-test.co",
            },
        }
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.mark.parametrize("mock_correct_response", [linked_account_response()], indirect=True)
    def test_return_linked_account_on_correct_params(
        self, mocker, mock_correct_response, default_linked_account_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_linked_account_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_linked_account_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_linked_account_data)

    @pytest.mark.parametrize("mock_correct_response", [linked_account_response()], indirect=True)
    def test_return_linked_account_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_linked_account_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_linked_account_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_linked_account_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_linked_account_data)

    @pytest.mark.parametrize("mock_correct_response", [linked_account_response()], indirect=True)
    def test_send_correct_card_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data_card):
        self.run_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data_card)

    @pytest.mark.parametrize("mock_correct_response", [linked_account_response()], indirect=True)
    def test_send_correct_online_bank_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data_online_bank):
        self.run_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data_online_bank)
# fmt: on
