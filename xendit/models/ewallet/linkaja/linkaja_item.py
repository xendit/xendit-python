from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery


class LinkAjaItem(BaseModel):
    """Item Class for LinkAja (API Reference: eWallets)"""

    class Query(BaseQuery):
        """Item Object for LinkAja Query (API Reference: eWallets)

        Use this for create_linkaja_payment

        Attributes:
          - id (str)
          - name (str)
          - price (int)
          - quantity (int)
        """

        id: str
        name: str
        price: int
        quantity: int
