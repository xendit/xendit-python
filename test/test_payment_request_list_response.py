"""
    The version of the XENDIT API: 1.44.0
"""


import sys
import unittest

import xendit
from xendit.payment_request.model.payment_request import PaymentRequest
globals()['PaymentRequest'] = PaymentRequest
from xendit.payment_request.model.payment_request_list_response import PaymentRequestListResponse


class TestPaymentRequestListResponse(unittest.TestCase):
    """PaymentRequestListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentRequestListResponse(self):
        """Test PaymentRequestListResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaymentRequestListResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
