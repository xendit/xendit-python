"""
    The version of the XENDIT API: 3.4.3
"""


import sys
import unittest

import xendit
from xendit.balance_and_transaction.model.channels_categories import ChannelsCategories
from xendit.balance_and_transaction.model.currency import Currency
from xendit.balance_and_transaction.model.fee_response import FeeResponse
from xendit.balance_and_transaction.model.transaction_id import TransactionId
from xendit.balance_and_transaction.model.transaction_response_type import TransactionResponseType
from xendit.balance_and_transaction.model.transaction_statuses import TransactionStatuses
globals()['ChannelsCategories'] = ChannelsCategories
globals()['Currency'] = Currency
globals()['FeeResponse'] = FeeResponse
globals()['TransactionId'] = TransactionId
globals()['TransactionResponseType'] = TransactionResponseType
globals()['TransactionStatuses'] = TransactionStatuses
from xendit.balance_and_transaction.model.transaction_response import TransactionResponse


class TestTransactionResponse(unittest.TestCase):
    """TransactionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTransactionResponse(self):
        """Test TransactionResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TransactionResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
