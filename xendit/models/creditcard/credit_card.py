from xendit.models._base_model import BaseModel


class CreditCard(BaseModel):
    """CreditCard class (API Reference: CreditCard)

    Related Classes:
      - CreditCardReverseAuthorization
      - CreditCardCharge
      - CreditCardRefund
      - CreditCardPromotion
      - CreditCardPromotionCalculation

    Static Methods:
      - CreditCard.create_authorization (API Reference: /Create Authorization)
      - CreditCard.reverse_authorization (API Reference: /Reverse Authorization)
      - CreditCard.create_charge (API Reference: /Create Charge)
      - CreditCard.capture_charge (API Reference: /Capture Charge)
      - CreditCard.get_charge (API Reference: /Get Charge)
      - CreditCard.create_refund (API Reference: /Create Refund)
      - CreditCard.create_promotion (API Reference: /Create Promotion)
      - CreditCard.get_promotion (API Reference: /Get Prmotion)
      - CreditCard.get_promotion_calculation (API Reference: /Get Promotion Calculation)
    """
