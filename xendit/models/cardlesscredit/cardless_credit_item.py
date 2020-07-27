from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery


class CardlessCreditItem(BaseModel):
    """Item to be send for Cardless Credit (API Reference: Cardless Credit)"""

    class Query(BaseQuery):
        """Item to be sent for Cardless Credit (API Reference: Cardless Credit)

        Use this to initialize create_payment

        Attributes:
        - id (str)
        - name (str)
        - price (int)
        - type (str)
        - url (str)
        - quantity (int)

        """

        id: str
        name: str
        price: int
        type: str
        url: str
        quantity: int
