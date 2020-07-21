import pytest
from ..model_base_test import ModelBaseTest
from tests.sampleresponse.batch_disbursement import batch_disbursement_response
from xendit.models import BatchDisbursement


# fmt: off
class TestGetBatchDisbursement(ModelBaseTest):
    @pytest.fixture
    def default_batch_disbursement_data(self):
        tested_class = BatchDisbursement
        class_name = "BatchDisbursement"
        method_name = "create"
        http_method_name = "post"

        batch_disbursement_items = []
        batch_disbursement_items.append(
            BatchDisbursement.helper_create_batch_item(
                amount=10000,
                bank_code="BCA",
                bank_account_name="Adyaksa W",
                bank_account_number="12345678",
                description="Sample Batch Disbursement",
                external_id="batch-disbursement-item-12345",
            )
        )
        args = ()
        kwargs = {
            "reference": "batch_disbursement-12345",
            "disbursements": batch_disbursement_items,
            "x_idempotency_key": "test_idemp_123",
        }
        params = (args, kwargs)
        url = "/batch_disbursements"
        expected_correct_result = batch_disbursement_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data(self, default_batch_disbursement_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_batch_disbursement_data
        headers = {"X-IDEMPOTENCY-KEY": "test_idemp_123"}
        body = {
            "reference": "batch_disbursement-12345",
            "disbursements": [
                {
                    "amount": 10000,
                    "bank_code": "BCA",
                    "bank_account_name": "Adyaksa W",
                    "bank_account_number": "12345678",
                    "description": "Sample Batch Disbursement",
                    "external_id": "batch-disbursement-item-12345",
                }
            ]
        }
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.mark.parametrize("mock_correct_response", [batch_disbursement_response()], indirect=True)
    def test_return_batch_disbursement_on_correct_params(
        self, mocker, mock_correct_response, default_batch_disbursement_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_batch_disbursement_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_batch_disbursement_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_batch_disbursement_data)

    @pytest.mark.parametrize("mock_correct_response", [batch_disbursement_response()], indirect=True)
    def test_return_batch_disbursement_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_batch_disbursement_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_batch_disbursement_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_batch_disbursement_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_batch_disbursement_data)

    @pytest.mark.parametrize("mock_correct_response", [batch_disbursement_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        self.run_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)

# fmt: on
