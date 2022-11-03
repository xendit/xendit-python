from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery


class ChannelProperties(BaseModel):
    """
    Information provided specific to the channel partner that was provided during the request
    (API Reference: Payment Method)

    Attributes:
      - payment_code (str)
      - customer_name (str)
      - expires_at (str)
    """

    payment_code: str
    customer_name: str
    expires_at: str

    class Query(BaseQuery):
        """
        Object that contains the information to generate a valid payment code
        (API Reference: Payment Method)

        Attributes:
          - payment_code (str)
          - customer_name (str)
          - expires_at (str)
        """

        payment_code: str
        customer_name: str
        expires_at: str
