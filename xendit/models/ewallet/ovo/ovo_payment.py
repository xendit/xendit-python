import json


class OVOPayment:
    """Payment detail for OVO (API Reference: eWallets)

    Attributes:
      - business_id (str)
      - external_id (str)
      - amount (int)
      - phone (str)
      - ewallet_type (str)
      - status (str)
      - created (str) (ISO 8601)
    """

    def __init__(self, xendit_response):
        self.business_id = xendit_response["business_id"]
        self.external_id = xendit_response["external_id"]
        self.amount = xendit_response["amount"]
        self.phone = xendit_response["phone"]
        self.ewallet_type = xendit_response["ewallet_type"]
        self.status = xendit_response["status"]
        self.created = xendit_response["created"]

    def __repr__(self):
        return json.dumps(vars(self), indent=4)
