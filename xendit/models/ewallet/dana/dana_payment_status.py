import json


class DANAPaymentStatus:
    """Payment Status for DANA (API Reference: eWallets)

    Attributes:
      - external_id (str)
      - business_id (str)
      - amount (int)
      - expiration_date (str)
      - checkout_url (str)
      - status (str)
    """

    def __init__(self, xendit_response):
        self.amount = xendit_response["amount"]
        self.business_id = xendit_response["business_id"]
        self.checkout_url = xendit_response["checkout_url"]
        self.external_id = xendit_response["external_id"]
        self.status = xendit_response["status"]
        self.expiration_date = xendit_response["expiration_date"]

    def __repr__(self):
        return json.dumps(vars(self), indent=4)
