"""
    The version of the XENDIT API: 2.87.2
"""


import sys
import unittest

import xendit
from xendit.payment_method.model.qr_code_channel_code import QRCodeChannelCode
from xendit.payment_method.model.qr_code_channel_properties import QRCodeChannelProperties
globals()['QRCodeChannelCode'] = QRCodeChannelCode
globals()['QRCodeChannelProperties'] = QRCodeChannelProperties
from xendit.payment_method.model.qr_code_parameters import QRCodeParameters


class TestQRCodeParameters(unittest.TestCase):
    """QRCodeParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testQRCodeParameters(self):
        """Test QRCodeParameters"""
        # FIXME: construct object with mandatory attributes with example values
        # model = QRCodeParameters()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
