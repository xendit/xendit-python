from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery


class CreditCardChargeInstallment(BaseModel):
    """Installment class of Charge (API Reference: Credit Card)

    Optional Attributes:
        - count (int)
        - interval (str)
    """

    # Optional
    count: int
    interval: str

    class Query(BaseQuery):
        """Installment class of Charge Query (API Reference: Credit Card)

        Used for create_authorization and create_charge

        Optional Attributes:
          - count (int)
          - interval (str)
        """

        # Optional
        count: int
        interval: str
