from xendit.models._base_model import BaseModel


class EWalletCharge(BaseModel):
    """Detail for EWallet Charge (API Reference: eWallets)

    Attributes:
      - id (str) (prefix: ewc_ followed by UUIDv4)
      - business_id (str)
      - reference_id (str)
      - status (str)
      - currency (str) (ISO 4217)
      - charge_amount (int)
      - capture_amount (int)
      - checkout_method (str)
      - channel_code (str)
      - channel_properties (dict)
      - actions (str)
      - is_redirect_required (bool)
      - callback_url (str)
      - created (str) (ISO 8601)
      - updated (str) (ISO 8601)
      - voided_at (str) (ISO 8601)
      - capture_now (str)
      - customer_id (str)
      - payment_method_id (str)
      - failure_code (str)
      - basket (list)
      - metadata (dict)
    """

    id: str
    business_id: str
    reference_id: str
    status: str
    currency: str
    charge_amount: int
    capture_amount: int
    checkout_method: str
    channel_code: str
    channel_properties: dict
    actions: str
    is_redirect_required: bool
    callback_url: str
    created: str
    updated: str
    voided_at: str
    capture_now: str
    customer_id: str
    payment_method_id: str
    failure_code: str
    basket: list
    metadata: dict
