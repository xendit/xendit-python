import pytest

from .base_integration_test import BaseIntegrationTest
from xendit import BalanceAccountType
from tests.sampleresponse.balance import balance_response


class TestBalance(BaseIntegrationTest):
    @pytest.fixture
    def Balance(self, xendit_instance):
        return xendit_instance.Balance

    def test_get_balance_return_correct_keys(self, Balance):
        balance = Balance.get(BalanceAccountType.HOLDING)
        self.assert_returned_object_has_same_key_as_sample_response(
            balance, balance_response()
        )
