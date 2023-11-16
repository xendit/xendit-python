"""
    The version of the XENDIT API: 2.91.2
"""


import sys
import unittest

import xendit
from xendit.payment_method.model.payment_method import PaymentMethod
globals()['PaymentMethod'] = PaymentMethod
from xendit.payment_method.model.payment_method_list import PaymentMethodList


class TestPaymentMethodList(unittest.TestCase):
    """PaymentMethodList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentMethodList(self):
        """Test PaymentMethodList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaymentMethodList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
