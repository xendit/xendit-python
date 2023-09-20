"""
    The version of the XENDIT API: 1.0.0
"""


import sys
import unittest

import xendit
from xendit.payout.model.channel_amount_limits import ChannelAmountLimits
from xendit.payout.model.channel_category import ChannelCategory
globals()['ChannelAmountLimits'] = ChannelAmountLimits
globals()['ChannelCategory'] = ChannelCategory
from xendit.payout.model.channel import Channel


class TestChannel(unittest.TestCase):
    """Channel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testChannel(self):
        """Test Channel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Channel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
