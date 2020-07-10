from xendit.models._base_model import BaseModel


class CreditCardChargeInstallment(BaseModel):
    """Installment class of Charge (API Reference: Credit Card)

    Used for create_authorization and create_charge

    Optional Attributes:
        - count (int)
        - interval (str)
    """

    # Optional
    count: int
    interval: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.initialize_dict(**kwargs)
