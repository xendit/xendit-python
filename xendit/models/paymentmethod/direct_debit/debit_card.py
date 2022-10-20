from xendit.models._base_model import BaseModel


class DebitCard(BaseModel):
    """
    If type='DEBIT_CARD', this contains details regarding the debit card to be used for payments. This will be None otherwise.

    Attributes:
      - mobile_number (str)
      - card_last_four (str)
      - card_expiry (str)
      - email (str)
    """

    mobile_number: str
    card_last_four: str
    card_expiry: str
    email: str
