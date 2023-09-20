"""
    The version of the XENDIT API: 1.42.3
"""


import sys
import unittest

import xendit
from xendit.payment_request.model.payment_request_currency import PaymentRequestCurrency
from xendit.payment_request.model.virtual_account_channel_code import VirtualAccountChannelCode
from xendit.payment_request.model.virtual_account_channel_properties import VirtualAccountChannelProperties
globals()['PaymentRequestCurrency'] = PaymentRequestCurrency
globals()['VirtualAccountChannelCode'] = VirtualAccountChannelCode
globals()['VirtualAccountChannelProperties'] = VirtualAccountChannelProperties
from xendit.payment_request.model.virtual_account_parameters import VirtualAccountParameters


class TestVirtualAccountParameters(unittest.TestCase):
    """VirtualAccountParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVirtualAccountParameters(self):
        """Test VirtualAccountParameters"""
        # FIXME: construct object with mandatory attributes with example values
        # model = VirtualAccountParameters()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
