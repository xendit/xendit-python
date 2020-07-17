from xendit.models._base_model import BaseModel


class CreditCardReverseAuthorization(BaseModel):
    """Reverse Authorization class (API Reference: Credit Card)

    Attributes:
      - status (str)
      - currency (str)
      - credit_card_charge_id (str)
      - business_id (str)
      - external_id (str)
      - amount (int)
      - created (str)
      - id (str)

    Optional Attributes:
      - failure_reason (str)
    """

    status: str
    currency: str
    credit_card_charge_id: str
    business_id: str
    external_id: str
    amount: int
    created: str
    id: str

    # Optional
    failure_reason: str
