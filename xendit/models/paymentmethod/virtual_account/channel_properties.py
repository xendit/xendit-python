from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery


class ChannelProperties(BaseModel):
    """
    Information provided specific to the channel partner that was provided during the request
    (API Reference: Payment Method)

    Attributes:
      - customer_name (str)
      - virtual_account_number (str)
      - expires_at (str)
      - suggested_amount (float)

    """

    customer_name: str
    virtual_account_number: str
    expires_at: str
    suggested_amount: float

    class Query(BaseQuery):
        """
        Object that contains the information to generate a virtual account number
        (API Reference: Payment Method)

        Attributes
          - customer_name (str)
          - virtual_account_number (str)
          - expires_at (str)
          - suggested_amount (float)
        """

        customer_name: str
        virtual_account_number: str
        expires_at: str
        suggested_amount: float
