"""
    The version of the XENDIT API: 1.42.3
"""


import sys
import unittest

import xendit
from xendit.payment_request.model.e_wallet_account import EWalletAccount
from xendit.payment_request.model.e_wallet_all_of import EWalletAllOf
from xendit.payment_request.model.e_wallet_channel_code import EWalletChannelCode
from xendit.payment_request.model.e_wallet_channel_properties import EWalletChannelProperties
from xendit.payment_request.model.e_wallet_parameters import EWalletParameters
globals()['EWalletAccount'] = EWalletAccount
globals()['EWalletAllOf'] = EWalletAllOf
globals()['EWalletChannelCode'] = EWalletChannelCode
globals()['EWalletChannelProperties'] = EWalletChannelProperties
globals()['EWalletParameters'] = EWalletParameters
from xendit.payment_request.model.e_wallet import EWallet


class TestEWallet(unittest.TestCase):
    """EWallet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEWallet(self):
        """Test EWallet"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EWallet()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
