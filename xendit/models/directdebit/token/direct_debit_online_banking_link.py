from xendit.models._base_model import BaseModel


class DirectDebitOnlineBankingLink(BaseModel):
    """Online Banking Linking class in Direct Debit Tokenization (API Reference: Direct Debit)

    Use this for initialize_tokenization

    Attributes:
      - success_redirect_url (str)

    Optional Attributes:

    """

    account_mobile_number: str
    card_last_four: str
    card_expiry: str
    account_email: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.initialize_dict(**kwargs)
