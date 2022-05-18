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
        charge = CreditCard.create_authorization(
            token_id="602b9886396b5a001c99b798",
            external_id=f"card_preAuth-{int(time.time())}",
            amount=75000,
            card_cvn="123",
            metadata={
                "meta": "data",
            },
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            charge, charge_response()
        )

    def test_reverse_authorization_return_correct_keys(self, CreditCard):
        charge = CreditCard.create_authorization(
            token_id="602b9886396b5a001c99b798",
            external_id=f"card_preAuth-{int(time.time())}",
            amount=75000,
            card_cvn="123",
        )
        reverse_auth = CreditCard.reverse_authorization(
            credit_card_charge_id=charge.id,
            external_id=f"reverse-authorization-{int(time.time())}",
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            reverse_auth, reverse_auth_response()
        )

    def test_create_charge_return_correct_keys(self, CreditCard):
        charge = CreditCard.create_charge(
            token_id="602b9886396b5a001c99b798",
            external_id=f"card_preAuth-{int(time.time())}",
            amount=75000,
            card_cvn="123",
            metadata={
                "meta": "data",
            },
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            charge, charge_response()
        )

    def test_capture_charge_return_correct_keys(self, CreditCard):
        charge = CreditCard.create_authorization(
            token_id="602b9886396b5a001c99b798",
            external_id=f"card_preAuth-{int(time.time())}",
            amount=75000,
            card_cvn="123",
        )
        captured_charge = CreditCard.capture_charge(
            credit_card_charge_id=charge.id, amount=75000,
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            captured_charge, charge_response()
        )

    def test_get_charge_return_correct_keys(self, CreditCard):
        charge = CreditCard.create_charge(
            token_id="602b9886396b5a001c99b798",
            external_id=f"card_preAuth-{int(time.time())}",
            amount=75000,
            card_cvn="123",
        )

        charge = CreditCard.get_charge(credit_card_charge_id=charge.id)
        self.assert_returned_object_has_same_key_as_sample_response(
            charge, charge_response()
        )

    def test_create_refund_return_correct_keys(self, CreditCard):
        charge = CreditCard.create_charge(
            token_id="602b9886396b5a001c99b798",
            external_id=f"card_preAuth-{int(time.time())}",
            amount=75000,
            card_cvn="123",
        )

        refund = CreditCard.create_refund(
            credit_card_charge_id=charge.id,
            amount=10000,
            external_id=f"card_refund-{int(time.time())}",
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            refund, refund_response()
        )

    def test_create_promotion_return_correct_keys(self, CreditCard):
        promotion = CreditCard.create_promotion(
            reference_id=f"BRI_20_JAN-{int(time.time())}",
            description="20% discount applied for all BRI cards",
            discount_amount=10000,
            bin_list=["400000", "460000"],
            start_time="2020-01-01T00:00:00.000Z",
            end_time="2100-01-01T00:00:00.000Z",
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            promotion, promotion_response()
        )
