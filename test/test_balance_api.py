"""
    The version of the XENDIT API: 3.4.1
"""


import unittest

import xendit
from balance_and_transaction.balance_api import BalanceApi  # noqa: E501


class TestBalanceApi(unittest.TestCase):
    """BalanceApi unit test stubs"""

    def setUp(self):
        self.api = BalanceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_balance(self):
        """Test case for get_balance

        Retrieves balances for a business, default to CASH type  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
