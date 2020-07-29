import pytest
from ..model_base_test import ModelBaseTest
from tests.sampleresponse.xenplatform import xenplatform_account_response
from xendit.models import XenPlatform, XenPlatformAccountType


# fmt: off
class TestCreateAccount(ModelBaseTest):
    @pytest.fixture
    def default_xenplatform_data(self):
        tested_class = XenPlatform
        class_name = "XenPlatform"
        method_name = "create_account"
        http_method_name = "post"

        business_profile = XenPlatform.helper_create_business_profile(
            business_name="python-xendit",
        )
        args = ()
        kwargs = {
            "account_email": "test-xenplatform@pythonxendit.co",
            "type": XenPlatformAccountType.OWNED,
            "business_profile": business_profile,
            "x_idempotency_key": "test_idemp_123",
        }
        params = (args, kwargs)
        url = "/accounts"
        expected_correct_result = xenplatform_account_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data(self, default_xenplatform_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_xenplatform_data
        headers = {"X-IDEMPOTENCY-KEY": "test_idemp_123"}
        body = {
            "account_email": "test-xenplatform@pythonxendit.co",
            "type": "OWNED",
            "business_profile": {
                "business_name": "python-xendit"
            },
        }
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.mark.parametrize("mock_correct_response", [xenplatform_account_response()], indirect=True)
    def test_return_xenplatform_account_on_correct_params(
        self, mocker, mock_correct_response, default_xenplatform_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_xenplatform_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_xenplatform_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_xenplatform_data)

    @pytest.mark.parametrize("mock_correct_response", [xenplatform_account_response()], indirect=True)
    def test_return_xenplatform_account_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_xenplatform_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_xenplatform_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_xenplatform_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_xenplatform_data)

    @pytest.mark.parametrize("mock_correct_response", [xenplatform_account_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        self.run_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)

# fmt: on
