from xendit.models._base_model import BaseModel


class XenPlatformAccount(BaseModel):
    """Account response object for xenPlatform (API Reference: xenPlatform)

    Attributes:
      - created (str)
      - status (str)
      - account_email (str)
      - user_id (str)
      - type (str)
    """

    created: str
    status: str
    account_email: str
    user_id: str
    type: str
