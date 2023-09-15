"""
    The version of the XENDIT API: 1.5.0
"""


import sys
import unittest

import xendit
from xendit.invoice.model.qr_code_type import QrCodeType
globals()['QrCodeType'] = QrCodeType
from xendit.invoice.model.qr_code import QrCode


class TestQrCode(unittest.TestCase):
    """QrCode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testQrCode(self):
        """Test QrCode"""
        # FIXME: construct object with mandatory attributes with example values
        # model = QrCode()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
