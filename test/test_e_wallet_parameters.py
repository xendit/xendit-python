"""
    The version of the XENDIT API: 2.89.1
"""


import sys
import unittest

import xendit
from xendit.payment_method.model.e_wallet_account import EWalletAccount
from xendit.payment_method.model.e_wallet_channel_code import EWalletChannelCode
from xendit.payment_method.model.e_wallet_channel_properties import EWalletChannelProperties
globals()['EWalletAccount'] = EWalletAccount
globals()['EWalletChannelCode'] = EWalletChannelCode
globals()['EWalletChannelProperties'] = EWalletChannelProperties
from xendit.payment_method.model.e_wallet_parameters import EWalletParameters


class TestEWalletParameters(unittest.TestCase):
    """EWalletParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEWalletParameters(self):
        """Test EWalletParameters"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EWalletParameters()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
