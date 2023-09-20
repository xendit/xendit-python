"""
    The version of the XENDIT API: 1.0.0
"""


import sys
import unittest

import xendit
from xendit.payout.model.get_payouts200_response_data_inner import GetPayouts200ResponseDataInner
from xendit.payout.model.get_payouts200_response_links import GetPayouts200ResponseLinks
globals()['GetPayouts200ResponseDataInner'] = GetPayouts200ResponseDataInner
globals()['GetPayouts200ResponseLinks'] = GetPayouts200ResponseLinks
from xendit.payout.model.get_payouts200_response import GetPayouts200Response


class TestGetPayouts200Response(unittest.TestCase):
    """GetPayouts200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetPayouts200Response(self):
        """Test GetPayouts200Response"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetPayouts200Response()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
