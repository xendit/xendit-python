"""
    The version of the XENDIT API: 1.4.2
"""


import sys
import unittest

import xendit
from xendit.invoice.model.customer_object import CustomerObject
from xendit.invoice.model.invoice_fee import InvoiceFee
from xendit.invoice.model.invoice_item import InvoiceItem
from xendit.invoice.model.notification_preference import NotificationPreference
globals()['CustomerObject'] = CustomerObject
globals()['InvoiceFee'] = InvoiceFee
globals()['InvoiceItem'] = InvoiceItem
globals()['NotificationPreference'] = NotificationPreference
from xendit.invoice.model.create_invoice_request import CreateInvoiceRequest


class TestCreateInvoiceRequest(unittest.TestCase):
    """CreateInvoiceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateInvoiceRequest(self):
        """Test CreateInvoiceRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CreateInvoiceRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
