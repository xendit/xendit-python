from xendit.models._base_model import BaseModel


class InvoiceRetailOutlet(BaseModel):
    """EWallet data detail in Invoice (API Reference: Invoice)

    Attributes:
      - ewallet_type (str)
    """

    ewallet_type: str
