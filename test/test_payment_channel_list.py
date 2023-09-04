"""
    The version of the XENDIT API: 2.86.1
"""


import sys
import unittest

import xendit
from xendit.payment_method.model.payment_channel import PaymentChannel
from xendit.payment_method.model.payment_channel_list_links_inner import PaymentChannelListLinksInner
globals()['PaymentChannel'] = PaymentChannel
globals()['PaymentChannelListLinksInner'] = PaymentChannelListLinksInner
from xendit.payment_method.model.payment_channel_list import PaymentChannelList


class TestPaymentChannelList(unittest.TestCase):
    """PaymentChannelList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentChannelList(self):
        """Test PaymentChannelList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaymentChannelList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
