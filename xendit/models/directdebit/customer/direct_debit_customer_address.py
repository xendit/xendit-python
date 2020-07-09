from xendit.models._base_model import BaseModel


class DirectDebitCustomerAddress(BaseModel):
    """Address class of Customer in Direct Debit (API Reference: Direct Debit)

    Use this to initialize create_customer

    Attributes:
        - country (str)

    Optional Attributes:
        - street_line1 (str)
        - street_line2 (str)
        - city (str)
        - province (str)
        - state (str)
        - postal_code (str)
    """

    country: str

    # Optional
    street_line1: str
    street_line2: str
    city: str
    province: str
    state: str
    postal_code: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.initialize_dict(**kwargs)
