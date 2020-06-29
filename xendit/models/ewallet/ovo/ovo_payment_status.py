import json


class OVOPaymentStatus:
    """Payment Status for OVO (API Reference: eWallets)

    Attributes:
      - amount (str)
      - business_id (str)
      - ewallet_type (str)
      - external_id (str)
      - status (str)
      - transaction_date (str) (ISO 8601 Date)
    """

    def __init__(self, xendit_response):
        self.amount = xendit_response["amount"]
        self.business_id = xendit_response["business_id"]
        self.ewallet_type = xendit_response["ewallet_type"]
        self.status = xendit_response["status"]
        self.transaction_date = xendit_response["transaction_date"]

    def __repr__(self):
        return json.dumps(vars(self), indent=4)
