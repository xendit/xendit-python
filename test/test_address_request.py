"""
    The version of the XENDIT API: 1.0.0
"""


import sys
import unittest

import xendit
from xendit.customer.model.address_status import AddressStatus
from xendit.customer.model.country_code import CountryCode
globals()['AddressStatus'] = AddressStatus
globals()['CountryCode'] = CountryCode
from xendit.customer.model.address_request import AddressRequest


class TestAddressRequest(unittest.TestCase):
    """AddressRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAddressRequest(self):
        """Test AddressRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AddressRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
