"""
    The version of the XENDIT API: 2.86.1
"""


import sys
import unittest

import xendit
from xendit.payment_method.model.over_the_counter_channel_properties_update import OverTheCounterChannelPropertiesUpdate
globals()['OverTheCounterChannelPropertiesUpdate'] = OverTheCounterChannelPropertiesUpdate
from xendit.payment_method.model.over_the_counter_update_parameters import OverTheCounterUpdateParameters


class TestOverTheCounterUpdateParameters(unittest.TestCase):
    """OverTheCounterUpdateParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOverTheCounterUpdateParameters(self):
        """Test OverTheCounterUpdateParameters"""
        # FIXME: construct object with mandatory attributes with example values
        # model = OverTheCounterUpdateParameters()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
