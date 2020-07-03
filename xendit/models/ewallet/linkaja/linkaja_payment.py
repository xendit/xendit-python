import json


class LinkAjaPayment:
    """Payment detail for LinkAja (API Reference: eWallets)

    Attributes:
      - checkout_url (str)
      - transaction_date (str) (ISO 8601)
      - amount (int)
      - external_id (str)
      - ewallet_type (str)
    """

    def __init__(self, xendit_response, x_api_version=None):
        self.checkout_url = xendit_response["checkout_url"]
        self.transaction_date = xendit_response["transaction_date"]
        self.amount = xendit_response["amount"]
        self.external_id = xendit_response["external_id"]
        self.ewallet_type = xendit_response["ewallet_type"]

    def __repr__(self):
        return json.dumps(vars(self), indent=4)
