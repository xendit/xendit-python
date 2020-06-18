from enum import Enum
from xendit.xendit_error import XenditError
from xendit._api_requestor import _APIRequestor


class Balance:
    """Balance class (API Reference: Balance)

    Related Enums:
      - Balance.AccountType

    Static Methods:
      - Balance.get (API Reference: /Get Balance)
    """

    class AccountType(Enum):
        """Account Type for Get Balance"""

        CASH = "CASH"
        HOLDING = "HOLDING"
        TAX = "TAX"

    def __init__(self, xendit_response):
        self.balance = xendit_response["balance"]

    def __repr__(self):
        return str({"balance": self.balance})

    @staticmethod
    def get(account_type=AccountType.CASH, **kwargs):
        """Send GET request to retrieve balance (API Reference: Balance/Get Balance)

        Args:
          - account_type (Balance.AccountType)

        Returns: Balance

        Raises: XenditError
        """
        account_type = Balance._parse_value(account_type)
        url = f"/balance?account_type={account_type}"
        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return Balance(resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def _parse_value(account_type):
        try:
            return account_type.name
        except AttributeError:
            return account_type
