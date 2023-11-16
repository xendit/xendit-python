"""
    The version of the XENDIT API: 3.5.0
"""


import sys
import unittest

import xendit
from xendit.balance_and_transaction.model.transaction_types import TransactionTypes
globals()['TransactionTypes'] = TransactionTypes
from xendit.balance_and_transaction.model.transaction_response_type import TransactionResponseType


class TestTransactionResponseType(unittest.TestCase):
    """TransactionResponseType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTransactionResponseType(self):
        """Test TransactionResponseType"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TransactionResponseType()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
