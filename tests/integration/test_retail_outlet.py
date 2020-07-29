import pytest

from .base_integration_test import BaseIntegrationTest
from tests.sampleresponse.retail_outlet import retail_outlet_response
from tests.sampleresponse.retail_outlet import retail_outlet_update_response


class TestRetailOutlet(BaseIntegrationTest):
    @pytest.fixture(scope="class")
    def RetailOutlet(self, xendit_instance):
        return xendit_instance.RetailOutlet

    @pytest.fixture(scope="class")
    def retail_outlet_data(self, RetailOutlet):
        retail_outlet = RetailOutlet.create_fixed_payment_code(
            external_id="demo_fixed_payment_code_123",
            retail_outlet_name="ALFAMART",
            name="Rika Sutanto",
            expected_amount=10000,
        )
        return retail_outlet

    def test_create_fixed_payment_code_return_correct_keys(self, retail_outlet_data):
        retail_outlet = retail_outlet_data
        self.assert_returned_object_has_same_key_as_sample_response(
            retail_outlet, retail_outlet_response()
        )

    def test_update_fixed_payment_code_return_correct_keys(
        self, RetailOutlet, retail_outlet_data
    ):
        retail_outlet = retail_outlet_data
        retail_outlet = RetailOutlet.update_fixed_payment_code(
            fixed_payment_code_id=retail_outlet.id, name="Joe Contini",
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            retail_outlet, retail_outlet_update_response()
        )

    def test_get_fixed_payment_code_return_correct_keys(
        self, RetailOutlet, retail_outlet_data
    ):
        retail_outlet = retail_outlet_data
        retail_outlet = RetailOutlet.get_fixed_payment_code(
            fixed_payment_code_id=retail_outlet.id
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            retail_outlet, retail_outlet_response()
        )
