"""
    The version of the XENDIT API: 1.0.0
"""


import sys
import unittest

import xendit
from xendit.customer.model.account_bank import AccountBank
from xendit.customer.model.account_card import AccountCard
from xendit.customer.model.account_ewallet import AccountEwallet
from xendit.customer.model.account_otc import AccountOTC
from xendit.customer.model.account_pay_later import AccountPayLater
from xendit.customer.model.account_qr_code import AccountQRCode
globals()['AccountBank'] = AccountBank
globals()['AccountCard'] = AccountCard
globals()['AccountEwallet'] = AccountEwallet
globals()['AccountOTC'] = AccountOTC
globals()['AccountPayLater'] = AccountPayLater
globals()['AccountQRCode'] = AccountQRCode
from xendit.customer.model.identity_account_response_properties import IdentityAccountResponseProperties


class TestIdentityAccountResponseProperties(unittest.TestCase):
    """IdentityAccountResponseProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIdentityAccountResponseProperties(self):
        """Test IdentityAccountResponseProperties"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IdentityAccountResponseProperties()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
