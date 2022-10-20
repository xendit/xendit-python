from xendit.models._base_model import BaseModel


class CardVerificationResults(BaseModel):
    """
    Contains the results of various checks done such as 3DS, CVV, and AVS.
    (API Reference: Payment Method)

    Attributes:
      - three_d_secure
      - cvv_result
      - address_verification_result
    """

    three_d_secure: dict
    cvv_result: str
    address_verification_result: str
