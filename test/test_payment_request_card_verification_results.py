"""
    The version of the XENDIT API: 1.41.0
"""


import sys
import unittest

import xendit
from xendit.payment_request.model.payment_request_card_verification_results_three_dee_secure import PaymentRequestCardVerificationResultsThreeDeeSecure
globals()['PaymentRequestCardVerificationResultsThreeDeeSecure'] = PaymentRequestCardVerificationResultsThreeDeeSecure
from xendit.payment_request.model.payment_request_card_verification_results import PaymentRequestCardVerificationResults


class TestPaymentRequestCardVerificationResults(unittest.TestCase):
    """PaymentRequestCardVerificationResults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentRequestCardVerificationResults(self):
        """Test PaymentRequestCardVerificationResults"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaymentRequestCardVerificationResults()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
