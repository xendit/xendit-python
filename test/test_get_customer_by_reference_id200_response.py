"""
    The version of the XENDIT API: 1.0.0
"""


import sys
import unittest

import xendit
from xendit.customer.model.customer import Customer
globals()['Customer'] = Customer
from xendit.customer.model.get_customer_by_reference_id200_response import GetCustomerByReferenceID200Response


class TestGetCustomerByReferenceID200Response(unittest.TestCase):
    """GetCustomerByReferenceID200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetCustomerByReferenceID200Response(self):
        """Test GetCustomerByReferenceID200Response"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetCustomerByReferenceID200Response()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
