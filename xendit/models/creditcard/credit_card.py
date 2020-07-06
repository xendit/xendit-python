from .charge import CreditCardCharge

from xendit.models._base_model import BaseModel

from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params

from xendit.xendit_error import XenditError


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

    Static Methods for Object Creation:
      - CreditCard.helper_create_installment (For Installment in create_authorization and create_charge)
      - CreditCard.helper_create_charge_promotion (For Promotion in create_authorization and create_charge)
      - CreditCard.helper_create_billing_details (For BillingDetails in create_authorization and create_charge)
      - CreditCard.helper_create_address (For Address in create_billing_details)
    """

    @staticmethod
    def helper_create_installment(*, count=None, interval=None, **kwargs):
        """Construct Installments Object for Charge

        Args:
          - **count (int)
          - **interval (str)

        Return:
          - CreditCardCharge.Installment
        """
        params = locals()

        return CreditCardCharge.Installment(**params)

    @staticmethod
    def helper_create_charge_promotion(
        *, reference_id=None, original_amount=None, **kwargs
    ):
        """Construct Promotion Object for Charge

        Args:
          - **reference_id (str)
          - **original_amount (float)

        Return:
          - CreditCardCharge.Promotion
        """
        params = locals()

        return CreditCardCharge.Promotion(**params)

    @staticmethod
    def helper_create_billing_details(
        *,
        given_name,
        address,
        middle_name=None,
        surname=None,
        email=None,
        mobile_number=None,
        phone_number=None,
        **kwargs,
    ):
        """Construct Billing Details Object for Charge

        Args:
          - given_name (str)
          - address (CreditCardCharge.Address)
          - **middle_name (str)
          - **surname (str)
          - **email (str)
          - **mobile_number (str)
          - **phone_number (str)

        Return:
          - CreditCardCharge.BillingDetails
        """
        params = locals()

        return CreditCardCharge.BillingDetails(**params)

    @staticmethod
    def helper_create_address(
        *,
        country,
        street_line1=None,
        street_line2=None,
        city=None,
        province=None,
        state=None,
        postal_code=None,
        description=None,
        **kwargs,
    ):
        """Construct Address Object for Billing Details

        Args:
          - country (str)
          - **street_line1 (str)
          - **street_line2 (str)
          - **city (str)
          - **province (str)
          - **state (str)
          - **postal_code (str)
          - **description (str)

        Return:
          - CreditCardCharge.Address
        """
        params = locals()

        return CreditCardCharge.Address(**params)

    @staticmethod
    def create_authorization(
        *,
        token_id,
        external_id,
        amount,
        capture=False,
        authentication_id=None,
        card_cvn=None,
        descriptor=None,
        currency=None,
        mid_label=None,
        billing_details=None,
        promotion=None,
        installment=None,
        x_idempotency_key=None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Send POST Request to create Credit Card Authorization (API Reference: Credit Card/Create Authorization)

        Args:
          - token_id (str)
          - external_id (str)
          - amount (float)
          - authentication_id (str)
          - card_cvn (str)
          - **capture (bool)
          - **descriptor (str)
          - **currency (str)
          - **mid_label (str)
          - **billing_details (CreditCardCharge.BillingDetails)
          - **promotion (CreditCardCharge.Promotion)
          - **installment (CreditCardCharge.Installment)

        Returns:
          CreditCardCharge

        Raises:
          XenditError

        """
        url = "/credit_card_charge"
        headers, body = _extract_params(
            locals(),
            func_object=CreditCard.create_authorization,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return CreditCardCharge(**resp.body)
        else:
            raise XenditError(resp)
