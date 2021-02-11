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
from tests.sampleresponse.ewallet import ewallet_charge_response


class TestEWallet(BaseIntegrationTest):
    @pytest.fixture(scope="class")
    def EWallet(self, xendit_instance):
        return xendit_instance.EWallet

    @pytest.fixture(scope="class")
    def ovo_payment_data(self, EWallet):
        ovo_payment = EWallet.create_ovo_payment(
            external_id=f"ovo-ewallet-testing-id-{int(time.time())}",
            amount="80001",
            phone="08123123123",
        )
        return ovo_payment

    @pytest.fixture(scope="class")
    def dana_payment_data(self, EWallet):
        dana_payment = EWallet.create_dana_payment(
            external_id=f"dana-ewallet-test-{time.time()}",
            amount="1001",
            callback_url="https://my-shop.com/callbacks",
            redirect_url="https://my-shop.com/home",
        )
        return dana_payment

    @pytest.fixture(scope="class")
    def linkaja_payment_data(self, EWallet):
        # Object Creation Test
        items = []
        item = xendit.EWallet.helper_create_linkaja_item(
            id="123123", name="Phone Case", price=100000, quantity=1
        )
        items.append(item)

        linkaja_payment = EWallet.create_linkaja_payment(
            external_id=f"linkaja-ewallet-test-{time.time()}",
            phone="089911111111",
            amount=300000,
            items=items,
            callback_url="https://my-shop.com/callbacks",
            redirect_url="https://xendit.co/",
        )
        return linkaja_payment

    def test_create_ovo_payment_return_correct_keys(self, ovo_payment_data):
        ovo_payment = ovo_payment_data

        self.assert_returned_object_has_same_key_as_sample_response(
            ovo_payment, ovo_payment_response()
        )

    def test_create_dana_payment_return_correct_keys(self, dana_payment_data):
        dana_payment = dana_payment_data
        self.assert_returned_object_has_same_key_as_sample_response(
            dana_payment, dana_payment_response()
        )

    def test_create_linkaja_payment_return_correct_keys(self, linkaja_payment_data):
        linkaja_payment = linkaja_payment_data
        self.assert_returned_object_has_same_key_as_sample_response(
            linkaja_payment, linkaja_payment_response()
        )

    def test_get_ovo_payment_status_return_correct_keys(
        self, EWallet, ovo_payment_data
    ):
        ovo_payment = ovo_payment_data

        ewallet = EWallet.get_payment_status(
            external_id=ovo_payment.external_id, ewallet_type=EWalletType.OVO,
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            ewallet, ovo_payment_status_response()
        )

    def test_get_dana_payment_return_correct_keys(self, EWallet, dana_payment_data):
        dana_payment = dana_payment_data
        ewallet = EWallet.get_payment_status(
            external_id=dana_payment.external_id, ewallet_type=EWalletType.DANA,
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            ewallet, dana_payment_status_response()
        )

    def test_get_completed_linkaja_payment_status_return_correct_keys(self, EWallet):
        ewallet = EWallet.get_payment_status(
            external_id="linkaja-ewallet-test-1234", ewallet_type=EWalletType.LINKAJA,
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            ewallet, linkaja_payment_status_completed_response()
        )

    def test_get_failed_linkaja_payment_status_return_correct_keys(self, EWallet):
        ewallet = EWallet.get_payment_status(
            external_id="linkaja-ewallet-test-123", ewallet_type=EWalletType.LINKAJA,
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            ewallet, linkaja_payment_status_expired_response()
        )

    @pytest.fixture(scope="class")
    def ewallet_charge_data(self, EWallet):
        # Object Creation Test
        basket = []
        basket_item = EWallet.helper_create_basket_item(
            reference_id="basket-product-ref-id",
            name="product_name",
            category="mechanics",
            currency="IDR",
            price=50000,
            quantity=5,
            type="wht",
            sub_category="evr",
            metadata={
                "meta": "data"
            }
        )
        basket.append(basket_item)

        ewallet_charge = EWallet.create_ewallet_charge(
            reference_id="basket-product-ref-id",
            currency="IDR",
            amount=1688,
            checkout_method="ONE_TIME_PAYMENT",
            channel_code="ID_SHOPEEPAY",
            channel_properties={
                "success_redirect_url": "https://yourwebsite.com/order/123",
            },
            basket=basket,
            metadata={
                "meta2": "data2",
            },
        )
        return ewallet_charge

    def test_create_ewallet_charge_return_correct_keys(self, ewallet_charge_data):
        ewallet_charge = ewallet_charge_data

        self.assert_returned_object_has_same_key_as_sample_response(
            ewallet_charge, ewallet_charge_response()
        )

    def test_get_ewallet_charge_status_return_correct_keys(
        self, EWallet, ewallet_charge_data
    ):
        ewallet_charge = ewallet_charge_data

        ewallet_charge_status = EWallet.get_ewallet_charge_status(
            charge_id=ewallet_charge.id,
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            ewallet_charge_status, ewallet_charge_response()
        )
