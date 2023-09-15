"""
    The version of the XENDIT API: 2.87.2
"""


import sys
import unittest

import xendit
from xendit.payment_method.model.over_the_counter_update_parameters import OverTheCounterUpdateParameters
from xendit.payment_method.model.payment_method_reusability import PaymentMethodReusability
from xendit.payment_method.model.payment_method_status import PaymentMethodStatus
from xendit.payment_method.model.virtual_account_update_parameters import VirtualAccountUpdateParameters
globals()['OverTheCounterUpdateParameters'] = OverTheCounterUpdateParameters
globals()['PaymentMethodReusability'] = PaymentMethodReusability
globals()['PaymentMethodStatus'] = PaymentMethodStatus
globals()['VirtualAccountUpdateParameters'] = VirtualAccountUpdateParameters
from xendit.payment_method.model.payment_method_update_parameters import PaymentMethodUpdateParameters


class TestPaymentMethodUpdateParameters(unittest.TestCase):
    """PaymentMethodUpdateParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentMethodUpdateParameters(self):
        """Test PaymentMethodUpdateParameters"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaymentMethodUpdateParameters()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
