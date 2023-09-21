"""
    The version of the XENDIT API: 1.44.0
"""


import sys
import unittest

import xendit
from xendit.payment_request.model.payment_method_parameters import PaymentMethodParameters
from xendit.payment_request.model.payment_request_basket import PaymentRequestBasket
from xendit.payment_request.model.payment_request_capture_method import PaymentRequestCaptureMethod
from xendit.payment_request.model.payment_request_currency import PaymentRequestCurrency
from xendit.payment_request.model.payment_request_initiator import PaymentRequestInitiator
from xendit.payment_request.model.payment_request_parameters_channel_properties import PaymentRequestParametersChannelProperties
from xendit.payment_request.model.payment_request_shipping_information import PaymentRequestShippingInformation
globals()['PaymentMethodParameters'] = PaymentMethodParameters
globals()['PaymentRequestBasket'] = PaymentRequestBasket
globals()['PaymentRequestCaptureMethod'] = PaymentRequestCaptureMethod
globals()['PaymentRequestCurrency'] = PaymentRequestCurrency
globals()['PaymentRequestInitiator'] = PaymentRequestInitiator
globals()['PaymentRequestParametersChannelProperties'] = PaymentRequestParametersChannelProperties
globals()['PaymentRequestShippingInformation'] = PaymentRequestShippingInformation
from xendit.payment_request.model.payment_request_parameters import PaymentRequestParameters


class TestPaymentRequestParameters(unittest.TestCase):
    """PaymentRequestParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentRequestParameters(self):
        """Test PaymentRequestParameters"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaymentRequestParameters()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
