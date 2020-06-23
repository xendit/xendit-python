import pytest
from ..base_model_test import BaseModelTest
from .sample_response import virtual_account_response
from xendit.models import VirtualAccount
from xendit._api_requestor import _APIRequestor


# fmt: off
class TestGetVirtualAccount(BaseModelTest):
    @pytest.fixture
    def default_virtual_account_data(self):
        tested_class = VirtualAccount
        class_name = "VirtualAccount"
        method_name = "get"
        http_method_name = "get"
        args = ("5eec3a3e8dd9ea2fc97d6728",)
        kwargs = {}
        params = (args, kwargs)
        url = f"/callback_virtual_accounts/{args[0]}"
        expected_correct_result = virtual_account_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.mark.parametrize("mock_correct_response", [virtual_account_response()], indirect=True)
    def test_return_virtual_account_on_correct_params(
        self, mocker, mock_correct_response, default_virtual_account_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_virtual_account_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_virtual_account_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_virtual_account_data)

    @pytest.mark.parametrize("mock_correct_response", [virtual_account_response()], indirect=True)
    def test_return_virtual_account_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_virtual_account_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_virtual_account_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_virtual_account_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_virtual_account_data)

    @pytest.mark.parametrize("mock_correct_response", [virtual_account_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, default_virtual_account_data):
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
        _, _, _, http_method_name, url, params, expected_correct_result = default_virtual_account_data
        args, kwargs = params

        mocker.patch.object(_APIRequestor, http_method_name)
        tested_method = getattr(_APIRequestor, http_method_name)
        setattr(tested_method, "return_value", mock_correct_response)

        VirtualAccount.get(*args, **kwargs)
        tested_method.assert_called_with(url)
# fmt: on