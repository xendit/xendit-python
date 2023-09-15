"""
    The version of the XENDIT API: 2.87.2
"""


import sys
import unittest

import xendit
from xendit.payment_method.model.channel_property_all_of import ChannelPropertyAllOf
globals()['ChannelPropertyAllOf'] = ChannelPropertyAllOf
from xendit.payment_method.model.channel_property import ChannelProperty


class TestChannelProperty(unittest.TestCase):
    """ChannelProperty unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testChannelProperty(self):
        """Test ChannelProperty"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ChannelProperty()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
