import json


class LinkAjaPaymentStatus:
    """Payment Status for LinkAja (API Reference: eWallets)

    Attributes:
      - business_id (str)
      - external_id (str)
      - amount (int)
      - status (str)
      - payment_timestamp (str) (Exists if status == "COMPLETED" or "FAILED")
      - expired_at (str) (Exists if status == "PENDING" or "EXPIRED")
      - checkout_url (str) (Exists if status == "PENDING" or "EXPIRED")
    """

    def __init__(self, xendit_response):
        self.business_id = xendit_response["business_id"]
        self.external_id = xendit_response["external_id"]
        self.amount = xendit_response["amount"]
        self.status = xendit_response["status"]

        if self.status == "COMPLETED" or self.status == "FAILED":
            self.payment_timestamp = xendit_response["payment_timestamp"]
        elif self.status == "PENDING" or self.status == "EXPIRED":
            self.expired_at = xendit_response["expired_at"]
            self.checkout_url = xendit_response["checkout_url"]

    def __repr__(self):
        return json.dumps(vars(self), indent=4)
