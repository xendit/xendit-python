"""
    The version of the XENDIT API: 2.86.1
"""


import sys
import unittest

import xendit
from xendit.payment_method.model.payment_channel_list_links_inner_all_of import PaymentChannelListLinksInnerAllOf
globals()['PaymentChannelListLinksInnerAllOf'] = PaymentChannelListLinksInnerAllOf
from xendit.payment_method.model.payment_channel_list_links_inner import PaymentChannelListLinksInner


class TestPaymentChannelListLinksInner(unittest.TestCase):
    """PaymentChannelListLinksInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentChannelListLinksInner(self):
        """Test PaymentChannelListLinksInner"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaymentChannelListLinksInner()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
