"""
    The version of the XENDIT API: 2.89.1
"""


import sys
import unittest

import xendit
from xendit.payment_method.model.billing_information import BillingInformation
from xendit.payment_method.model.card_parameters import CardParameters
from xendit.payment_method.model.direct_debit_parameters import DirectDebitParameters
from xendit.payment_method.model.e_wallet_parameters import EWalletParameters
from xendit.payment_method.model.over_the_counter_parameters import OverTheCounterParameters
from xendit.payment_method.model.payment_method_reusability import PaymentMethodReusability
from xendit.payment_method.model.payment_method_type import PaymentMethodType
from xendit.payment_method.model.qr_code_parameters import QRCodeParameters
from xendit.payment_method.model.virtual_account_parameters import VirtualAccountParameters
globals()['BillingInformation'] = BillingInformation
globals()['CardParameters'] = CardParameters
globals()['DirectDebitParameters'] = DirectDebitParameters
globals()['EWalletParameters'] = EWalletParameters
globals()['OverTheCounterParameters'] = OverTheCounterParameters
globals()['PaymentMethodReusability'] = PaymentMethodReusability
globals()['PaymentMethodType'] = PaymentMethodType
globals()['QRCodeParameters'] = QRCodeParameters
globals()['VirtualAccountParameters'] = VirtualAccountParameters
from xendit.payment_method.model.payment_method_parameters import PaymentMethodParameters


class TestPaymentMethodParameters(unittest.TestCase):
    """PaymentMethodParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentMethodParameters(self):
        """Test PaymentMethodParameters"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaymentMethodParameters()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
