"""
    The version of the XENDIT API: 1.45.1
"""


import sys
import unittest

import xendit
from xendit.payment_request.model.capture_list import CaptureList
globals()['CaptureList'] = CaptureList
from xendit.payment_request.model.capture_list_response import CaptureListResponse


class TestCaptureListResponse(unittest.TestCase):
    """CaptureListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCaptureListResponse(self):
        """Test CaptureListResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CaptureListResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
