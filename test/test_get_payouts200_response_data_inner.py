"""
    The version of the XENDIT API: 1.0.0
"""


import sys
import unittest

import xendit
from xendit.payout.model.digital_payout_channel_properties import DigitalPayoutChannelProperties
from xendit.payout.model.payout import Payout
from xendit.payout.model.receipt_notification import ReceiptNotification
globals()['DigitalPayoutChannelProperties'] = DigitalPayoutChannelProperties
globals()['Payout'] = Payout
globals()['ReceiptNotification'] = ReceiptNotification
from xendit.payout.model.get_payouts200_response_data_inner import GetPayouts200ResponseDataInner


class TestGetPayouts200ResponseDataInner(unittest.TestCase):
    """GetPayouts200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetPayouts200ResponseDataInner(self):
        """Test GetPayouts200ResponseDataInner"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetPayouts200ResponseDataInner()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
