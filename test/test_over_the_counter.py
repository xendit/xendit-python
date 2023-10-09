"""
    The version of the XENDIT API: 2.89.1
"""


import sys
import unittest

import xendit
from xendit.payment_method.model.over_the_counter_channel_code import OverTheCounterChannelCode
from xendit.payment_method.model.over_the_counter_channel_properties import OverTheCounterChannelProperties
from xendit.payment_method.model.over_the_counter_parameters import OverTheCounterParameters
globals()['OverTheCounterChannelCode'] = OverTheCounterChannelCode
globals()['OverTheCounterChannelProperties'] = OverTheCounterChannelProperties
globals()['OverTheCounterParameters'] = OverTheCounterParameters
from xendit.payment_method.model.over_the_counter import OverTheCounter


class TestOverTheCounter(unittest.TestCase):
    """OverTheCounter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOverTheCounter(self):
        """Test OverTheCounter"""
        # FIXME: construct object with mandatory attributes with example values
        # model = OverTheCounter()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
