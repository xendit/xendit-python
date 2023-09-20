"""
    The version of the XENDIT API: 2.87.2
"""


import sys
import unittest

import xendit
from xendit.payment_method.model.channel_amount_limits import ChannelAmountLimits
from xendit.payment_method.model.channel_property import ChannelProperty
globals()['ChannelAmountLimits'] = ChannelAmountLimits
globals()['ChannelProperty'] = ChannelProperty
from xendit.payment_method.model.payment_channel_all_of import PaymentChannelAllOf


class TestPaymentChannelAllOf(unittest.TestCase):
    """PaymentChannelAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentChannelAllOf(self):
        """Test PaymentChannelAllOf"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaymentChannelAllOf()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
