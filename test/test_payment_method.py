"""
    The version of the XENDIT API: 1.44.0
"""


import sys
import unittest

import xendit
from xendit.payment_request.model.card import Card
from xendit.payment_request.model.direct_debit import DirectDebit
from xendit.payment_request.model.e_wallet import EWallet
from xendit.payment_request.model.over_the_counter import OverTheCounter
from xendit.payment_request.model.payment_method_reusability import PaymentMethodReusability
from xendit.payment_request.model.payment_method_status import PaymentMethodStatus
from xendit.payment_request.model.payment_method_type import PaymentMethodType
from xendit.payment_request.model.qr_code import QRCode
from xendit.payment_request.model.virtual_account import VirtualAccount
globals()['Card'] = Card
globals()['DirectDebit'] = DirectDebit
globals()['EWallet'] = EWallet
globals()['OverTheCounter'] = OverTheCounter
globals()['PaymentMethodReusability'] = PaymentMethodReusability
globals()['PaymentMethodStatus'] = PaymentMethodStatus
globals()['PaymentMethodType'] = PaymentMethodType
globals()['QRCode'] = QRCode
globals()['VirtualAccount'] = VirtualAccount
from xendit.payment_request.model.payment_method import PaymentMethod


class TestPaymentMethod(unittest.TestCase):
    """PaymentMethod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentMethod(self):
        """Test PaymentMethod"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaymentMethod()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
