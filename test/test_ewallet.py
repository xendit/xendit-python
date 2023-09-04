"""
    The version of the XENDIT API: 1.4.2
"""


import sys
import unittest

import xendit
from xendit.invoice.model.ewallet_type import EwalletType
globals()['EwalletType'] = EwalletType
from xendit.invoice.model.ewallet import Ewallet


class TestEwallet(unittest.TestCase):
    """Ewallet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEwallet(self):
        """Test Ewallet"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Ewallet()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
