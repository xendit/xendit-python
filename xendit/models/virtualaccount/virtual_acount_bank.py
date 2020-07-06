from xendit.models._base_model import BaseModel


class VirtualAccountBank(BaseModel):
    """Bank class for Virtual Account (API Reference: Virtual Account)

    Attributes:
      - name (str)
      - code (str)
    """

    name: str
    code: str
