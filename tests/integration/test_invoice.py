import pytest

from .base_integration_test import BaseIntegrationTest
from tests.sampleresponse.invoice import invoice_response
from tests.sampleresponse.invoice import multiple_invoice_response


class TestInvoice(BaseIntegrationTest):
    @pytest.fixture
    def Invoice(self, xendit_instance):
        return xendit_instance.Invoice

    def test_create_and_get_and_expire_invoice_return_correct_keys(self, Invoice):
        invoice = Invoice.create(
            external_id="invoice-1593766262",
            amount=20000,
            payer_email="customer@domain.com",
            description="Invoice Demo #123",
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            invoice, invoice_response()
        )
        invoice_id = invoice.id

        invoice = Invoice.get(invoice_id=invoice_id,)
        self.assert_returned_object_has_same_key_as_sample_response(
            invoice, invoice_response()
        )

        invoice = Invoice.expire(invoice_id=invoice_id,)
        self.assert_returned_object_has_same_key_as_sample_response(
            invoice, invoice_response()
        )

    def test_list_all_invoice_return_correct_keys(self, Invoice):
        invoices = Invoice.list_all(limit=3,)
        self.assert_returned_object_has_same_key_as_sample_response(
            invoices[0], multiple_invoice_response()[0]
        )
