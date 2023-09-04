"""
    The version of the XENDIT API: 2.86.1
"""


import sys
import unittest

import xendit
from xendit.payment_method.model.over_the_counter_channel_code import OverTheCounterChannelCode
from xendit.payment_method.model.over_the_counter_channel_properties import OverTheCounterChannelProperties
globals()['OverTheCounterChannelCode'] = OverTheCounterChannelCode
globals()['OverTheCounterChannelProperties'] = OverTheCounterChannelProperties
from xendit.payment_method.model.over_the_counter_parameters import OverTheCounterParameters


class TestOverTheCounterParameters(unittest.TestCase):
    """OverTheCounterParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOverTheCounterParameters(self):
        """Test OverTheCounterParameters"""
        # FIXME: construct object with mandatory attributes with example values
        # model = OverTheCounterParameters()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
