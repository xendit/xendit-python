"""
    The version of the XENDIT API: 2.91.2
"""


import sys
import unittest

import xendit
from xendit.payment_method.model.direct_debit_channel_code import DirectDebitChannelCode
from xendit.payment_method.model.direct_debit_channel_properties import DirectDebitChannelProperties
globals()['DirectDebitChannelCode'] = DirectDebitChannelCode
globals()['DirectDebitChannelProperties'] = DirectDebitChannelProperties
from xendit.payment_method.model.direct_debit_parameters import DirectDebitParameters


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
