from xendit.api_requestor import APIRequestor
from xendit.xendit_error import XenditError


class Balance:
    accepted_account_type = ["CASH", "HOLDING", "TAX"]

    def __init__(self, xendit_response):
        self.balance = xendit_response["balance"]

    def __repr__(self):
        return str({"balance": self.balance})

    @staticmethod
    def get(account_type="CASH"):
        url = f"/balance?account_type={account_type}"
        resp = APIRequestor.get(url)
        if resp.status_code >= 200 and resp.status_code < 300:
            return Balance(resp.body)
        else:
            raise XenditError(resp)
