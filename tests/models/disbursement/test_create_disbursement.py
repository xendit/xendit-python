import pytest
from ..base_model_test import BaseModelTest
from .sample_response import disbursement_response
from xendit.models import Disbursement
from xendit._api_requestor import _APIRequestor


# fmt: off
class TestCreateDisbursement(BaseModelTest):
    @pytest.fixture
    def default_disbursement_data(self):
        tested_class = Disbursement
        class_name = "Disbursement"
        method_name = "create"
        http_method_name = "post"
        args = ("demo_1475459775872", "BCA", "Bob Jones", "1231242311", "Reimbursement for shoes", 17000,)
        kwargs = {}
        params = (args, kwargs)
        url = "/disbursements"
        expected_correct_result = disbursement_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

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
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, default_disbursement_data):
        """It should send correct request to API Requestor

        Args:
            mocker (fixture): Default mocker fixture
            mock_correct_response (function): Mock correct response that sent by APIRequestor
            default_tested_class_data (tuple): Tuple with 6 item that contain:
            - tested_class (class): Class that will be tested
            - class_name (str): String representation for the class
            - method_name (str): Method name that will be tested
            - http_method_name (str): HTTP Method name that will be used in the API Requestor
            - url (str): URL for the request
            - params (tuple): Params with format (args, kwargs)
            - expected_correct_result (dict): Expected Correct Result
        """
        _, _, _, http_method_name, url, params, expected_correct_result = default_disbursement_data
        args, kwargs = params
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

        mocker.patch.object(_APIRequestor, http_method_name)
        tested_method = getattr(_APIRequestor, http_method_name)
        setattr(tested_method, "return_value", mock_correct_response)

        Disbursement.create(*args, **kwargs)
        tested_method.assert_called_with(url, headers=headers, body=body)
# fmt: on
