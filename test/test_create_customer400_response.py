"""
    The version of the XENDIT API: 1.0.0
"""


import sys
import unittest

import xendit
from xendit.customer.model.create_customer400_response_all_of import CreateCustomer400ResponseAllOf
from xendit.customer.model.error import Error
globals()['CreateCustomer400ResponseAllOf'] = CreateCustomer400ResponseAllOf
globals()['Error'] = Error
from xendit.customer.model.create_customer400_response import CreateCustomer400Response


class TestCreateCustomer400Response(unittest.TestCase):
    """CreateCustomer400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateCustomer400Response(self):
        """Test CreateCustomer400Response"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CreateCustomer400Response()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
