import json


class LinkAjaPaymentStatus:
    """Payment Status for LinkAja (API Reference: eWallets)

    Attributes:
      - amount (int)
      - business_id (str)
      - ewallet_type (str)
      - external_id (str)
      - status (str)
      - external_id (str) (Exists if status == "COMPLETED" or "FAILED")
      - checkout_url (str) (Exists if status == "PENDING" or "EXPIRED")
      - expired_at (str) (Exists if status == "PENDING" or "EXPIRED")
    """

    def __init__(self, xendit_response):
        self.amount = xendit_response["amount"]
        self.business_id = xendit_response["business_id"]
        self.ewallet_type = xendit_response["ewallet_type"]
        self.status = xendit_response["status"]
        self.transaction_date = xendit_response["transaction_date"]

        if self.status == "COMPLETED" or self.status == "FAILED":
            self.external_id = xendit_response["external_id"]
        elif self.status == "PENDING" or self.status == "EXPIRED":
            self.checkout_url = xendit_response["checkout_url"]
            self.expired_at = xendit_response["expired_at"]

    def __repr__(self):
        return json.dumps(vars(self), indent=4)
