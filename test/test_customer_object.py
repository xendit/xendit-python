"""
    The version of the XENDIT API: 1.5.0
"""


import sys
import unittest

import xendit
from xendit.invoice.model.address_object import AddressObject
globals()['AddressObject'] = AddressObject
from xendit.invoice.model.customer_object import CustomerObject


class TestCustomerObject(unittest.TestCase):
    """CustomerObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomerObject(self):
        """Test CustomerObject"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CustomerObject()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
