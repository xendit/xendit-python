from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery


class DirectDebitBasket(BaseModel):
    """Basket class in Direct Debit payment (API Reference: Direct Debit)

    Attributes:
      - reference_id (str)
      - name (str)
      - market (str)
      - type (str)
      - description (str)
      - category (str)
      - sub_category (str)
      - price (str)
      - url (str)
      - metadata (str)
      - quantity (str)
    """

    reference_id: str
    name: str
    market: str
    type: str
    description: str
    category: str
    sub_category: str
    price: str
    url: str
    metadata: str
    quantity: str

    class Query(BaseQuery):
        """Basket class in Direct Debit payment query (API Reference: Direct Debit)

        Use this for create_payment

        Attributes:
          - reference_id (str)
          - name (str)
          - market (str)
          - type (str)

        Optional Attributes:
          - description (str)
          - category (str)
          - sub_category (str)
          - price (str)
          - url (str)
          - metadata (str)
          - quantity (str)
        """

        reference_id: str
        name: str
        market: str
        type: str
        description: str
        category: str
        sub_category: str
        price: str
        url: str
        metadata: str
        quantity: str
