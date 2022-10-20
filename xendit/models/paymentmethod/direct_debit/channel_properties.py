from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery


class ChannelProperties(BaseModel):
    """
    Information provided specific to the channel partner that was provided during the request
    (API Reference: Payment Method)

    Attributes:
      - success_return_url (str)
      - failure_return_url (str)
      - mobile_number (int)
      - card_last_four (str)
      - card_expiry (str)
      - email (str)
      - require_auth (bool)
    """

    success_return_url: str
    failure_return_url: str
    mobile_number: str
    card_last_four: str
    card_expiry: str
    email: str
    require_auth: bool

    class Query(BaseQuery):
        """
        Object that contains the information to authorize the direct debit account for payments
        (API Reference: Payment Method)

        Attributes:
        - success_return_url (str)
        - failure_return_url (str)
        - mobile_number (int)
        - card_last_four (str)
        - card_expiry (str)
        - email (str)
        - require_auth (bool)
        """

        success_return_url: str
        failure_return_url: str
        mobile_number: str
        card_last_four: str
        card_expiry: str
        email: str
        require_auth: bool
