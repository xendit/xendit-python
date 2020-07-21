import pytest
import time

from .base_integration_test import BaseIntegrationTest
from tests.sampleresponse.batch_disbursement import batch_disbursement_response


class TestBatchDisbursement(BaseIntegrationTest):
    @pytest.fixture
    def BatchDisbursement(self, xendit_instance):
        return xendit_instance.BatchDisbursement

    def test_create_batch_disbursement_return_correct_keys(self, BatchDisbursement):
        batch_disbursement_items = []
        batch_disbursement_items.append(
            BatchDisbursement.helper_create_batch_item(
                amount=10000,
                bank_code="BCA",
                bank_account_name="Adyaksa W",
                bank_account_number="12345678",
                description="Sample Batch Disbursement",
                external_id=f"batch-disbursement-item-{int(time.time())}",
            )
        )
        batch_disbursement = BatchDisbursement.create(
            reference=f"batch_disbursement-{int(time.time())}",
            disbursements=batch_disbursement_items,
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            batch_disbursement, batch_disbursement_response()
        )
