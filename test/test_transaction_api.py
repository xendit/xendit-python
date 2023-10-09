"""
    The version of the XENDIT API: 3.4.3
"""


import unittest

import xendit
from balance_and_transaction.transaction_api import TransactionApi  # noqa: E501


class TestTransactionApi(unittest.TestCase):
    """TransactionApi unit test stubs"""

    def setUp(self):
        self.api = TransactionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all_transactions(self):
        """Test case for get_all_transactions

        Get a list of transactions  # noqa: E501
        """
        pass

    def test_get_transaction_by_id(self):
        """Test case for get_transaction_by_id

        Get a transaction based on its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
