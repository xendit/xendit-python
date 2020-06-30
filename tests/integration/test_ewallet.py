import pytest
import time
import xendit

from .base_integration_test import BaseIntegrationTest

from xendit import EWalletType

from tests.sampleresponse.ewallet import ovo_payment_response
from tests.sampleresponse.ewallet import ovo_payment_status_response
from tests.sampleresponse.ewallet import dana_payment_response
from tests.sampleresponse.ewallet import dana_payment_status_response
from tests.sampleresponse.ewallet import linkaja_payment_response
from tests.sampleresponse.ewallet import linkaja_payment_status_completed_response
from tests.sampleresponse.ewallet import linkaja_payment_status_expired_response


class TestEWallet(BaseIntegrationTest):
    @pytest.fixture
    def EWallet(self, xendit_instance):
        return xendit_instance.EWallet

    def test_create_ovo_payment_return_correct_keys(self, EWallet):
        ovo_payment = EWallet.create_ovo_payment(
            f"ovo-ewallet-testing-id-{int(time.time())}", "8888", "08123123123"
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            ovo_payment, ovo_payment_response()
        )

    def test_create_dana_payment_return_correct_keys(self, EWallet):
        dana_payment = EWallet.create_dana_payment(
            f"dana-ewallet-test-{time.time()}",
            "1001",
            "https://my-shop.com/callbacks",
            "https://my-shop.com/home",
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            dana_payment, dana_payment_response()
        )

    def test_create_linkaja_payment_return_correct_keys(self, EWallet):
        items = []
        items.append(
            xendit.LinkAjaItem(id="123123", name="Phone Case", price=100000, quantity=1)
        )
        linkaja_payment = EWallet.create_linkaja_payment(
            f"linkaja-ewallet-test-{time.time()}",
            "089911111111",
            300000,
            items,
            "https://my-shop.com/callbacks",
            "https://xendit.co/",
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            linkaja_payment, linkaja_payment_response()
        )

    def test_get_ovo_payment_status_return_correct_keys(self, EWallet):
        ewallet = EWallet.get_payment_status(
            "ovo-ewallet-testing-id-1234", EWalletType.OVO
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            ewallet, ovo_payment_status_response()
        )

    def test_get_dana_payment_return_correct_keys(self, EWallet):
        ewallet = EWallet.get_payment_status("dana-ewallet-test-1234", EWalletType.DANA)
        self.assert_returned_object_has_same_key_as_sample_response(
            ewallet, dana_payment_status_response()
        )

    def test_get_completed_linkaja_payment_status_return_correct_keys(self, EWallet):
        ewallet = EWallet.get_payment_status(
            "linkaja-ewallet-test-1234", EWalletType.LINKAJA
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            ewallet, linkaja_payment_status_completed_response()
        )

    def test_get_failed_linkaja_payment_status_return_correct_keys(self, EWallet):
        ewallet = EWallet.get_payment_status(
            "linkaja-ewallet-test-123", EWalletType.LINKAJA
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            ewallet, linkaja_payment_status_expired_response()
        )
