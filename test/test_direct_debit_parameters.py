"""
    The version of the XENDIT API: 1.42.3
"""


import sys
import unittest

import xendit
from xendit.payment_request.model.direct_debit_channel_code import DirectDebitChannelCode
from xendit.payment_request.model.direct_debit_channel_properties import DirectDebitChannelProperties
from xendit.payment_request.model.direct_debit_type import DirectDebitType
globals()['DirectDebitChannelCode'] = DirectDebitChannelCode
globals()['DirectDebitChannelProperties'] = DirectDebitChannelProperties
globals()['DirectDebitType'] = DirectDebitType
from xendit.payment_request.model.direct_debit_parameters import DirectDebitParameters


class TestDirectDebitParameters(unittest.TestCase):
    """DirectDebitParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDirectDebitParameters(self):
        """Test DirectDebitParameters"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DirectDebitParameters()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
