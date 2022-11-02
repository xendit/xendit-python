import pytest
from tests.sampleresponse.payment_request import payment_request_response
from xendit.models.paymentmethod.ewallet.channel_properties import \
    ChannelProperties as EWalletChannelProperties
from xendit.models.paymentmethod.ewallet.ewallet import EWallet
from xendit.models.paymentmethod import PaymentMethod
from .base_integration_test import BaseIntegrationTest


class TestPaymentRequest(BaseIntegrationTest):
    @pytest.fixture
    def PaymentRequest(self, xendit_instance):
        return xendit_instance.PaymentRequest

    def test_get_return_correct_keys(self, PaymentRequest):
        payment_request = PaymentRequest.get(payment_request_id ="ewc_f02159c3-1e52-48a4-974f-243d906a5da3")
        self.assert_returned_object_has_same_key_as_sample_response(
            payment_request, payment_request_response()
        )
    
    # def test_create_paymereturn_correct_keys(self, xendit_instance):
        
    #     payment_request = xendit_instance.PaymentRequest.create(
    #         amount=1500,
    #         currency="IDR",
    #         payment_method=PaymentMethod.Query(
    #             type="EWALLET",
    #             reusability="ONE_TIME_USE",
    #             ewallet=EWallet.Query(
    #                 channel_code="OVO",
    #                 channel_properties=EWalletChannelProperties.Query(
    #                     mobile_number="+628123123123"
    #                 )
    #             )
    #         )
    #     )
 
    #     self.assert_returned_object_has_same_key_as_sample_response(
    #         payment_request, payment_request_response()
    #     )

    def test_list_return_correct_keys(self, PaymentRequest):
        payment_request_list = PaymentRequest.list(limit=5)

        for payment_request in payment_request_list.data:
            self.assert_returned_object_has_same_key_as_sample_response(
                payment_request, payment_request_response()
            )
