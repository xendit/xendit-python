from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery


class ChannelProperties(BaseModel):
    """
    Information provided specific to the channel partner that was provided during the request

    Attributes:
      - skip_three_d_secure (bool)
      - success_return_url (str)
      - failure_return_url (str)
      - cardonfile_type (str)
    """

    skip_three_d_secure: bool
    success_return_url: str
    failure_return_url: str
    cardonfile_type: str

    class Query(BaseQuery):
        """
        Object that contains the information to authorize the card for payments

        Attributes:
          - skip_three_d_secure (bool)
          - success_return_url (str)
          - failure_return_url (str)
          - cardonfile_type (str)

        """

        skip_three_d_secure: bool
        success_return_url: str
        failure_return_url: str
        cardonfile_type: str
