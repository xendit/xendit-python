from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery


class XenPlatformBusinessProfile(BaseModel):
    """Business profile for xenPlatform (API Reference: xenPlatform)"""

    class Query(BaseQuery):
        """Business profile for xenPlatform (API Reference: xenPlatform)

        Use this to initialize create_batch

        Attributes:
        - business_name (str)

        """

        business_name: str
