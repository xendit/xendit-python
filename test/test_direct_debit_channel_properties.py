"""
    The version of the XENDIT API: 1.41.0
"""


import sys
import unittest

import xendit
from xendit.payment_request.model.direct_debit_channel_properties_bank_account import DirectDebitChannelPropertiesBankAccount
from xendit.payment_request.model.direct_debit_channel_properties_bank_redirect import DirectDebitChannelPropertiesBankRedirect
from xendit.payment_request.model.direct_debit_channel_properties_debit_card import DirectDebitChannelPropertiesDebitCard
globals()['DirectDebitChannelPropertiesBankAccount'] = DirectDebitChannelPropertiesBankAccount
globals()['DirectDebitChannelPropertiesBankRedirect'] = DirectDebitChannelPropertiesBankRedirect
globals()['DirectDebitChannelPropertiesDebitCard'] = DirectDebitChannelPropertiesDebitCard
from xendit.payment_request.model.direct_debit_channel_properties import DirectDebitChannelProperties


class TestDirectDebitChannelProperties(unittest.TestCase):
    """DirectDebitChannelProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDirectDebitChannelProperties(self):
        """Test DirectDebitChannelProperties"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DirectDebitChannelProperties()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
