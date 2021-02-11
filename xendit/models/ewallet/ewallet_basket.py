from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery


class EWalletBasket(BaseModel):
    """Basket Class for EWallet (API Reference: eWallets)"""

    class Query(BaseQuery):
        """Basket Object for EWallet Query (API Reference: eWallets)

        Use this for create_ewallet_charge

        Attributes:
          - reference_id: str
          - name: str
          - category: str
          - currency: str
          - price: int
          - quantity: int
          - type: str
          - url: str
          - description: str
          - sub_category: str
          - metadata: dict
        """

        reference_id: str
        name: str
        category: str
        currency: str
        price: int
        quantity: int
        type: str
        url: str
        description: str
        sub_category: str
        metadata: dict
