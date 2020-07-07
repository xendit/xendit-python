import pytest
import time

from .base_integration_test import BaseIntegrationTest
from tests.sampleresponse.credit_card import (
    reverse_auth_response,
    charge_response,
    refund_response,
    promotion_response,
)


class TestCreditCard(BaseIntegrationTest):
    @pytest.fixture
    def CreditCard(self, xendit_instance):
        return xendit_instance.CreditCard

    def test_create_authorization_return_correct_keys(self, CreditCard):
        charge_response()
        pass

    def test_reverse_authorization_return_correct_keys(self, CreditCard):
        reverse_auth_response()
        pass

    def test_create_charge_return_correct_keys(self, CreditCard):
        address = CreditCard.helper_create_address(country="Indonesia")
        billing_details = CreditCard.helper_create_billing_details(
            given_names="Adyaksa", address=address
        )
        installment = CreditCard.helper_create_installment(count=1, interval="month")
        promotion = CreditCard.helper_create_charge_promotion(
            reference_id="Xendit-123", original_amount=75000
        )

        charge = CreditCard.create_charge(
            token_id="5f0410898bcf7a001a00879d",
            external_id=f"card_preAuth-{int(time.time())}",
            amount=75000,
            card_cvn="123",
            billing_details=billing_details,
            installment=installment,
            promotion=promotion,
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            charge, charge_response()
        )

    def test_capture_charge_return_correct_keys(self, CreditCard):
        charge_response()
        pass

    def test_get_charge_return_correct_keys(self, CreditCard):
        charge_response()
        pass

    def test_create_refund_return_correct_keys(self, CreditCard):
        refund_response()
        pass

    def test_create_promotion_return_correct_keys(self, CreditCard):
        promotion_response()
        pass
