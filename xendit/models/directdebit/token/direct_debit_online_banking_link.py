from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery


class DirectDebitOnlineBankingLink(BaseModel):
    """Online Banking Linking class in Direct Debit Tokenization (API Reference: Direct Debit)

    Use this for initialize_tokenization

    Attributes:
      - account_details (str)
      - account_hash (str)
      - account_type (str)
      - currency (str)
      - description (str)

    """

    account_details: str
    account_hash: str
    account_type: str
    currency: str
    description: str

    class Query(BaseQuery):
        """Online Banking Linking class in Direct Debit Tokenization (API Reference: Direct Debit)

        Use this for initialize_tokenization

        Attributes:
          - success_redirect_url (str)
          - failure_redirect_url (str)
          - callback_url (str)

        """

        success_redirect_url: str
        failure_redirect_url: str
        callback_url: str
