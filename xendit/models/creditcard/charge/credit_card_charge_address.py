from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery


class CreditCardChargeAddress(BaseModel):
    """Address class of Charge Billing Details (API Reference: Credit Card)"""

    class Query(BaseQuery):
        """Address class of Charge Billing Details Query (API Reference: Credit Card)

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
