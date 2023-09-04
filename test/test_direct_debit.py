"""
    The version of the XENDIT API: 1.4.2
"""


import sys
import unittest

import xendit
from xendit.invoice.model.direct_debit_type import DirectDebitType
globals()['DirectDebitType'] = DirectDebitType
from xendit.invoice.model.direct_debit import DirectDebit


class TestDirectDebit(unittest.TestCase):
    """DirectDebit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDirectDebit(self):
        """Test DirectDebit"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DirectDebit()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
