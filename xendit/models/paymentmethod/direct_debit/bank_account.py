from xendit.models._base_model import BaseModel


class BankAccount(BaseModel):
    """
    If type='BANK_ACCOUNT', this contains details regarding the underlying bank account of the payment method. This will be None otherwise.

    Attributes:
      - masked_bank_account_number (str)
      - bank_account_hash (str)
    """

    masked_bank_account_number: str
    bank_account_hash: str
