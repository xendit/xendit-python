"""
    The version of the XENDIT API: 1.44.0
"""


import sys
import unittest

import xendit
from xendit.payment_request.model.direct_debit_bank_account import DirectDebitBankAccount
from xendit.payment_request.model.direct_debit_debit_card import DirectDebitDebitCard
from xendit.payment_request.model.direct_debit_type import DirectDebitType
globals()['DirectDebitBankAccount'] = DirectDebitBankAccount
globals()['DirectDebitDebitCard'] = DirectDebitDebitCard
globals()['DirectDebitType'] = DirectDebitType
from xendit.payment_request.model.direct_debit_all_of import DirectDebitAllOf


class TestDirectDebitAllOf(unittest.TestCase):
    """DirectDebitAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDirectDebitAllOf(self):
        """Test DirectDebitAllOf"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DirectDebitAllOf()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
