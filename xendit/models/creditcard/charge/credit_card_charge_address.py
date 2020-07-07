from xendit.models._base_model import BaseModel


class CreditCardChargeAddress(BaseModel):
    """Address class of Charge Billing Details (API Reference: Credit Card)

    Use this for initialize create_authorization and create_charge

    Attributes:
        - country (str)

    Optional Attributes:
        - street_line1 (str)
        - street_line2 (str)
        - city (str)
        - province (str)
        - state (str)
        - postal_code (str)
        - description (str)
    """

    country: str

    # Optional
    street_line1: str
    street_line2: str
    city: str
    province: str
    state: str
    postal_code: str
    description: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.initialize_dict(**kwargs)
