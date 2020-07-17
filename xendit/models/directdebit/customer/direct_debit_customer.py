from typing import List
from .direct_debit_customer_address import DirectDebitCustomerAddress

from xendit.models._base_model import BaseModel


class DirectDebitCustomer(BaseModel):
    """Customer class in Direct Debit (API Reference: Direct Debit)

    Attributes:
      - id (str)
      - reference_id (str)
      - mobile_number (str)
      - email (str)
      - given_names (str)
      - middle_name (str)
      - surname (str)
      - description (str)
      - phone_number (str)
      - nationality (str)
      - addresses (DirectDebitCustomerAddress[])
      - date_of_birth (str)
      - metadata (dict)

    """

    id: str
    reference_id: str
    mobile_number: str
    email: str
    given_names: str
    middle_name: str
    surname: str
    description: str
    phone_number: str
    nationality: str
    addresses: List[DirectDebitCustomerAddress]
    date_of_birth: str
    metadata: dict
