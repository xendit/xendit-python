"""
    The version of the XENDIT API: 1.0.0
"""


import sys
import unittest

import xendit
from xendit.customer.model.country_code import CountryCode
from xendit.customer.model.identity_account_request_properties import IdentityAccountRequestProperties
from xendit.customer.model.identity_account_type import IdentityAccountType
globals()['CountryCode'] = CountryCode
globals()['IdentityAccountRequestProperties'] = IdentityAccountRequestProperties
globals()['IdentityAccountType'] = IdentityAccountType
from xendit.customer.model.identity_account_request import IdentityAccountRequest


class TestIdentityAccountRequest(unittest.TestCase):
    """IdentityAccountRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIdentityAccountRequest(self):
        """Test IdentityAccountRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IdentityAccountRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
