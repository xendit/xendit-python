from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery

from xendit.models.paymentmethod.ewallet.account import Account
from xendit.models.paymentmethod.ewallet.channel_properties import (
    ChannelProperties,
)


class EWallet(BaseModel):
    """
    For type='EWALLET', this contains the necessary information to describe an ewallet payment method.
    (API Reference: Payment Method)

    Attributes:
      - channel_code (str)
      - channel_properties (ChannelProperties.Query)
      - account (Account)
    """

    channel_code: str
    channel_properties: ChannelProperties
    account: Account

    class Query(BaseQuery):
        """
        For type='EWALLET', this contains the necessary information to describe an ewallet payment method.
        (API Reference: Payment Method)

        Attributes:
        - channel_code (str)
        - channel_properties (ChannelProperties.Query)
        """

        channel_code: str
        channel_properties: ChannelProperties.Query
