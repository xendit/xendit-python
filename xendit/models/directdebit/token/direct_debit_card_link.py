from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery


class DirectDebitCardLink(BaseModel):
    """Card Linking class in Direct Debit Tokenization (API Reference: Direct Debit)

    Attributes:
      - card_last_four (str)
      - card_expiry (str)
      - currency (str)
      - description (str)

    """

    card_last_four: str
    card_expiry: str
    currency: str
    description: str

    class Query(BaseQuery):
        """Card Linking class in Direct Debit Tokenization Query (API Reference: Direct Debit)

        Initialize this for initialize_tokenization

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
