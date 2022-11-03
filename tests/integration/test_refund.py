import pytest
from tests.sampleresponse.refund import refund_response
from xendit.models.paymentmethod.ewallet.channel_properties import \
    ChannelProperties as EWalletChannelProperties
from xendit.models.paymentmethod.ewallet.ewallet import EWallet
from xendit.models.paymentmethod import PaymentMethod
from .base_integration_test import BaseIntegrationTest


class TestRefund(BaseIntegrationTest):
    @pytest.fixture
    def Refund(self, xendit_instance):
        return xendit_instance.Refund

    def test_get_return_correct_keys(self, Refund):
        refund = Refund.get(refund_id ="rfd-48fd6af8-9cf3-471d-9f37-f6d27a829220")
        self.assert_returned_object_has_same_key_as_sample_response(
            refund, refund_response()
        )

    def test_list_return_correct_keys(self, Refund):
        refund_list = Refund.list(limit=5)

        for refund in refund_list.data:
            self.assert_returned_object_has_same_key_as_sample_response(
                refund, refund_response()
            )
