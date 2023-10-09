"""
    The version of the XENDIT API: 1.0.0
"""


import sys
import unittest

import xendit
from xendit.customer.model.address_request import AddressRequest
from xendit.customer.model.business_detail import BusinessDetail
from xendit.customer.model.identity_account_request import IdentityAccountRequest
from xendit.customer.model.individual_detail import IndividualDetail
from xendit.customer.model.kyc_document_request import KYCDocumentRequest
globals()['AddressRequest'] = AddressRequest
globals()['BusinessDetail'] = BusinessDetail
globals()['IdentityAccountRequest'] = IdentityAccountRequest
globals()['IndividualDetail'] = IndividualDetail
globals()['KYCDocumentRequest'] = KYCDocumentRequest
from xendit.customer.model.customer_request import CustomerRequest


class TestCustomerRequest(unittest.TestCase):
    """CustomerRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomerRequest(self):
        """Test CustomerRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CustomerRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
