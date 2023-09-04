"""
    The version of the XENDIT API: 1.0.0
"""


import sys
import unittest

import xendit
from xendit.payout.model.digital_payout_channel_properties import DigitalPayoutChannelProperties
from xendit.payout.model.receipt_notification import ReceiptNotification
globals()['DigitalPayoutChannelProperties'] = DigitalPayoutChannelProperties
globals()['ReceiptNotification'] = ReceiptNotification
from xendit.payout.model.create_payout_request import CreatePayoutRequest


class TestCreatePayoutRequest(unittest.TestCase):
    """CreatePayoutRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreatePayoutRequest(self):
        """Test CreatePayoutRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CreatePayoutRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
