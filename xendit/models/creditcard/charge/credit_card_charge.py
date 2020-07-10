from xendit.models._base_model import BaseModel
from .credit_card_charge_installment import CreditCardChargeInstallment
from .credit_card_charge_promotion import CreditCardChargePromotion


class CreditCardCharge(BaseModel):
    """Charge class (API Reference: Credit Card)

    Attributes:
      - created (str)
      - charge_type (str)
      - business_id (str)
      - authorized_amount (float)
      - external_id (str)
      - card_type (str)
      - merchant_id (str)
      - masked_card_number (str)
      - charge_type (str)
      - card_brand (str)
      - bank_reconciliation_id (str)
      - id (str)

    Optional Attributes:
      - eci (str)
      - capture_amount (float)
      - failure_reason (str)
      - approval_code (str)
      - merchant_reference_code (str)
      - descriptor (str)
      - currency (str)
      - mid_label (str)
      - promotion (CreditCardChargePromotion)
      - installment (CreditCardChargeInstallment)
    """

    created: str
    charge_type: str
    business_id: str
    authorized_amount: float
    external_id: str
    card_type: str
    merchant_id: str
    masked_card_number: float
    charge_type: str
    card_brand: str
    bank_reconciliation_id: str
    id: str

    # Optional
    eci: str
    capture_amount: float
    failure_reason: str
    approval_code: str
    merchant_reference_code: str
    descriptor: str
    currency: str
    mid_label: str
    promotion: CreditCardChargePromotion
    installment: CreditCardChargeInstallment
