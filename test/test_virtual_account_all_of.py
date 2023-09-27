"""
    The version of the XENDIT API: 1.44.0
"""


import sys
import unittest

import xendit
from xendit.payment_request.model.virtual_account_alternative_display import VirtualAccountAlternativeDisplay
globals()['VirtualAccountAlternativeDisplay'] = VirtualAccountAlternativeDisplay
from xendit.payment_request.model.virtual_account_all_of import VirtualAccountAllOf


class TestVirtualAccountAllOf(unittest.TestCase):
    """VirtualAccountAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVirtualAccountAllOf(self):
        """Test VirtualAccountAllOf"""
        # FIXME: construct object with mandatory attributes with example values
        # model = VirtualAccountAllOf()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
