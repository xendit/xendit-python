"""
    The version of the XENDIT API: 1.0.0
"""


import sys
import unittest

import xendit
from xendit.customer.model.address_status import AddressStatus
globals()['AddressStatus'] = AddressStatus
from xendit.customer.model.address import Address


class TestAddress(unittest.TestCase):
    """Address unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAddress(self):
        """Test Address"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Address()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
