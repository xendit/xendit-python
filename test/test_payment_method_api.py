"""
    The version of the XENDIT API: 2.87.2
"""


import unittest

import xendit
from payment_method.payment_method_api import PaymentMethodApi  # noqa: E501


class TestPaymentMethodApi(unittest.TestCase):
    """PaymentMethodApi unit test stubs"""

    def setUp(self):
        self.api = PaymentMethodApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_auth_payment_method(self):
        """Test case for auth_payment_method

        Validate a payment method's linking OTP  # noqa: E501
        """
        pass

    def test_create_payment_method(self):
        """Test case for create_payment_method

        Creates payment method  # noqa: E501
        """
        pass

    def test_expire_payment_method(self):
        """Test case for expire_payment_method

        Expires a payment method  # noqa: E501
        """
        pass

    def test_get_all_payment_channels(self):
        """Test case for get_all_payment_channels

        Get all payment channels  # noqa: E501
        """
        pass

    def test_get_all_payment_methods(self):
        """Test case for get_all_payment_methods

        Get all payment methods by filters  # noqa: E501
        """
        pass

    def test_get_payment_method_by_id(self):
        """Test case for get_payment_method_by_id

        Get payment method by ID  # noqa: E501
        """
        pass

    def test_get_payments_by_payment_method_id(self):
        """Test case for get_payments_by_payment_method_id

        Returns payments with matching PaymentMethodID.  # noqa: E501
        """
        pass

    def test_patch_payment_method(self):
        """Test case for patch_payment_method

        Patch payment methods  # noqa: E501
        """
        pass

    def test_simulate_payment(self):
        """Test case for simulate_payment

        Makes payment with matching PaymentMethodID.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
