import pytest
from tests.sampleresponse.payment_method import payment_method_response
from xendit.models.paymentmethod.card.card import Card
from xendit.models.paymentmethod.card.card_information import \
    CardInformation
from xendit.models.paymentmethod.card.channel_properties import \
    ChannelProperties as CardChannelProperties
from xendit.models.paymentmethod.direct_debit.channel_properties import \
    ChannelProperties as DirectDebitChannelProperties
from xendit.models.paymentmethod.direct_debit.direct_debit import \
    DirectDebit
from xendit.models.paymentmethod.ewallet.channel_properties import \
    ChannelProperties as EWalletChannelProperties
from xendit.models.paymentmethod.ewallet.ewallet import EWallet
from xendit.models.paymentmethod.over_the_counter.channel_properties import \
    ChannelProperties as OTCChannelProperties
from xendit.models.paymentmethod.over_the_counter.over_the_counter import \
    OverTheCounter
from xendit.models.paymentmethod.qr_code.qr_code import QRCode
from xendit.models.paymentmethod.virtual_account.channel_properties import \
    ChannelProperties as VAChannelProperties
from xendit.models.paymentmethod.virtual_account.virtual_account import \
    VirtualAccount

from .base_integration_test import BaseIntegrationTest


class TestPaymentMethod(BaseIntegrationTest):
    @pytest.fixture
    def PaymentMethod(self, xendit_instance):
        return xendit_instance.PaymentMethod

    def test_get_return_correct_keys(self, PaymentMethod):
        payment_method = PaymentMethod.get(payment_method_id="pm-1c229762-c21a-433d-8da5-f02240387e34")
        self.assert_returned_object_has_same_key_as_sample_response(
            payment_method, payment_method_response()
        )
    
    def test_create_ewallet_return_correct_keys(self, PaymentMethod):
        payment_method = PaymentMethod.create(
            type="EWALLET",
            reusability="ONE_TIME_USE",
            ewallet=EWallet.Query(
                channel_code="PAYMAYA",
                channel_properties=EWalletChannelProperties.Query(
                    cancel_return_url="https://redirect.me/nostuff",
                    failure_return_url="https://redirect.me/badstuff",
                    success_return_url="https://redirect.me/goodstuff"
                )
            )
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            payment_method, payment_method_response()
        )

    def test_create_direct_debit_return_correct_keys(self, PaymentMethod):
        payment_method = PaymentMethod.create(
            type="DIRECT_DEBIT",
            reusability="MULTIPLE_USE",
            customer_id="1c320af8-5b4b-45f8-bffa-9caeacada3a1",
            direct_debit=DirectDebit.Query(
                channel_code="BPI",
                channel_properties=DirectDebitChannelProperties.Query(
                    failure_return_url="https://redirect.me/badstuff",
                    success_return_url="https://redirect.me/goodstuff"
                )
            )
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            payment_method, payment_method_response()
        )

    def test_create_card_return_correct_keys(self, PaymentMethod):
        payment_method = PaymentMethod.create(
            type="CARD",
            reusability="MULTIPLE_USE",
            card=Card.Query(
                currency="PHP",
                card_information=CardInformation.Query(
                    card_number="4000000000000002",
                    expiry_month="12",
                    expiry_year="2040"
                ),
                channel_properties=CardChannelProperties.Query(
                    failure_return_url="https://redirect.me/badstuff",
                    success_return_url="https://redirect.me/goodstuff"
                )
            )
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            payment_method, payment_method_response()
        )

    def test_create_card_return_correct_keys(self, PaymentMethod):
        payment_method = PaymentMethod.create(
            type="CARD",
            reusability="MULTIPLE_USE",
            card=Card.Query(
                currency="PHP",
                card_information=CardInformation.Query(
                    card_number="4000000000000002",
                    expiry_month="12",
                    expiry_year="2040"
                ),
                channel_properties=CardChannelProperties.Query(
                    failure_return_url="https://redirect.me/badstuff",
                    success_return_url="https://redirect.me/goodstuff"
                )
            )
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            payment_method, payment_method_response()
        )

    def test_create_over_the_counter_return_correct_keys(self, PaymentMethod):
        payment_method = PaymentMethod.create(
            type="OVER_THE_COUNTER",
            reusability="ONE_TIME_USE",
            over_the_counter=OverTheCounter.Query(
                amount=50,
                currency="PHP",
                channel_code="7ELEVEN",
                channel_properties=OTCChannelProperties.Query(
                    customer_name="Test Customer"
                )
            )
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            payment_method, payment_method_response()
        )

    def test_create_qr_code_return_correct_keys(self, PaymentMethod):
        payment_method = PaymentMethod.create(
            type="QR_CODE",
            reusability="ONE_TIME_USE",
            qr_code=QRCode.Query(
                amount=50,
                currency="PHP",
                channel_code="RCBC",
            )
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            payment_method, payment_method_response()
        )

    def test_create_virtual_account_return_correct_keys(self, PaymentMethod):
        payment_method = PaymentMethod.create(
            type="VIRTUAL_ACCOUNT",
            reusability="MULTIPLE_USE",
            virtual_account=VirtualAccount.Query(
                channel_code="BCA",
                channel_properties=VAChannelProperties.Query(
                    customer_name="Test Customer"
                )
            )
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            payment_method, payment_method_response()
        )

    def test_update_return_correct_keys(self, PaymentMethod):
        payment_method = PaymentMethod.update(
            payment_method_id="pm-1c229762-c21a-433d-8da5-f02240387e34",
            status="INACTIVE"
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            payment_method, payment_method_response()
        )

    def test_expire_return_correct_keys(self, PaymentMethod):
        payment_method = PaymentMethod.create(
            type="EWALLET",
            reusability="ONE_TIME_USE",
            ewallet=EWallet.Query(
                channel_code="PAYMAYA",
                channel_properties=EWalletChannelProperties.Query(
                    cancel_return_url="https://redirect.me/nostuff",
                    failure_return_url="https://redirect.me/badstuff",
                    success_return_url="https://redirect.me/goodstuff"
                )
            )
        )

        expire_result = PaymentMethod.expire(
            payment_method_id=payment_method.id
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            payment_method, payment_method_response()
        )

    def test_list_return_correct_keys(self, PaymentMethod):
        payment_method_list = PaymentMethod.list(limit=5)

        for payment_method in payment_method_list.data:
            self.assert_returned_object_has_same_key_as_sample_response(
                payment_method, payment_method_response()
            )
