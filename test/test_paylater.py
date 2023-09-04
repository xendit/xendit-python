"""
    The version of the XENDIT API: 1.4.2
"""


import sys
import unittest

import xendit
from xendit.invoice.model.paylater_type import PaylaterType
globals()['PaylaterType'] = PaylaterType
from xendit.invoice.model.paylater import Paylater


class TestPaylater(unittest.TestCase):
    """Paylater unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaylater(self):
        """Test Paylater"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Paylater()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
