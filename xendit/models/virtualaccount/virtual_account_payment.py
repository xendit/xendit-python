import json


class VirtualAccountPayment:
    """Payment class for Virtual Account (API Reference: Virtual Account)

    Attributes:
      - id (str)
      - payment_id (str)
      - callback_virtual_account_id (str)
      - external_id (str)
      - merchant_code (str)
      - account_number (str)
      - bank_code (str)
      - amount (int)
      - transaction_timestamp (str)

    Optional Attributes:
      - sender_name (str)
    """

    def __init__(self, xendit_response):
        self.id = xendit_response["id"]
        self.payment_id = xendit_response["payment_id"]
        self.callback_virtual_account_id = xendit_response[
            "callback_virtual_account_id"
        ]
        self.external_id = xendit_response["external_id"]
        self.merchant_code = xendit_response["merchant_code"]
        self.account_number = xendit_response["account_number"]
        self.bank_code = xendit_response["bank_code"]
        self.amount = xendit_response["amount"]
        self.transaction_timestamp = xendit_response["transaction_timestamp"]

        if xendit_response.get("transaction_timestamp", None) is not None:
            self.transaction_timestamp = xendit_response["transaction_timestamp"]

    def __repr__(self):
        return json.dumps(vars(self), indent=4)
