import json
from dataclasses import dataclass


@dataclass(init=False)
class InvoiceRetailOutlet:
    retail_outlet_name: str
    payment_code: str
    transfer_amount: int

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return json.dumps(vars(self), indent=4)
