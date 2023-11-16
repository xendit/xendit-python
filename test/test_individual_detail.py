"""
    The version of the XENDIT API: 1.0.0
"""


import sys
import unittest

import xendit
from xendit.customer.model.country_code import CountryCode
from xendit.customer.model.employment_detail import EmploymentDetail
globals()['CountryCode'] = CountryCode
globals()['EmploymentDetail'] = EmploymentDetail
from xendit.customer.model.individual_detail import IndividualDetail


class TestIndividualDetail(unittest.TestCase):
    """IndividualDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIndividualDetail(self):
        """Test IndividualDetail"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IndividualDetail()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
