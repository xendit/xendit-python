import pytest
import time

from .base_integration_test import BaseIntegrationTest
from tests.sampleresponse.payout import payout_response
from tests.sampleresponse.payout import void_payout_response


class TestPayout(BaseIntegrationTest):
    @pytest.fixture
    def Payout(self, xendit_instance):
        return xendit_instance.Payout

    @pytest.fixture
    def payout_data(self, Payout):
        payout = Payout.create(
            external_id=f"payout-{int(time.time())}",
            amount=50000,
            email="test@email.co",
        )
        return payout

    def test_create_payout_return_correct_keys(self, payout_data):
        payout = payout_data
        self.assert_returned_object_has_same_key_as_sample_response(
            payout, payout_response()
        )

    def test_get_payout_return_correct_keys(self, Payout, payout_data):
        payout = payout_data
        payout = Payout.get(id=payout.id)
        self.assert_returned_object_has_same_key_as_sample_response(
            payout, payout_response()
        )

    def test_void_payout_return_correct_keys(self, Payout, payout_data):
        payout = payout_data
        void_payout = Payout.void(id=payout.id)
        self.assert_returned_object_has_same_key_as_sample_response(
            void_payout, void_payout_response()
        )
