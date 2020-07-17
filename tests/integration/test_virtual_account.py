import pytest

from .base_integration_test import BaseIntegrationTest
from tests.sampleresponse.virtual_account import virtual_account_response
from tests.sampleresponse.virtual_account import virtual_account_banks_response
from tests.sampleresponse.virtual_account import virtual_account_payment_response


class TestVirtualAccount(BaseIntegrationTest):
    @pytest.fixture
    def VirtualAccount(self, xendit_instance):
        return xendit_instance.VirtualAccount

    def test_create_virtual_account_return_correct_keys(self, VirtualAccount):
        virtual_account = VirtualAccount.create(
            external_id="demo_1475459775872", bank_code="BNI", name="Rika Sutanto",
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            virtual_account, virtual_account_response()
        )

    def test_get_virtual_account_bank_return_correct_keys(self, VirtualAccount):
        virtual_account_banks = VirtualAccount.get_banks()
        self.assert_returned_object_has_same_key_as_sample_response(
            virtual_account_banks[0], virtual_account_banks_response()[0]
        )

    def test_get_virtual_account_return_correct_keys(self, VirtualAccount):
        virtual_account = VirtualAccount.get(id="5eec3a3e8dd9ea2fc97d6728")
        self.assert_returned_object_has_same_key_as_sample_response(
            virtual_account, virtual_account_response()
        )

    def test_update_virtual_account_return_correct_keys(self, VirtualAccount):
        virtual_account = VirtualAccount.update(
            id="5eec3a3e8dd9ea2fc97d6728", is_single_use=True,
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            virtual_account, virtual_account_response()
        )

    def test_get_virtual_account_payment_return_correct_keys(self, VirtualAccount):
        virtual_account_payment = VirtualAccount.get_payment(
            payment_id="5ef18efca7d10d1b4d61fb52"
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            virtual_account_payment, virtual_account_payment_response()
        )
