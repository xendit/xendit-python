from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery


class DirectDebitPaymentMethodProperties(BaseModel):
    """Payment Method Properties class in Direct Debit (API Reference: Direct Debit)

    Attributes:
      - id (str)

    """

    class Query(BaseQuery):
        """Payment Method Properties class in Direct Debit Query (API Reference: Direct Debit)

        Attributes:
        - id (str)

        """

        id: str
