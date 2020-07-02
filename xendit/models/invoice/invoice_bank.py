from dataclasses import dataclass


@dataclass
class InvoiceBank:
    bank_code: str
    collection_type: str
    bank_account_number: str
    transfer_amount: int
    bank_branch: str
    account_holder_name: str
    identity_amount: str
