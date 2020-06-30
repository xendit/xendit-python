import pytest

from .base_integration_test import BaseIntegrationTest
from tests.sampleresponse.retail_outlet import retail_outlet_response
from tests.sampleresponse.retail_outlet import retail_outlet_update_response


class TestRetailOutlet(BaseIntegrationTest):
    @pytest.fixture
    def RetailOutlet(self, xendit_instance):
        return xendit_instance.RetailOutlet

    def test_create_fixed_payment_code_return_correct_keys(self, RetailOutlet):
        retail_outlet = RetailOutlet.create_fixed_payment_code(
            "demo_fixed_payment_code_123", "ALFAMART", "Rika Sutanto", 10000
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            retail_outlet, retail_outlet_response()
        )

    def test_update_fixed_payment_code_return_correct_keys(self, RetailOutlet):
        retail_outlet = RetailOutlet.update_fixed_payment_code(
            "5ef2f0f8e7f5c14077275493", name="Joe Contini"
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            retail_outlet, retail_outlet_update_response()
        )

    def test_get_fixed_payment_code_return_correct_keys(self, RetailOutlet):
        retail_outlet = RetailOutlet.get_fixed_payment_code("5ef2f0f8e7f5c14077275493")
        self.assert_returned_object_has_same_key_as_sample_response(
            retail_outlet, retail_outlet_response()
        )
