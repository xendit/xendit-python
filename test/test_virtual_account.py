"""
    The version of the XENDIT API: 2.89.1
"""


import sys
import unittest

import xendit
from xendit.payment_method.model.virtual_account_all_of import VirtualAccountAllOf
from xendit.payment_method.model.virtual_account_alternative_display import VirtualAccountAlternativeDisplay
from xendit.payment_method.model.virtual_account_channel_code import VirtualAccountChannelCode
from xendit.payment_method.model.virtual_account_channel_properties import VirtualAccountChannelProperties
from xendit.payment_method.model.virtual_account_parameters import VirtualAccountParameters
globals()['VirtualAccountAllOf'] = VirtualAccountAllOf
globals()['VirtualAccountAlternativeDisplay'] = VirtualAccountAlternativeDisplay
globals()['VirtualAccountChannelCode'] = VirtualAccountChannelCode
globals()['VirtualAccountChannelProperties'] = VirtualAccountChannelProperties
globals()['VirtualAccountParameters'] = VirtualAccountParameters
from xendit.payment_method.model.virtual_account import VirtualAccount


class TestVirtualAccount(unittest.TestCase):
    """VirtualAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVirtualAccount(self):
        """Test VirtualAccount"""
        # FIXME: construct object with mandatory attributes with example values
        # model = VirtualAccount()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
