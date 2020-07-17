from typing import List

from xendit.models._base_model import BaseModel

from .direct_debit_basket import DirectDebitBasket


class DirectDebitPayment(BaseModel):
    """Payment class in Direct Debit (API Reference: Direct Debit)

    Attributes:
      - id (str)
      - reference_id (str)
      - channel_code (str)
      - payment_method_id (str)
      - currency (str)
      - amount (float)
      - description (str)
      - status (bool)
      - failure_code (str)
      - is_otp_required (bool)
      - otp_mobile_number (str)
      - otp_expiration_timestamp (str)
      - created (str)
      - updated (str)
      - basket (DirectDebitBasket[])
      - metadata (dict)
    """

    id: str
    reference_id: str
    channel_code: str
    payment_method_id: str
    currency: str
    amount: float
    description: str
    status: bool
    failure_code: str
    is_otp_required: bool
    otp_mobile_number: str
    otp_expiration_timestamp: str
    created: str
    updated: str
    basket: List[DirectDebitBasket]
    metadata: dict
