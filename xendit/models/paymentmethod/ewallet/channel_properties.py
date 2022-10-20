from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery


class ChannelProperties(BaseModel):
    """
    Information provided specific to the channel partner that was provided during the request
    (API Reference: Payment Method)

    Attributes:
      - success_return_url (str)
      - failure_return_url (int)
      - cancel_return_url (str)
      - mobile_number (str)
      - redeem_points (str)
      - cashtag (str)
    """

    success_return_url: str
    failure_return_url: str
    cancel_return_url: str
    mobile_number: str
    redeem_points: str
    cashtag: str

    class Query(BaseQuery):
        """
        Object that contains the information to authorize the e-wallet account for payments
        (API Reference: Payment Method)

        Attributes:
          - success_return_url (str)
          - failure_return_url (int)
          - cancel_return_url (str)
          - mobile_number (str)
          - redeem_points (str)
          - cashtag (str)

        """

        success_return_url: str
        failure_return_url: str
        cancel_return_url: str
        mobile_number: str
        redeem_points: str
        cashtag: str
