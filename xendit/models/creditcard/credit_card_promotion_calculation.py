from xendit.models._base_model import BaseModel


class CreditCardPromotionCalculation(BaseModel):
    """Promotion Calculation class (API Reference: Credit Card)

    Attributes:
      - reference_id (str)
      - original_amount (float)
      - final_amount (float)
      - description (str)

    Optional Attributes:
      - discount_percent (float)
      - discount_amount (float)
    """
