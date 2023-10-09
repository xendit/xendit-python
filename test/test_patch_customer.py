"""
    The version of the XENDIT API: 1.0.0
"""


import sys
import unittest

import xendit
from xendit.customer.model.address_request import AddressRequest
from xendit.customer.model.business_detail import BusinessDetail
from xendit.customer.model.end_customer_status import EndCustomerStatus
from xendit.customer.model.identity_account_request import IdentityAccountRequest
from xendit.customer.model.individual_detail import IndividualDetail
from xendit.customer.model.kyc_document_request import KYCDocumentRequest
globals()['AddressRequest'] = AddressRequest
globals()['BusinessDetail'] = BusinessDetail
globals()['EndCustomerStatus'] = EndCustomerStatus
globals()['IdentityAccountRequest'] = IdentityAccountRequest
globals()['IndividualDetail'] = IndividualDetail
globals()['KYCDocumentRequest'] = KYCDocumentRequest
from xendit.customer.model.patch_customer import PatchCustomer


class TestPatchCustomer(unittest.TestCase):
    """PatchCustomer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPatchCustomer(self):
        """Test PatchCustomer"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PatchCustomer()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
