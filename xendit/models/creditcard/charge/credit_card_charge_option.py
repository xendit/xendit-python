from typing import List
from xendit.models._base_model import BaseModel


class CreditCardChargeOption(BaseModel):
    """Charge Option class (API Reference: Credit Card)

    Attributes:
      - business_id (str)
      - bin (str)
      - promotions (CreditCardChargeOption.Promotion[])
      - installments (CreditCardChargeOption.Installments)
    """

    class Promotion(BaseModel):
        """Promotion class of Charge Option (API Reference: Credit Card)

        Attributes:
          - original_amount (float)
          - final_amount (float)
          - currency (str)

        Optional Attributes:
          - reference_id (str)
          - discount_amount (float)
          - discount_percent (float)
        """

        original_amount: float
        final_amount: float
        currency: str

        # Optional
        reference_id: str
        discount_amount: float
        discount_percent: float

    class Installments(BaseModel):
        """Installment class of Charge Option (API Reference: Credit Card)

      Attributes:
        - count: int
        - interval: str
        - acquirer: str
        - currency: str
        - minimum_amount: str
      """

        count: int
        interval: str
        acquirer: str
        currency: str
        minimum_amount: str

    business_id: str
    bin: str
    promotions: List[Promotion]
    installments: Installments
