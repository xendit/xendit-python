"""
    The version of the XENDIT API: 1.0.0
"""


import sys
import unittest

import xendit
from xendit.customer.model.country_code import CountryCode
globals()['CountryCode'] = CountryCode
from xendit.customer.model.business_detail import BusinessDetail


class TestBusinessDetail(unittest.TestCase):
    """BusinessDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBusinessDetail(self):
        """Test BusinessDetail"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BusinessDetail()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
