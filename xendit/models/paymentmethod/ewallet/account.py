from xendit.models._base_model import BaseModel


class Account(BaseModel):
    """
    Details regarding the underlying e-wallet account as payment method

    Attributes:
      - name (str)
      - account_details (int)
      - balance (float)
      - point_balance (float)
    """

    name: str
    account_details: str
    balance: float
    point_balance: float
