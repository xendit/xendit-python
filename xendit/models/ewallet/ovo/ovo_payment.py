import json


class OVOPayment:
    """Payment detail for OVO (API Reference: eWallets)

    Attributes:
      - amount (int)
      - business_id (str)
      - created (str) (ISO 8601)
      - ewallet_type (str)
      - external_id (str)
      - phone (str)
      - status (str)

    Legacy Attributes:
      - transaction_date (Last version: 2019-02-04)
      - ewallet_transaction_id (Last version: 2019-02-04)
    """

    def __init__(self, xendit_response, x_api_version=None):
        self.amount = xendit_response["amount"]
        self.business_id = xendit_response["business_id"]
        self.external_id = xendit_response["external_id"]
        self.ewallet_type = xendit_response["ewallet_type"]
        self.phone = xendit_response["phone"]

        if x_api_version == "2019-02-04":
            self.transaction_date = xendit_response["transaction_date"]
            self.ewallet_transaction_id = xendit_response["ewallet_transaction_id"]
        else:
            self.created = xendit_response["created"]
            self.status = xendit_response["status"]

    def __repr__(self):
        return json.dumps(vars(self), indent=4)
