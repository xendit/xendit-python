from xendit.models._base_model import BaseModel


class VirtualAccountPayment(BaseModel):
    """Payment class for Virtual Account (API Reference: Virtual Account)

    Attributes:
      - id (str)
      - payment_id (str)
      - callback_virtual_account_id (str)
      - external_id (str)
      - merchant_code (str)
      - account_number (str)
      - bank_code (str)
      - amount (int)
      - transaction_timestamp (str)

    Optional Attributes:
      - sender_name (str)
    """

    id: str
    payment_id: str
    callback_virtual_account_id: str
    external_id: str
    merchant_code: str
    account_number: str
    bank_code: str
    amount: int
    transaction_timestamp: str

    # Optional
    sender_name: str
