from enum import Enum
from xendit.xendit_error import XenditError
from xendit.api_requestor import APIRequestor


class Balance:
    class AccountType(Enum):
        CASH = "CASH"
        HOLDING = "HOLDING"
        TAX = "TAX"

    def __init__(self, xendit_response):
        self.balance = xendit_response["balance"]

    def __repr__(self):
        return str({"balance": self.balance})

    @staticmethod
    def get(account_type=AccountType.CASH, *args, **kwargs):
        """
        URL: /balance
        Method: GET
        Params: Account Type (optional)
        """
        account_type = Balance._parse_value(account_type)
        url = f"/balance?account_type={account_type}"
        resp = APIRequestor.get(url, *args, **kwargs)
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
