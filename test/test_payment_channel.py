"""
    The version of the XENDIT API: 2.86.1
"""


import sys
import unittest

import xendit
from xendit.payment_method.model.channel_amount_limits import ChannelAmountLimits
from xendit.payment_method.model.channel_property import ChannelProperty
from xendit.payment_method.model.payment_channel_all_of import PaymentChannelAllOf
globals()['ChannelAmountLimits'] = ChannelAmountLimits
globals()['ChannelProperty'] = ChannelProperty
globals()['PaymentChannelAllOf'] = PaymentChannelAllOf
from xendit.payment_method.model.payment_channel import PaymentChannel


class TestPaymentChannel(unittest.TestCase):
    """PaymentChannel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentChannel(self):
        """Test PaymentChannel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaymentChannel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
