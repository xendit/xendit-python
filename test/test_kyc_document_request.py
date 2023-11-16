"""
    The version of the XENDIT API: 1.0.0
"""


import sys
import unittest

import xendit
from xendit.customer.model.country_code import CountryCode
from xendit.customer.model.kyc_document_sub_type import KYCDocumentSubType
from xendit.customer.model.kyc_document_type import KYCDocumentType
globals()['CountryCode'] = CountryCode
globals()['KYCDocumentSubType'] = KYCDocumentSubType
globals()['KYCDocumentType'] = KYCDocumentType
from xendit.customer.model.kyc_document_request import KYCDocumentRequest


class TestKYCDocumentRequest(unittest.TestCase):
    """KYCDocumentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testKYCDocumentRequest(self):
        """Test KYCDocumentRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = KYCDocumentRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
