"""
    The version of the XENDIT API: 1.2.3
"""


import unittest

import xendit
from refund.refund_api import RefundApi  # noqa: E501


class TestRefundApi(unittest.TestCase):
    """RefundApi unit test stubs"""

    def setUp(self):
        self.api = RefundApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_refund(self):
        """Test case for cancel_refund

        """
        pass

    def test_create_refund(self):
        """Test case for create_refund

        """
        pass

    def test_get_all_refunds(self):
        """Test case for get_all_refunds

        """
        pass

    def test_get_refund(self):
        """Test case for get_refund

        """
        pass


if __name__ == '__main__':
    unittest.main()
