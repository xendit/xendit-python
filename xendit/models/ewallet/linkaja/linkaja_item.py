from xendit.models._base_model import BaseModel


class LinkAjaItem(BaseModel):
    """Item Object for LinkAja (API Reference: eWallets)

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

    def __init__(self, id, name, price, quantity):
        dict.__init__(self, id=id, name=name, price=price, quantity=quantity)
