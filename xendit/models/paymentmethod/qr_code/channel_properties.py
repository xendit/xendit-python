from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery


class ChannelProperties(BaseModel):
    """
    Information provided specific to the channel partner that was provided during the request
    (API Reference: Payment Method)

    Attributes:
      - qr_string (str)
      - expires_at (str)
    """

    qr_string: str
    expires_at: str
