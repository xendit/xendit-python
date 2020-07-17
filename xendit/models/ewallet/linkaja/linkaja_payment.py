from xendit.models._base_model import BaseModel


class LinkAjaPayment(BaseModel):
    """Payment detail for LinkAja (API Reference: eWallets)

    Attributes:
      - checkout_url (str)
      - transaction_date (str) (ISO 8601)
      - amount (int)
      - external_id (str)
      - ewallet_type (str)
    """

    checkout_url: str
    transaction_date: str
    amount: int
    external_id: str
    ewallet_type: str
