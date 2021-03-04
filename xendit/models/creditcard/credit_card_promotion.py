from typing import List
from xendit.models._base_model import BaseModel


class CreditCardPromotion(BaseModel):
    """Promotion class (API Reference: Credit Card)

    Attributes:
      - id (str)
      - business_id (str)
      - status (str)
      - reference_id (str)
      - description (str)
      - promo_code (str)
      - bin_list (str[])
      - channel_code (str)
      - discount_percent (float)
      - discount_amount (float)
      - currency (str)
      - start_time (str)
      - end_time (str)
      - min_original_amount (float)
      - max_discount_amount (float)
    """

    id: str
    business_id: str
    status: str
    reference_id: str
    description: str
    promo_code: str
    bin_list: List[str]
    channel_code: str
    discount_percent: float
    discount_amount: float
    currency: str
    start_time: str
    end_time: str
    min_original_amount: float
    max_discount_amount: float
