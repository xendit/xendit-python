"""
    The version of the XENDIT API: 1.0.0
"""


import unittest

import xendit
from payout.payout_api import PayoutApi  # noqa: E501


class TestPayoutApi(unittest.TestCase):
    """PayoutApi unit test stubs"""

    def setUp(self):
        self.api = PayoutApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_payout(self):
        """Test case for cancel_payout

        API to cancel requested payouts that have not yet been sent to partner banks and e-wallets. Cancellation is possible if the payout has not been sent out via our partner and when payout status is ACCEPTED.  # noqa: E501
        """
        pass

    def test_create_payout(self):
        """Test case for create_payout

        API to send money at scale to bank accounts & eWallets  # noqa: E501
        """
        pass

    def test_get_payout_by_id(self):
        """Test case for get_payout_by_id

        API to fetch the current status, or details of the payout  # noqa: E501
        """
        pass

    def test_get_payout_channels(self):
        """Test case for get_payout_channels

        API providing the current list of banks and e-wallets we support for payouts for both regions  # noqa: E501
        """
        pass

    def test_get_payouts(self):
        """Test case for get_payouts

        API to retrieve all matching payouts with reference ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
