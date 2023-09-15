"""
    The version of the XENDIT API: 1.5.0
"""


import sys
import unittest

import xendit
from xendit.invoice.model.retail_outlet_name import RetailOutletName
globals()['RetailOutletName'] = RetailOutletName
from xendit.invoice.model.retail_outlet import RetailOutlet


class TestRetailOutlet(unittest.TestCase):
    """RetailOutlet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRetailOutlet(self):
        """Test RetailOutlet"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RetailOutlet()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
