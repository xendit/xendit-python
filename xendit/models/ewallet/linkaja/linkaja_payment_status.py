from xendit.models._base_model import BaseModel


class LinkAjaPaymentStatus(BaseModel):
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

    business_id: str
    external_id: str
    amount: int
    status: str

    # Attributes for (status == "COMPLETED" or "FAILED")
    payment_timestamp: str

    # Attributes for (status == "PENDING" or "EXPIRED")
    expired_at: str
    checkout_url: str
