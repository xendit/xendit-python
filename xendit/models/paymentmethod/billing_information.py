from xendit.models._base_model import BaseModel


class BillingInformation(BaseModel):
    """
    Object containing information about the end-customer’s billing address.
    For cards, this is the billing information on record with the cardholder’s issuer.
    Recommended for 3DS 2 / AVS verification.

    Attributes:
      - country (str)
      - street_line1 (str)
      - street_line2 (str)
      - city (str)
      - province_state (str)
      - postal_code (str)
    """

    country: str
    street_line1: str
    street_line2: str
    city: str
    province_state: str
    postal_code: str
