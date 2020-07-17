import pytest
from ..model_base_test import ModelBaseTest
from tests.sampleresponse.qrcode import qrcode_response
from xendit.models import QRCode, QRCodeType


# fmt: off
class TestCreateQRCode(ModelBaseTest):
    @pytest.fixture
    def default_qrcode_data(self):
        tested_class = QRCode
        class_name = "QRCode"
        method_name = "create"
        http_method_name = "post"
        args = ()
        kwargs = {
            "external_id": "mock-qrcode-id-1594794038",
            "type": QRCodeType.DYNAMIC,
            "callback_url": "https://mock-site.site",
            "amount": "4000",
            "x_idempotency_key": "test-idemp_123",
        }
        params = (args, kwargs)
        url = "/qr_codes"
        expected_correct_result = qrcode_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data(self, default_qrcode_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_qrcode_data
        headers = {"X-IDEMPOTENCY-KEY": "test-idemp_123"}
        body = {
            "external_id": "mock-qrcode-id-1594794038",
            "type": "DYNAMIC",
            "callback_url": "https://mock-site.site",
            "amount": "4000",
        }
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.mark.parametrize("mock_correct_response", [qrcode_response()], indirect=True)
    def test_return_qrcode_on_correct_params(
        self, mocker, mock_correct_response, default_qrcode_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_qrcode_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_qrcode_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_qrcode_data)

    @pytest.mark.parametrize("mock_correct_response", [qrcode_response()], indirect=True)
    def test_return_qrcode_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_qrcode_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_qrcode_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_qrcode_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_qrcode_data)

    @pytest.mark.parametrize("mock_correct_response", [qrcode_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        self.run_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)
# fmt: on
