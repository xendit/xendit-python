import pytest
from ..base_model_test import BaseModelTest
from .sample_response import retail_outlet_response
from xendit.models import RetailOutlet
from xendit._api_requestor import _APIRequestor


# fmt: off
class TestGetFixedPaymentCode(BaseModelTest):
    @pytest.fixture
    def default_retail_outlet_data(self):
        tested_class = RetailOutlet
        class_name = "RetailOutlet"
        method_name = "get_fixed_payment_code"
        http_method_name = "get"
        args = ("5ef2f0f8e7f5c14077275493",)
        kwargs = {}
        params = (args, kwargs)
        url = f"/fixed_payment_code/{args[0]}"
        expected_correct_result = retail_outlet_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.mark.parametrize("mock_correct_response", [retail_outlet_response()], indirect=True)
    def test_return_retail_outlet_on_correct_params(
        self, mocker, mock_correct_response, default_retail_outlet_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_retail_outlet_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_retail_outlet_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_retail_outlet_data)

    @pytest.mark.parametrize("mock_correct_response", [retail_outlet_response()], indirect=True)
    def test_return_retail_outlet_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_retail_outlet_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_retail_outlet_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_retail_outlet_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_retail_outlet_data)

    @pytest.mark.parametrize("mock_correct_response", [retail_outlet_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, default_retail_outlet_data):
        """It should send correct request to API Requestor

        Args:
            mocker (fixture): Default mocker fixture
            mock_correct_response (function): Mock correct response that sent by APIRequestor
            default_tested_class_data (tuple): Tuple with 7 item that contain:
            - tested_class (class): Class that will be tested
            - class_name (str): String representation for the class
            - method_name (str): Method name that will be tested
            - http_method_name (str): HTTP Method name that will be used in the API Requestor
            - url (str): URL for the request
            - params (tuple): Params with format (args, kwargs)
            - expected_correct_result (dict): Expected Correct Result
        """
        _, _, _, http_method_name, url, params, expected_correct_result = default_retail_outlet_data
        args, kwargs = params

        mocker.patch.object(_APIRequestor, http_method_name)
        tested_method = getattr(_APIRequestor, http_method_name)
        setattr(tested_method, "return_value", mock_correct_response)

        RetailOutlet.get_fixed_payment_code(*args, **kwargs)
        tested_method.assert_called_with(url)
# fmt: on
