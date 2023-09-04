"""
    The version of the XENDIT API: 1.0.0
"""


import sys
import unittest

import xendit
from xendit.payout.model.channel_account_type import ChannelAccountType
globals()['ChannelAccountType'] = ChannelAccountType
from xendit.payout.model.digital_payout_channel_properties import DigitalPayoutChannelProperties


class TestDigitalPayoutChannelProperties(unittest.TestCase):
    """DigitalPayoutChannelProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDigitalPayoutChannelProperties(self):
        """Test DigitalPayoutChannelProperties"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DigitalPayoutChannelProperties()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
