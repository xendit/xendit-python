from xendit.apirequestor import APIRequestor


class Balance:
    accepted_account_type = ["CASH", "HOLDING", "TAX"]

    @staticmethod
    def get(account_type):
        Balance._validate_get_params(account_type)
        url = f"/balance?account_type={account_type}"
        return APIRequestor.get(url)

    @staticmethod
    def _validate_get_params(account_type):
        if account_type not in Balance.accepted_account_type:
            msg = f"Account type {account_type} is invalid. Available types: CASH, TAX, HOLDING"
            raise ValueError(msg)
