from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery
from xendit.models.paymentmethod.card.card_verification_results import (
    CardVerificationResults,
)
from xendit.models.paymentmethod.card.card_information import CardInformation
from xendit.models.paymentmethod.card.channel_properties import ChannelProperties


class Card(BaseModel):
    """
    For type=CARD, this contains the necessary information to describe a card payment method. This will be None otherwise.
    (API Reference: Payment Method)

    Attributes:
      - currency (str)
      - channel_properties (ChannelProperties)
      - card_information (CardInformation)
      - card_verification_results (CardVerificationResults)

    """

    currency: str
    channel_properties: ChannelProperties
    card_information: CardInformation
    card_verification_results: CardVerificationResults

    class Query(BaseQuery):
        """
        For type='CARD', this contains the necessary information to describe a virtual account payment method.
        (API Reference: Payment Method)

        Attributes:
          - currency (str)
          - channel_properties (ChannelProperties.Query)
          - card_information (CardInformation.Query)
        """

        currency: str
        channel_properties: ChannelProperties.Query
        card_information: CardInformation.Query
