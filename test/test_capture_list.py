"""
    The version of the XENDIT API: 1.45.1
"""


import sys
import unittest

import xendit
from xendit.payment_request.model.capture import Capture
globals()['Capture'] = Capture
from xendit.payment_request.model.capture_list import CaptureList


class TestCaptureList(unittest.TestCase):
    """CaptureList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCaptureList(self):
        """Test CaptureList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CaptureList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
