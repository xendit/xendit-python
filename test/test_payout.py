"""
    The version of the XENDIT API: 1.0.0
"""


import sys
import unittest

import xendit
from xendit.payout.model.create_payout_request import CreatePayoutRequest
from xendit.payout.model.digital_payout_channel_properties import DigitalPayoutChannelProperties
from xendit.payout.model.payout_all_of import PayoutAllOf
from xendit.payout.model.receipt_notification import ReceiptNotification
globals()['CreatePayoutRequest'] = CreatePayoutRequest
globals()['DigitalPayoutChannelProperties'] = DigitalPayoutChannelProperties
globals()['PayoutAllOf'] = PayoutAllOf
globals()['ReceiptNotification'] = ReceiptNotification
from xendit.payout.model.payout import Payout


class TestPayout(unittest.TestCase):
    """Payout unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPayout(self):
        """Test Payout"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Payout()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
