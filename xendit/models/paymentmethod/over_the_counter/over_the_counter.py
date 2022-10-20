from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery
from xendit.models.paymentmethod.over_the_counter.channel_properties import (
    ChannelProperties,
)


class OverTheCounter(BaseModel):
    """
    For type='OVER_THE_COUNTER', this contains the necessary information to describe an over-the-counter/retail outlet payment method.
    (API Reference: Payment Method)

    Attributes:
      - amount (float)
      - currency (str)
      - channel_code (str)
      - channel_properties (ChannelProperties)
    """

    amount: float
    currency: str
    channel_code: str
    channel_properties: ChannelProperties

    class Query(BaseQuery):
        """
        For type='OVER_THE_COUNTER', this contains the necessary information to describe an over-the-counter/retail outlet payment method.
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
