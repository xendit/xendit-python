"""
    The version of the XENDIT API: 1.0.0
"""


import sys
import unittest

import xendit
from xendit.customer.model.country_code import CountryCode
from xendit.customer.model.identity_account_response_properties import IdentityAccountResponseProperties
globals()['CountryCode'] = CountryCode
globals()['IdentityAccountResponseProperties'] = IdentityAccountResponseProperties
from xendit.customer.model.identity_account_response import IdentityAccountResponse


class TestIdentityAccountResponse(unittest.TestCase):
    """IdentityAccountResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIdentityAccountResponse(self):
        """Test IdentityAccountResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IdentityAccountResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
