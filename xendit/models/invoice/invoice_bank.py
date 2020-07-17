from xendit.models._base_model import BaseModel


class InvoiceBank(BaseModel):
    """Bank data detail in Invoice (API Reference: Invoice)

    Attributes:
      - bank_code (str)
      - collection_type (str)
      - bank_account_number (str)
      - transfer_amount (int)
      - bank_branch (str)
      - account_holder_name (str)
      - identity_amount (str)
    """

    bank_code: str
    collection_type: str
    bank_account_number: str
    transfer_amount: int
    bank_branch: str
    account_holder_name: str
    identity_amount: str
