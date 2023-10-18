"""
    The version of the XENDIT API: 1.44.1
"""


import unittest

import xendit
from payment_request.payment_request_api import PaymentRequestApi  # noqa: E501


class TestPaymentRequestApi(unittest.TestCase):
    """PaymentRequestApi unit test stubs"""

    def setUp(self):
        self.api = PaymentRequestApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_payment_request(self):
        """Test case for create_payment_request

        Create Payment Request  # noqa: E501
        """
        pass

    def test_get_payment_request_by_id(self):
        """Test case for get_payment_request_by_id

        Get payment request by ID  # noqa: E501
        """
        pass

    def test_get_payment_request_captures(self):
        """Test case for get_payment_request_captures

        Get Payment Request Capture  # noqa: E501
        """
        pass

    def test_get_all_payment_requests(self):
        """Test case for get_all_payment_requests

        Get all payment requests by filter  # noqa: E501
        """
        pass

    def test_capture_payment_request(self):
        """Test case for capture_payment_request

        Payment Request Capture  # noqa: E501
        """
        pass

    def test_authorize_payment_request(self):
        """Test case for authorize_payment_request

        Payment Request Authorize  # noqa: E501
        """
        pass

    def test_resend_payment_request_auth(self):
        """Test case for resend_payment_request_auth

        Payment Request Resend Auth  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
