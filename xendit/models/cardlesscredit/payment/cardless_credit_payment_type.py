from xendit.models._base_model import BaseModel


class CardlessCreditPaymentType(BaseModel):
    """Payment type class of Cardless Credit (API Reference: Cardless Credit)

    Attributes:
      - raw_monthly_installment (float)
      - name (str)
      - amount (int)
      - installment_amount (int)
      - raw_amount (float)
      - rate (float)
      - down_payment (int)
      - monthly_installment (int)
      - discounted_monthly_installment (int)
      - tenure (int)
      - id (str)
    """

    raw_monthly_installment: float
    name: str
    name: str
    amount: int
    installment_amount: int
    raw_amount: float
    rate: float
    down_payment: IndentationError
    monthly_installment: int
    discounted_monthly_installment: int
    tenure: int
    id: str
