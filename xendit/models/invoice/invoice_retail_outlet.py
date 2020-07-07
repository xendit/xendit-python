from xendit.models._base_model import BaseModel


class InvoiceRetailOutlet(BaseModel):
    """Retail Outlet data detail in Invoice (API Reference: Invoice)

    Attributes:
      - retail_outlet_name (str)
      - payment_code (str)
      - transfer_amount (int)
    """

    retail_outlet_name: str
    payment_code: str
    transfer_amount: int
