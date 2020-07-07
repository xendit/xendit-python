from xendit.models._base_model import BaseModel


class CreditCardChargePromotion(BaseModel):
    """Promotion class of Credit Card Charge (API Reference: Credit Card)

    Used for create_authorization and create_charge

    Optional Attributes:
        - reference_id (str)
        - original_amount (float)
    """

    # Optional
    reference_id: str
    original_amount: int

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.initialize_dict(**kwargs)
