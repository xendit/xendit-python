from xendit.models._base_model import BaseModel


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
      - promotion (?)
      - installment (?)
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

    class BillingDetails(BaseModel):
        """BillingDetails class of Charge (API Reference: Credit Card)

        Use this for initialize create_authorization and create_charge

        Attributes:
          - given_names (str)
          - address (CreditCardCharge.Address)

        Optional Attributes:
          - middle_name (str)
          - surname (str)
          - email (str)
          - mobile_number (str)
          - phone_number (str)

        """

        class Address(BaseModel):
            """Address class of Charge Billing Details (API Reference: Credit Card)

            Use this for initialize create_authorization and create_charge

            Attributes:
              - country (str)

            Optional Attributes:
              - street_line1 (str)
              - street_line2 (str)
              - city (str)
              - province (str)
              - state (str)
              - postal_code (str)
              - description (str)
            """

            country: str

            # Optional
            street_line1: str
            street_line2: str
            city: str
            province: str
            state: str
            postal_code: str
            description: str

        given_name: str
        address: Address

        # Optional
        middle_name: str
        surname: str
        email: str
        mobile_number: str
        phone_number: str

    class Installment(BaseModel):
        """Installment class of Charge (API Reference: Credit Card)

        Used for create_authorization and create_charge

        Optional Attributes:
          - count (int)
          - interval (str)
        """

        # Optional
        count: int
        interval: str

    class Promotion(BaseModel):
        """Promotion class of Credit Card Charge (API Reference: Credit Card)

        Used for create_authorization and create_charge

        Optional Attributes:
          - reference_id (str)
          - original_amount (float)
        """

        # Optional
        reference_id: str
        original_amount: int
