from xendit.models._base_model import BaseModel


class DirectDebitCardLink(BaseModel):
    """Card Linking class in Direct Debit Tokenization (API Reference: Direct Debit)

    Use this for initialize_tokenization

    Attributes:
      - account_mobile_number (str)
      - card_last_four (str)
      - card_expiry (str)
      - account_email (str)

    """

    account_mobile_number: str
    card_last_four: str
    card_expiry: str
    account_email: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.initialize_dict(**kwargs)
