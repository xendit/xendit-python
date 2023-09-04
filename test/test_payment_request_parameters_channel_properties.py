"""
    The version of the XENDIT API: 1.41.0
"""


import sys
import unittest

import xendit
from xendit.payment_request.model.payment_request_channel_properties import PaymentRequestChannelProperties
from xendit.payment_request.model.payment_request_parameters_channel_properties_all_of import PaymentRequestParametersChannelPropertiesAllOf
globals()['PaymentRequestChannelProperties'] = PaymentRequestChannelProperties
globals()['PaymentRequestParametersChannelPropertiesAllOf'] = PaymentRequestParametersChannelPropertiesAllOf
from xendit.payment_request.model.payment_request_parameters_channel_properties import PaymentRequestParametersChannelProperties


class TestPaymentRequestParametersChannelProperties(unittest.TestCase):
    """PaymentRequestParametersChannelProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentRequestParametersChannelProperties(self):
        """Test PaymentRequestParametersChannelProperties"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaymentRequestParametersChannelProperties()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
