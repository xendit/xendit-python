import pytest
import time

from .base_integration_test import BaseIntegrationTest
from tests.sampleresponse.cardless_credit import (
    cardless_credit_payment_response,
    cardless_credit_payment_type_response,
)
from xendit import CardlessCreditType


class TestCardlessCredit(BaseIntegrationTest):
    @pytest.fixture
    def CardlessCredit(self, xendit_instance_cardless_enabled):
        return xendit_instance_cardless_enabled.CardlessCredit

    def test_create_payment_return_correct_keys(self, CardlessCredit):
        cardless_credit_items = []
        cardless_credit_items.append(
            CardlessCredit.helper_create_item(
                id=f"item-{int(time.time())}",
                name="Phone Case",
                price=200000,
                type="Smartphone",
                url="http://example.com/phone/phone_case",
                quantity=2,
            )
        )
        customer_details = CardlessCredit.helper_create_customer_details(
            first_name="customer first name",
            last_name="customer last name",
            email="customer@email.com",
            phone="0812332145",
        )
        shipping_address = CardlessCredit.helper_create_shipping_address(
            first_name="first name",
            last_name="last name",
            address="Jl Teknologi No. 12",
            city="Jakarta",
            postal_code="12345",
            phone="081513114262",
            country_code="IDN",
        )
        cardless_credit_payment = CardlessCredit.create_payment(
            cardless_credit_type=CardlessCreditType.KREDIVO,
            external_id=f"ext-id-{int(time.time())}",
            amount=10000,
            payment_type="3_months",
            items=cardless_credit_items,
            customer_details=customer_details,
            shipping_address=shipping_address,
            redirect_url="https://mock-my-shop.com/home",
            callback_url="https://mock-my-shop.com/callback",
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            cardless_credit_payment, cardless_credit_payment_response()
        )

    def test_calculate_payment_type_return_correct_keys(self, CardlessCredit):
        cardless_credit_items = []
        cardless_credit_items.append(
            CardlessCredit.helper_create_item(
                id=f"item-{int(time.time())}",
                name="Phone Case",
                price=200000,
                type="Smartphone",
                url="http://example.com/phone/phone_case",
                quantity=2,
            )
        )

        cardless_credit_payment_types = CardlessCredit.calculate_payment_type(
            cardless_credit_type=CardlessCreditType.KREDIVO,
            amount=10000,
            items=cardless_credit_items,
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            cardless_credit_payment_types, cardless_credit_payment_type_response()
        )
