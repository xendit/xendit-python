from xendit.models._base_model import BaseModel


class InvoiceRetailOutlet(BaseModel):
    retail_outlet_name: str
    payment_code: str
    transfer_amount: int
