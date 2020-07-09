import pytest
import time

from .base_integration_test import BaseIntegrationTest
from tests.sampleresponse.direct_debit import customer_response, multi_customer_response


class TestDirectDebit(BaseIntegrationTest):
    @pytest.fixture
    def DirectDebit(self, xendit_instance):
        return xendit_instance.DirectDebit

    def test_create_customer_return_correct_keys(self, DirectDebit):
        customer = DirectDebit.create_customer(
            reference_id=f"merc-{int(time.time())}",
            email="t@x.co",
            given_names="Adyaksa",
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            customer, customer_response()
        )

    @pytest.mark.skip(reason="Currently not implemented by Direct Debit")
    def test_get_customer_by_ref_id_return_correct_keys(self, DirectDebit):
        customer = DirectDebit.get_customer_by_ref_id(reference_id="merc-1594272368",)
        self.assert_returned_object_has_same_key_as_sample_response(
            customer[0], multi_customer_response()
        )
