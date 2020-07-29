from xendit.models._base_model import BaseModel


class XenPlatformTransfers(BaseModel):
    """Transfers response object for xenPlatform (API Reference: xenPlatform)

    Attributes:
      - created (str)
      - transfer_id (str)
      - reference (str)
      - source_user_id (str)
      - destination_user_id (str)
      - status (str)
      - amount (str)
    """

    created: str
    transfer_id: str
    reference: str
    source_user_id: str
    destination_user_id: str
    status: str
    amount: str
