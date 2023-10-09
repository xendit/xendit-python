"""
    The version of the XENDIT API: 1.0.0
"""


import sys
import unittest

import xendit
from xendit.customer.model.address import Address
from xendit.customer.model.business_detail import BusinessDetail
from xendit.customer.model.end_customer_status import EndCustomerStatus
from xendit.customer.model.identity_account_response import IdentityAccountResponse
from xendit.customer.model.individual_detail import IndividualDetail
from xendit.customer.model.kyc_document_response import KYCDocumentResponse
globals()['Address'] = Address
globals()['BusinessDetail'] = BusinessDetail
globals()['EndCustomerStatus'] = EndCustomerStatus
globals()['IdentityAccountResponse'] = IdentityAccountResponse
globals()['IndividualDetail'] = IndividualDetail
globals()['KYCDocumentResponse'] = KYCDocumentResponse
from xendit.customer.model.customer import Customer


class TestCustomer(unittest.TestCase):
    """Customer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomer(self):
        """Test Customer"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Customer()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
