from xendit.models._base_model import BaseModel


class DANAPaymentStatus(BaseModel):
    """Payment Status for DANA (API Reference: eWallets)

    Attributes:
      - external_id (str)
      - business_id (str)
      - amount (int)
      - expiration_date (str)
      - checkout_url (str)
      - status (str)
    """

    external_id: str
    business_id: str
    amount: int
    expiration_date: str
    checkout_url: str
    status: str
