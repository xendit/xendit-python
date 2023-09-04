"""
    The version of the XENDIT API: 2.86.1
"""


import sys
import unittest

import xendit
from xendit.payment_method.model.card_channel_properties import CardChannelProperties
from xendit.payment_method.model.card_verification_results import CardVerificationResults
from xendit.payment_method.model.tokenized_card_information import TokenizedCardInformation
globals()['CardChannelProperties'] = CardChannelProperties
globals()['CardVerificationResults'] = CardVerificationResults
globals()['TokenizedCardInformation'] = TokenizedCardInformation
from xendit.payment_method.model.card import Card


class TestCard(unittest.TestCase):
    """Card unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCard(self):
        """Test Card"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Card()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
