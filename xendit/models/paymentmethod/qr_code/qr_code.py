from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery
from xendit.models.paymentmethod.qr_code.channel_properties import (
    ChannelProperties,
)


class QRCode(BaseModel):
    """
    For type=QR_CODE, this contains the necessary information to describe an QR code payment method. This will be None otherwise.
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

    class Query(BaseQuery):
        """
        For type='QR_CODE', this contains the necessary information to describe a QR Code payment method.
        Note: A QR Code Payment method will only be ACTIVE and eligible for accepting payments with a corresponding valid Payment
        (API Reference: Payment Method)

        Attributes:
          - amount (float)
          - currency (str)
          - channel_code (str)
        """

        amount: float
        currency: str
        channel_code: str
