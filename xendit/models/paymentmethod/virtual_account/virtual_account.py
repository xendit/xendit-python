from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery
from xendit.models.paymentmethod.virtual_account.channel_properties import (
    ChannelProperties,
)


class VirtualAccount(BaseModel):
    """
    For type=VIRTUAL_ACCOUNT, this contains the necessary information to describe a virtual account payment method. This will be None otherwise.
    (API Reference: Payment Method)

    Attributes:
      - amount (float)
      - min_amount (float)
      - max_amount (float)
      - currency (str)
      - channel_code (str)
      - channel_properties (ChannelProperties)
    """

    amount: float
    min_amount: float
    max_amount: float
    currency: str
    channel_code: str
    channel_properties: ChannelProperties

    class Query(BaseQuery):
        """
        For type='VIRTUAL_ACCOUNT', this contains the necessary information to describe a virtual account payment method.
        (API Reference: Payment Method)

        Attributes:
          - amount (float)
          - currency (str)
          - channel_code (str)
          - channel_properties (ChannelProperties.Query)
        """

        amount: float
        currency: str
        channel_code: str
        channel_properties: ChannelProperties.Query
