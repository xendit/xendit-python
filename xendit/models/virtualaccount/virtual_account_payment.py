import json
from xendit._init_from_xendit_response import _init_from_xendit_response


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

    @_init_from_xendit_response(
        required=[
            "id",
            "payment_id",
            "callback_virtual_account_id",
            "external_id",
            "merchant_code",
            "account_number",
            "bank_code",
            "amount",
            "transaction_timestamp",
        ],
        optional=["sender_name"],
    )
    def __init__(self, xendit_response):
        pass

    def __repr__(self):
        return json.dumps(vars(self), indent=4)
