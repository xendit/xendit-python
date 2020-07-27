from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery


class CardlessCreditShippingAddress(BaseModel):
    """Shipping address of Cardless Credit (API Reference: Cardless Credit)"""

    class Query(BaseQuery):
        """Item to be sent for Cardless Credit (API Reference: Cardless Credit)

        Use this to initialize create_payment

        Attributes:
        - first_name (str)
        - last_name (str)
        - address (str)
        - city (str)
        - postal_code (str)
        - phone (str)
        - country_code (str)

        """

        first_name: str
        last_name: str
        address: str
        city: str
        postal_code: str
        phone: str
        country_code: str
