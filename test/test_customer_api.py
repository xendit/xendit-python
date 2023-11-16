"""
    The version of the XENDIT API: 1.0.0
"""


import unittest

import xendit
from customer.customer_api import CustomerApi  # noqa: E501


class TestCustomerApi(unittest.TestCase):
    """CustomerApi unit test stubs"""

    def setUp(self):
        self.api = CustomerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_customer(self):
        """Test case for create_customer

        Create Customer  # noqa: E501
        """
        pass

    def test_get_customer(self):
        """Test case for get_customer

        Get Customer By ID  # noqa: E501
        """
        pass

    def test_get_customer_by_reference_id(self):
        """Test case for get_customer_by_reference_id

        GET customers by reference id  # noqa: E501
        """
        pass

    def test_update_customer(self):
        """Test case for update_customer

        Update End Customer Resource  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
