import pytest

from .base_integration_test import BaseIntegrationTest
from tests.sampleresponse.credit_card import (
    reverse_auth_response,
    charge_response,
    refund_response,
    charge_option_response,
    promotion_response,
    promotion_calculation_response,
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
        charge_response()
        pass

    def test_capture_charge_return_correct_keys(self, CreditCard):
        charge_response()
        pass

    def test_get_charge_return_correct_keys(self, CreditCard):
        charge_response()
        pass

    def test_create_refund_return_correct_keys(self, CreditCard):
        refund_response()
        pass

    def test_get_charge_option_return_correct_keys(self, CreditCard):
        charge_option_response()
        pass

    def test_create_promotion_return_correct_keys(self, CreditCard):
        promotion_response()
        pass

    def test_get_promotion_return_correct_keys(self, CreditCard):
        promotion_response()
        pass

    def test_get_promotion_calculation_return_correct_keys(self, CreditCard):
        promotion_calculation_response()
        pass
