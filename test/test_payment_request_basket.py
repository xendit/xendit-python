"""
    The version of the XENDIT API: 1.45.1
"""


import sys
import unittest

import xendit
from xendit.payment_request.model.payment_request_basket_item import PaymentRequestBasketItem
globals()['PaymentRequestBasketItem'] = PaymentRequestBasketItem
from xendit.payment_request.model.payment_request_basket import PaymentRequestBasket


class TestPaymentRequestBasket(unittest.TestCase):
    """PaymentRequestBasket unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentRequestBasket(self):
        """Test PaymentRequestBasket"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaymentRequestBasket()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
