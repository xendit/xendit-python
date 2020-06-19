import json

from .balance_account_type import BalanceAccountType

from xendit._init_from_xendit_response import _init_from_xendit_response
from xendit.xendit_error import XenditError
from xendit._api_requestor import _APIRequestor


class Balance:
    """Balance class (API Reference: Balance)

    Related Classes:
      - Balance.AccountType

    Static Methods:
      - Balance.get (API Reference: /Get Balance)

    Attributes:
      - balance (int)
    """

    @_init_from_xendit_response(required=["balance"])
    def __init__(self, xendit_response):
        pass

    def __repr__(self):
        return json.dumps(vars(self), indent=4)

    @staticmethod
    def get(account_type=BalanceAccountType.CASH, **kwargs):
        """Send GET request to retrieve balance (API Reference: Balance/Get Balance)

        Args:
          - account_type (Balance.AccountType)

        Returns
          Balance

        Raises
          XenditError
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
