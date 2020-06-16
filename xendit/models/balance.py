from xendit.api_requestor import APIRequestor
from xendit.xendit_error import XenditError
from enum import Enum


class Balance:
    class AccountType(Enum):
        CASH = ("CASH",)
        HOLDING = ("HOLDING",)
        TAX = "TAX"

    def __init__(self, xendit_response):
        self.balance = xendit_response["balance"]

    def __repr__(self):
        return str({"balance": self.balance})

    @staticmethod
    def get(account_type=AccountType.CASH):
        """
        URL: /balance
        Method: GET
        Params: Account Type (optional)
        """
        if isinstance(account_type, Balance.AccountType):
            return Balance._process_get_balance(account_type.name)
        else:
            raise ValueError(
                "Please input the correct params with type Balance.AccountType"
            )

    @staticmethod
    def _process_get_balance(account_type):
        url = f"/balance?account_type={account_type}"
        resp = APIRequestor.get(url)
        if resp.status_code >= 200 and resp.status_code < 300:
            return Balance(resp.body)
        else:
            raise XenditError(resp)
