from xendit.models._base_model import BaseModel


class XenPlatformCallbackURL(BaseModel):
    """Callback URL response object for xenPlatform (API Reference: xenPlatform)

    Attributes:
      - status (str)
      - user_id (str)
      - url (str)
      - environment (str)
      - callback_token (str)
    """

    status: str
    user_id: str
    url: str
    environment: str
    callback_token: str
