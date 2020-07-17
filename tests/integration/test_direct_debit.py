import pytest
import time

from .base_integration_test import BaseIntegrationTest
from tests.sampleresponse.direct_debit import (
    customer_response,
    multi_customer_response,
    linked_account_response,
    accessible_accounts_response,
    payment_method_response,
    multi_payment_method_response,
    payment_response,
    multi_payment_response,
)

from xendit import DirectDebitPaymentMethodType


class TestDirectDebit(BaseIntegrationTest):
    @pytest.fixture(scope="class")
    def DirectDebit(self, xendit_instance):
        return xendit_instance.DirectDebit

    @pytest.fixture(scope="class")
    def customer_data(self, DirectDebit):
        customer = DirectDebit.create_customer(
            reference_id=f"merc-{int(time.time())}",
            email="t@x.co",
            given_names="Adyaksa",
        )
        return customer

    @pytest.fixture(scope="class")
    def linked_account_data(self, DirectDebit, customer_data):
        customer = customer_data
        linked_account_token = DirectDebit.initialize_tokenization(
            customer_id=customer.id,
            channel_code="DC_BRI",
            properties={
                "account_mobile_number": "+62818555988",
                "card_last_four": "8888",
                "card_expiry": "06/24",
                "account_email": "test.email@xendit.co",
            },
        )
        validated_linked_account_token = DirectDebit.validate_token_otp(
            linked_account_token_id=linked_account_token.id, otp_code="333000",
        )
        accessible_accounts = DirectDebit.get_accessible_accounts_by_token(
            linked_account_token_id=validated_linked_account_token.id
        )
        return linked_account_token, validated_linked_account_token, accessible_accounts

    @pytest.fixture(scope="class")
    def payment_method_data(self, DirectDebit, linked_account_data):
        linked_account_token, _, accessible_accounts = linked_account_data
        payment_method = DirectDebit.create_payment_method(
            customer_id=linked_account_token.customer_id,
            type=DirectDebitPaymentMethodType.DEBIT_CARD,
            properties={"id": accessible_accounts[0].id},
        )
        return payment_method

    @pytest.fixture(scope="class")
    def payment_data(self, DirectDebit, payment_method_data):
        payment_method = payment_method_data
        payment = DirectDebit.create_payment(
            reference_id=f"direct-debit-ref-{int(time.time())}",
            payment_method_id=payment_method.id,
            currency="IDR",
            amount="60000",
            callback_url="http://webhook.site/",
            enable_otp=True,
            idempotency_key=f"idemp_key-{int(time.time())}",
        )
        return payment

    def test_create_customer_return_correct_keys(self, customer_data):
        customer = customer_data
        self.assert_returned_object_has_same_key_as_sample_response(
            customer, customer_response()
        )

    @pytest.mark.skip(reason="Currently not implemented by Direct Debit")
    def test_get_customer_by_ref_id_return_correct_keys(
        self, DirectDebit, customer_data
    ):
        customer = customer_data

        tested_customer = DirectDebit.get_customer_by_ref_id(
            reference_id=customer.reference_id,
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            tested_customer[0], multi_customer_response()
        )

    def test_linked_account_token_scheme_return_correct_keys(self, linked_account_data):
        (
            linked_account_token,
            validated_linked_account_token,
            accessible_accounts,
        ) = linked_account_data

        self.assert_returned_object_has_same_key_as_sample_response(
            linked_account_token, linked_account_response()
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            validated_linked_account_token, linked_account_response()
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            accessible_accounts[0], accessible_accounts_response()[0]
        )

    def test_create_payment_method_return_correct_keys(
        self, DirectDebit, payment_method_data
    ):
        payment_method = payment_method_data

        self.assert_returned_object_has_same_key_as_sample_response(
            payment_method, payment_method_response()
        )

    def test_get_payment_methods_by_ref_id_return_correct_keys(
        self, DirectDebit, customer_data
    ):
        customer = customer_data

        payment_methods = DirectDebit.get_payment_methods_by_customer_id(
            customer_id=customer.id,
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            payment_methods[0], multi_payment_method_response()[0]
        )

    def test_create_payment_return_correct_keys(self, payment_data):
        payment = payment_data
        self.assert_returned_object_has_same_key_as_sample_response(
            payment, payment_response()
        )

    def test_validate_payment_otp_return_correct_keys(self, DirectDebit, payment_data):
        payment = payment_data

        validated_payment = DirectDebit.validate_payment_otp(
            direct_debit_id=payment.id, otp_code="222000",
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            validated_payment, payment_response()
        )

    def test_get_payment_status_return_correct_keys(self, DirectDebit, payment_data):
        payment = payment_data

        payment = DirectDebit.get_payment_status(direct_debit_id=payment.id)

        self.assert_returned_object_has_same_key_as_sample_response(
            payment, payment_response()
        )

    def test_get_payment_status_by_ref_id_return_correct_keys(
        self, DirectDebit, payment_data
    ):
        payment = payment_data

        payments = DirectDebit.get_payment_status_by_ref_id(
            reference_id=payment.reference_id
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            payments[0], multi_payment_response()[0]
        )
