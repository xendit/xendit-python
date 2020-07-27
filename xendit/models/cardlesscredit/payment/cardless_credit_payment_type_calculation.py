from typing import List
from xendit.models._base_model import BaseModel

from .cardless_credit_payment_type import CardlessCreditPaymentType


class CardlessCreditPaymentTypeCalculation(BaseModel):
    """Payment type calculation of Cardless Credit (API Reference: Cardless Credit)

    Attributes:
      - message (str)
      - payments (CardlessCreditPaymentType[])
    """

    message: str
    payments: List[CardlessCreditPaymentType]
