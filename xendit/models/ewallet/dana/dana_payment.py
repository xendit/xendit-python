import json


class DANAPayment:
    """Payment detail for DANA (API Reference: eWallets)

    Attributes:
      - external_id (str)
      - amount (int)
      - checkout_url (str)
      - ewallet_type (str)
    """

    def __init__(self, xendit_response, x_api_version=None):
        self.external_id = xendit_response["external_id"]
        self.amount = xendit_response["amount"]
        self.checkout_url = xendit_response["checkout_url"]
        self.ewallet_type = xendit_response["ewallet_type"]

    def __repr__(self):
        return json.dumps(vars(self), indent=4)
