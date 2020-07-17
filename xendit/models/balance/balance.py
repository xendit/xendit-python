from xendit.models._base_model import BaseModel
from .balance_account_type import BalanceAccountType

from xendit.xendit_error import XenditError
from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params


class Balance(BaseModel):
    """Balance class (API Reference: Balance)

    Related Classes:
      - Balance.AccountType

    Static Methods:
      - Balance.get (API Reference: /Get Balance)

    Attributes:
      - balance (int)
    """

    balance: int

    @staticmethod
    def get(
        *,
        account_type=BalanceAccountType.CASH,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Send GET request to retrieve balance (API Reference: Balance/Get Balance)

        Args:
          - account_type (BalanceAccountType)
          - **for_user_id (str) (XenPlatform only)
          - **x_api_version (str): API Version that will be used. If not provided will default to the latest

        Returns
          Balance

        Raises
          XenditError
        """
        headers, _ = _extract_params(
            locals(),
            func_object=Balance.get,
            headers_params=["for_user_id", "x_api_version"],
        )
        kwargs["headers"] = headers
        account_type = Balance._parse_value(account_type)
        url = f"/balance?account_type={account_type}"

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return Balance(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def _parse_value(account_type):
        try:
            return account_type.name
        except AttributeError:
            return account_type
