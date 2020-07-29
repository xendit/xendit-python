import pytest

from .base_integration_test import BaseIntegrationTest
from tests.sampleresponse.disbursement import disbursement_response
from tests.sampleresponse.disbursement import disbursement_banks_response


class TestDisbursement(BaseIntegrationTest):
    @pytest.fixture(scope="class")
    def Disbursement(self, xendit_instance):
        return xendit_instance.Disbursement

    @pytest.fixture(scope="class")
    def disbursement_data(self, Disbursement):
        disbursement = Disbursement.create(
            external_id="demo_1475459775872",
            bank_code="BCA",
            account_holder_name="Bob Jones",
            account_number="1231242311",
            description="Reimbursement for shoes",
            amount=17000,
        )
        return disbursement

    def test_create_disbursement_return_correct_keys(self, disbursement_data):
        disbursement = disbursement_data
        self.assert_returned_object_has_same_key_as_sample_response(
            disbursement, disbursement_response()
        )

    def test_get_disbursement_by_id_return_correct_keys(
        self, Disbursement, disbursement_data
    ):
        disbursement = disbursement_data

        disbursement = Disbursement.get(id=disbursement.id)
        self.assert_returned_object_has_same_key_as_sample_response(
            disbursement, disbursement_response()
        )

    def test_get_disbursement_by_external_id_return_correct_keys(self, Disbursement):
        disbursement = Disbursement.get_by_ext_id(external_id="demo_1475459775872")
        self.assert_returned_object_has_same_key_as_sample_response(
            disbursement[0], disbursement_response()
        )

    def test_get_disbursement_banks_return_correct_keys(self, Disbursement):
        disbursement_banks = Disbursement.get_available_banks()
        self.assert_returned_object_has_same_key_as_sample_response(
            disbursement_banks[0], disbursement_banks_response()[0]
        )
