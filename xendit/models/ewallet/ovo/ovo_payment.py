from xendit.models._base_model import BaseModel


class OVOPayment(BaseModel):
    """Payment detail for OVO (API Reference: eWallets)

    Attributes:
      - amount (int)
      - business_id (str)
      - created (str) (ISO 8601)
      - ewallet_type (str)
      - external_id (str)
      - phone (str)
      - status (str)

    Legacy Attributes:
      - transaction_date (Last version: 2019-02-04)
      - ewallet_transaction_id (Last version: 2019-02-04)
    """

    amount: int
    business_id: str
    created: str
    ewallet_type: str
    external_id: str
    phone: str
    status: str

    # Attributes for (x_api_version == 2019-02-04)
    transaction_date: str
    ewallet_transaction_id: str
