"""
    The version of the XENDIT API: 2.89.2
"""


import sys
import unittest

import xendit
from xendit.payment_method.model.virtual_account_channel_properties_patch import VirtualAccountChannelPropertiesPatch
globals()['VirtualAccountChannelPropertiesPatch'] = VirtualAccountChannelPropertiesPatch
from xendit.payment_method.model.virtual_account_update_parameters import VirtualAccountUpdateParameters


class TestVirtualAccountUpdateParameters(unittest.TestCase):
    """VirtualAccountUpdateParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVirtualAccountUpdateParameters(self):
        """Test VirtualAccountUpdateParameters"""
        # FIXME: construct object with mandatory attributes with example values
        # model = VirtualAccountUpdateParameters()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
