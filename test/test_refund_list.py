"""
    The version of the XENDIT API: 1.3.3
"""


import sys
import unittest

import xendit
from xendit.refund.model.refund import Refund
globals()['Refund'] = Refund
from xendit.refund.model.refund_list import RefundList


class TestRefundList(unittest.TestCase):
    """RefundList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRefundList(self):
        """Test RefundList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RefundList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
