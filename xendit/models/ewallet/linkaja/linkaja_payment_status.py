import json


class LinkAjaPaymentStatus:
    """Payment Status for LinkAja (API Reference: eWallets)

    Attributes:
      - amount (int)
      - business_id (str)
      - external_id (str)
      - status (str)
      - payment_timestamp (str) (Exists if status == "COMPLETED" or "FAILED")
      - checkout_url (str) (Exists if status == "PENDING" or "EXPIRED")
      - expired_at (str) (Exists if status == "PENDING" or "EXPIRED")
    """

    def __init__(self, xendit_response):
        self.amount = xendit_response["amount"]
        self.business_id = xendit_response["business_id"]
        self.external_id = xendit_response["external_id"]
        self.status = xendit_response["status"]

        if self.status == "COMPLETED" or self.status == "FAILED":
            self.payment_timestamp = xendit_response["payment_timestamp"]
        elif self.status == "PENDING" or self.status == "EXPIRED":
            self.checkout_url = xendit_response["checkout_url"]
            self.expired_at = xendit_response["expired_at"]

    def __repr__(self):
        return json.dumps(vars(self), indent=4)
