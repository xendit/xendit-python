"""
    The version of the XENDIT API: 1.0.0
"""


import sys
import unittest

import xendit
from xendit.customer.model.error import Error
from xendit.customer.model.update_customer400_response_all_of import UpdateCustomer400ResponseAllOf
globals()['Error'] = Error
globals()['UpdateCustomer400ResponseAllOf'] = UpdateCustomer400ResponseAllOf
from xendit.customer.model.update_customer400_response import UpdateCustomer400Response


class TestUpdateCustomer400Response(unittest.TestCase):
    """UpdateCustomer400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUpdateCustomer400Response(self):
        """Test UpdateCustomer400Response"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UpdateCustomer400Response()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
