from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery

from xendit.models.paymentmethod.direct_debit.bank_account import BankAccount
from xendit.models.paymentmethod.direct_debit.channel_properties import (
    ChannelProperties,
)
from xendit.models.paymentmethod.direct_debit.debit_card import DebitCard


class DirectDebit(BaseModel):
    """
    For type='DIRECT_DEBIT', this contains the necessary information to describe a direct debit payment method.
    (API Reference: Payment Method)

    Attributes:
      - type (str)
      - channel_code (str)
      - channel_properties (ChannelProperties)
      - bank_account (BankAccount)
      - debit_card (DebitCard)
    """

    type: str
    channel_code: str
    channel_properties: ChannelProperties
    bank_account: BankAccount
    debit_card: DebitCard

    class Query(BaseQuery):
        """
        For type='DIRECT_DEBIT', this contains the necessary information to describe a direct debit payment method.
        (API Reference: Payment Method)

        Attributes:
          - type (str)
          - channel_code (str)
          - channel_properties (ChannelProperties.Query)
        """

        type: str
        channel_code: str
        channel_properties: ChannelProperties.Query
