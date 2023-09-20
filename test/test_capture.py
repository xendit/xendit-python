"""
    The version of the XENDIT API: 1.42.3
"""


import sys
import unittest

import xendit
from xendit.payment_request.model.payment_method import PaymentMethod
globals()['PaymentMethod'] = PaymentMethod
from xendit.payment_request.model.capture import Capture


class TestCapture(unittest.TestCase):
    """Capture unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCapture(self):
        """Test Capture"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Capture()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
