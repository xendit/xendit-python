from .credit_card_charge_address import CreditCardChargeAddress

from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery


class CreditCardChargeBillingDetails(BaseModel):
    """BillingDetails class of Charge (API Reference: Credit Card)"""

    class Query(BaseQuery):
        """BillingDetails class of Charge Query (API Reference: Credit Card)

        Use this for initialize create_authorization and create_charge

        Attributes:
          - given_names (str)
          - address (CreditCardCharge.Address)

        Optional Attributes:
          - middle_name (str)
          - surname (str)
          - email (str)
          - mobile_number (str)
          - phone_number (str)

        """

        given_names: str
        address: CreditCardChargeAddress

        # Optional
        middle_name: str
        surname: str
        email: str
        mobile_number: str
        phone_number: str
