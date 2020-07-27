from xendit.models._base_model import BaseModel


class CardlessCreditPayment(BaseModel):
    """Payment class of Cardless Credit (API Reference: Cardless Credit)

    Attributes:
      - created (str)
      - reference (str)
      - total_uploaded_count (int)
      - total_uploaded_amount (int)
      - status (str)
      - id (str)
    """

    redirect_url: str
    transaction_id: str
    order_id: str
    external_id: str
    cardless_credit_type: str
