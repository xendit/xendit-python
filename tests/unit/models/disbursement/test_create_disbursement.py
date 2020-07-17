import pytest
from ..model_base_test import ModelBaseTest
from tests.sampleresponse.disbursement import disbursement_response
from xendit.models import Disbursement


# fmt: off
class TestCreateDisbursement(ModelBaseTest):
    @pytest.fixture
    def default_disbursement_data(self):
        tested_class = Disbursement
        class_name = "Disbursement"
        method_name = "create"
        http_method_name = "post"
        args = ()
        kwargs = {
            "external_id": "demo_1475459775872",
            "bank_code": "BCA",
            "account_holder_name": "Bob Jones",
            "account_number": "1231242311",
            "description": "Reimbursement for shoes",
            "amount": 17000,
        }
        params = (args, kwargs)
        url = "/disbursements"
        expected_correct_result = disbursement_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data(self, default_disbursement_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_disbursement_data
        headers = {}
        body = {
            "external_id": "demo_1475459775872",
            "bank_code": "BCA",
            "account_holder_name": "Bob Jones",
            "account_number": "1231242311",
            "description": "Reimbursement for shoes",
            "amount": 17000,
            "email_bcc": [],
            "email_cc": [],
            "email_to": [],
        }
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.mark.parametrize("mock_correct_response", [disbursement_response()], indirect=True)
    def test_return_disbursement_on_correct_params(
        self, mocker, mock_correct_response, default_disbursement_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_disbursement_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_disbursement_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_disbursement_data)

    @pytest.mark.parametrize("mock_correct_response", [disbursement_response()], indirect=True)
    def test_return_disbursement_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_disbursement_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_disbursement_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_disbursement_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_disbursement_data)

    @pytest.mark.parametrize("mock_correct_response", [disbursement_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        self.run_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)
# fmt: on
