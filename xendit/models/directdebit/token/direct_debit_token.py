from xendit.models._base_model import BaseModel


class DirectDebitToken(BaseModel):
    """Token class in Direct Debit (API Reference: Direct Debit)

    Attributes:
      - id (str)
      - customer_id (str)
      - channel_code (str)
      - status (str)
      - metadata (dict)

    Optional Attributes:
      - authorizer_url (str)

    """

    id: str
    customer_id: str
    channel_code: str
    status: str
    metadata: dict

    # Optional
    authorizer_url: str
