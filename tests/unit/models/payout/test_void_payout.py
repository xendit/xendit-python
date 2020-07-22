import pytest
from ..model_base_test import ModelBaseTest
from tests.sampleresponse.payout import void_payout_response
from xendit.models import Payout


# fmt: off
class TestVoidPayout(ModelBaseTest):
    @pytest.fixture
    def default_payout_data(self):
        tested_class = Payout
        class_name = "Payout"
        method_name = "void"
        http_method_name = "post"
        args = ()
        kwargs = {
            "id": "a6ee1bf1-ffcd-4bda-a7ab-99c1d5cd0472",
        }
        params = (args, kwargs)
        url = f"/payouts/{kwargs['id']}/void"
        expected_correct_result = void_payout_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data(self, default_payout_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_payout_data
        headers = {}
        body = {}
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.mark.parametrize("mock_correct_response", [void_payout_response()], indirect=True)
    def test_return_payout_on_correct_params(
        self, mocker, mock_correct_response, default_payout_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_payout_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_payout_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_payout_data)

    @pytest.mark.parametrize("mock_correct_response", [void_payout_response()], indirect=True)
    def test_return_payout_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_payout_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_payout_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_payout_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_payout_data)

    @pytest.mark.parametrize("mock_correct_response", [void_payout_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        self.run_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)

# fmt: on
