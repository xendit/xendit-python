import pytest
import time

from .base_integration_test import BaseIntegrationTest
from tests.sampleresponse.direct_debit import (
    customer_response,
    multi_customer_response,
    linked_account_response,
    accessible_account_response,
)


class TestDirectDebit(BaseIntegrationTest):
    @pytest.fixture
    def DirectDebit(self, xendit_instance):
        return xendit_instance.DirectDebit

    def test_create_customer_return_correct_keys(self, DirectDebit):
        customer = DirectDebit.create_customer(
            reference_id=f"merc-{int(time.time())}",
            email="t@x.co",
            given_names="Adyaksa",
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            customer, customer_response()
        )

    @pytest.mark.skip(reason="Currently not implemented by Direct Debit")
    def test_get_customer_by_ref_id_return_correct_keys(self, DirectDebit):
        customer = DirectDebit.get_customer_by_ref_id(reference_id="merc-1594272368",)
        self.assert_returned_object_has_same_key_as_sample_response(
            customer[0], multi_customer_response()
        )

    def test_linked_account_token_scheme_return_correct_keys(self, DirectDebit):
        linked_account_token = DirectDebit.initialize_tokenization(
            customer_id="ed20b5db-df04-41fc-8018-8ea4ac4d1030",
            channel_code="DC_BRI",
            properties={
                "account_mobile_number": "+62818555988",
                "card_last_four": "8888",
                "card_expiry": "06/24",
                "account_email": "test.email@xendit.co",
            },
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            linked_account_token, linked_account_response()
        )

        validated_linked_account_token = DirectDebit.validate_token_otp(
            linked_account_token_id=linked_account_token.id, otp_code="333000",
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            validated_linked_account_token, linked_account_response()
        )

        accessible_accounts = DirectDebit.get_accessible_account_by_token(
            linked_account_token_id=validated_linked_account_token.id
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            accessible_accounts[0], accessible_account_response()[0]
        )
