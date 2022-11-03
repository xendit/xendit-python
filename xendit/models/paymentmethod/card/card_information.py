from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery


class CardInformation(BaseModel):
    """
    Information pertaining to the card

    Attributes:
      - token_id (str)
      - masked_card_numer (str)
      - cardholder_name (str)
      - expiry_month (str)
      - expiry_year (str)
      - fingerprint (str)
      - type (str)
      - network (str)
      - country (str)
      - issuer (str)

    """

    token_id: str
    masked_card_number: str
    cardholder_name: str
    expiry_month: str
    expiry_year: str
    fingerprint: str
    type: str
    network: str
    country: str
    issuer: str

    class Query(BaseQuery):
        """
        Information pertaining to the card

        Attributes:
          - card_number (str)
          - expiry_month (str)
          - expiry_year (str)
          - cvv (str)

        """

        card_number: str
        expiry_month: str
        expiry_year: str
        cvv: str
