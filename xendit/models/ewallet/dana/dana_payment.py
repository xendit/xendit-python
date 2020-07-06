from xendit.models._base_model import BaseModel


class DANAPayment(BaseModel):
    """Payment detail for DANA (API Reference: eWallets)

    Attributes:
      - external_id (str)
      - amount (int)
      - checkout_url (str)
      - ewallet_type (str)
    """

    external_id: str
    amount: int
    checkout_url: str
    ewallet_type: str
