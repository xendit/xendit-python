from xendit.models._base_model import BaseModel


class CreditCardRefund(BaseModel):
    """Refund class (API Reference: Credit Card)

    Attributes:
      - updated (str)
      - created (str)
      - credit_card_charge_id (str)
      - user_id (str)
      - amount (int)
      - external_id (str)
      - status (str)
      - fee_refund_amount (int)
      - id (str)

    Optional Attributes:
      - failure_reason (str)
    """

    updated: str
    created: str
    credit_card_charge_id: str
    user_id: str
    amount: int
    external_id: str
    status: str
    fee_refund_amount: int
    id: str

    # Optional
    failure_reason: str
