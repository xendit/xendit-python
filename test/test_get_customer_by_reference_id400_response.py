"""
    The version of the XENDIT API: 1.0.0
"""


import sys
import unittest

import xendit
from xendit.customer.model.error import Error
from xendit.customer.model.get_customer_by_reference_id400_response_all_of import GetCustomerByReferenceID400ResponseAllOf
globals()['Error'] = Error
globals()['GetCustomerByReferenceID400ResponseAllOf'] = GetCustomerByReferenceID400ResponseAllOf
from xendit.customer.model.get_customer_by_reference_id400_response import GetCustomerByReferenceID400Response


class TestGetCustomerByReferenceID400Response(unittest.TestCase):
    """GetCustomerByReferenceID400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetCustomerByReferenceID400Response(self):
        """Test GetCustomerByReferenceID400Response"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetCustomerByReferenceID400Response()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
