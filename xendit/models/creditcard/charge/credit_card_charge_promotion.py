from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery


class CreditCardChargePromotion(BaseModel):
    """Promotion class of Credit Card Charge (API Reference: Credit Card)

    Optional Attributes:
        - reference_id (str)
        - original_amount (float)
    """

    # Optional
    reference_id: str
    original_amount: int

    class Query(BaseQuery):
        """Promotion class of Credit Card Charge Query (API Reference: Credit Card)

        Used for create_authorization and create_charge

        Optional Attributes:
          - reference_id (str)
          - original_amount (float)
        """

        # Optional
        reference_id: str
        original_amount: int
