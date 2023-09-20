"""
    The version of the XENDIT API: 2.87.2
"""


import sys
import unittest

import xendit
from xendit.payment_method.model.channel_amount_limits_all_of import ChannelAmountLimitsAllOf
globals()['ChannelAmountLimitsAllOf'] = ChannelAmountLimitsAllOf
from xendit.payment_method.model.channel_amount_limits import ChannelAmountLimits


class TestChannelAmountLimits(unittest.TestCase):
    """ChannelAmountLimits unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testChannelAmountLimits(self):
        """Test ChannelAmountLimits"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ChannelAmountLimits()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
