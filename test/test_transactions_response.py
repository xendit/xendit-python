"""
    The version of the XENDIT API: 3.4.1
"""


import sys
import unittest

import xendit
from xendit.balance_and_transaction.model.link_item import LinkItem
from xendit.balance_and_transaction.model.transaction_response import TransactionResponse
globals()['LinkItem'] = LinkItem
globals()['TransactionResponse'] = TransactionResponse
from xendit.balance_and_transaction.model.transactions_response import TransactionsResponse


class TestTransactionsResponse(unittest.TestCase):
    """TransactionsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTransactionsResponse(self):
        """Test TransactionsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TransactionsResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
