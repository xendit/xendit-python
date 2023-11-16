"""
    The version of the XENDIT API: 1.45.1
"""


import sys
import unittest

import xendit
from xendit.payment_request.model.payment_method import PaymentMethod
from xendit.payment_request.model.payment_request_action import PaymentRequestAction
from xendit.payment_request.model.payment_request_basket import PaymentRequestBasket
from xendit.payment_request.model.payment_request_capture_method import PaymentRequestCaptureMethod
from xendit.payment_request.model.payment_request_card_verification_results import PaymentRequestCardVerificationResults
from xendit.payment_request.model.payment_request_country import PaymentRequestCountry
from xendit.payment_request.model.payment_request_currency import PaymentRequestCurrency
from xendit.payment_request.model.payment_request_initiator import PaymentRequestInitiator
from xendit.payment_request.model.payment_request_shipping_information import PaymentRequestShippingInformation
from xendit.payment_request.model.payment_request_status import PaymentRequestStatus
globals()['PaymentMethod'] = PaymentMethod
globals()['PaymentRequestAction'] = PaymentRequestAction
globals()['PaymentRequestBasket'] = PaymentRequestBasket
globals()['PaymentRequestCaptureMethod'] = PaymentRequestCaptureMethod
globals()['PaymentRequestCardVerificationResults'] = PaymentRequestCardVerificationResults
globals()['PaymentRequestCountry'] = PaymentRequestCountry
globals()['PaymentRequestCurrency'] = PaymentRequestCurrency
globals()['PaymentRequestInitiator'] = PaymentRequestInitiator
globals()['PaymentRequestShippingInformation'] = PaymentRequestShippingInformation
globals()['PaymentRequestStatus'] = PaymentRequestStatus
from xendit.payment_request.model.payment_request import PaymentRequest


class TestPaymentRequest(unittest.TestCase):
    """PaymentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentRequest(self):
        """Test PaymentRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaymentRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
