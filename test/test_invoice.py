"""
    The version of the XENDIT API: 1.5.0
"""


import sys
import unittest

import xendit
from xendit.invoice.model.bank import Bank
from xendit.invoice.model.customer_object import CustomerObject
from xendit.invoice.model.direct_debit import DirectDebit
from xendit.invoice.model.ewallet import Ewallet
from xendit.invoice.model.invoice_currency import InvoiceCurrency
from xendit.invoice.model.invoice_fee import InvoiceFee
from xendit.invoice.model.invoice_item import InvoiceItem
from xendit.invoice.model.invoice_payment_method import InvoicePaymentMethod
from xendit.invoice.model.invoice_status import InvoiceStatus
from xendit.invoice.model.notification_preference import NotificationPreference
from xendit.invoice.model.paylater import Paylater
from xendit.invoice.model.qr_code import QrCode
from xendit.invoice.model.retail_outlet import RetailOutlet
globals()['Bank'] = Bank
globals()['CustomerObject'] = CustomerObject
globals()['DirectDebit'] = DirectDebit
globals()['Ewallet'] = Ewallet
globals()['InvoiceCurrency'] = InvoiceCurrency
globals()['InvoiceFee'] = InvoiceFee
globals()['InvoiceItem'] = InvoiceItem
globals()['InvoicePaymentMethod'] = InvoicePaymentMethod
globals()['InvoiceStatus'] = InvoiceStatus
globals()['NotificationPreference'] = NotificationPreference
globals()['Paylater'] = Paylater
globals()['QrCode'] = QrCode
globals()['RetailOutlet'] = RetailOutlet
from xendit.invoice.model.invoice import Invoice


class TestInvoice(unittest.TestCase):
    """Invoice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInvoice(self):
        """Test Invoice"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Invoice()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
