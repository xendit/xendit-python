"""
    The version of the XENDIT API: 1.41.0
"""


import sys
import unittest

import xendit
from xendit.payment_request.model.e_wallet_account import EWalletAccount
globals()['EWalletAccount'] = EWalletAccount
from xendit.payment_request.model.e_wallet_all_of import EWalletAllOf


class TestEWalletAllOf(unittest.TestCase):
    """EWalletAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEWalletAllOf(self):
        """Test EWalletAllOf"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EWalletAllOf()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
