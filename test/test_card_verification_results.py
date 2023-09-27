"""
    The version of the XENDIT API: 1.44.0
"""


import sys
import unittest

import xendit
from xendit.payment_request.model.card_verification_results_three_d_secure import CardVerificationResultsThreeDSecure
globals()['CardVerificationResultsThreeDSecure'] = CardVerificationResultsThreeDSecure
from xendit.payment_request.model.card_verification_results import CardVerificationResults


class TestCardVerificationResults(unittest.TestCase):
    """CardVerificationResults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCardVerificationResults(self):
        """Test CardVerificationResults"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CardVerificationResults()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
