"""
    The version of the XENDIT API: 1.4.2
"""


import sys
import unittest

import xendit
from xendit.invoice.model.bank_code import BankCode
globals()['BankCode'] = BankCode
from xendit.invoice.model.bank import Bank


class TestBank(unittest.TestCase):
    """Bank unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBank(self):
        """Test Bank"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Bank()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
