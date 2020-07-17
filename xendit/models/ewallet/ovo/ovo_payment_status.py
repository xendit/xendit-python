from xendit.models._base_model import BaseModel


class OVOPaymentStatus(BaseModel):
    """Payment Status for OVO (API Reference: eWallets)

    Attributes:
      - amount (str)
      - business_id (str)
      - ewallet_type (str)
      - external_id (str)
      - status (str)
      - transaction_date (str) (ISO 8601 Date)
    """

    amount: str
    business_id: str
    ewallet_type: str
    external_id: str
    status: str
    transaction_date: str
