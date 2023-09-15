"""
    The version of the XENDIT API: 1.5.0
"""


import unittest

import xendit
from invoice.invoice_api import InvoiceApi  # noqa: E501


class TestInvoiceApi(unittest.TestCase):
    """InvoiceApi unit test stubs"""

    def setUp(self):
        self.api = InvoiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_invoice(self):
        """Test case for create_invoice

        Create an invoice  # noqa: E501
        """
        pass

    def test_expire_invoice(self):
        """Test case for expire_invoice

        Manually expire an invoice  # noqa: E501
        """
        pass

    def test_get_invoice_by_id(self):
        """Test case for get_invoice_by_id

        Get invoice by invoice id  # noqa: E501
        """
        pass

    def test_get_invoices(self):
        """Test case for get_invoices

        Get all Invoices  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
