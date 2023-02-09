from .charge import (
    CreditCardCharge,
    CreditCardChargeAddress,
    CreditCardChargeBillingDetails,
    CreditCardChargeInstallment,
    CreditCardChargePromotion,
)

from .credit_card_promotion import CreditCardPromotion
from .credit_card_refund import CreditCardRefund
from .credit_card_reverse_authorization import CreditCardReverseAuthorization

from xendit.models._base_model import BaseModel

from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params

from xendit.xendit_error import XenditError


class CreditCard(BaseModel):
    """CreditCard class (API Reference: CreditCard)

    Related Classes:
      - CreditCardCharge
      - CreditCardChargeAddress
      - CreditCardChargeBillingDetails
      - CreditCardChargeInstallment
      - CreditCardChargePromotion

    Static Methods:
      - CreditCard.create_authorization (API Reference: /Create Authorization)
      - CreditCard.reverse_authorization (API Reference: /Reverse Authorization)
      - CreditCard.create_charge (API Reference: /Create Charge)
      - CreditCard.capture_charge (API Reference: /Capture Charge)
      - CreditCard.get_charge (API Reference: /Get Charge)
      - CreditCard.create_refund (API Reference: /Create Refund)
      - CreditCard.create_promotion (API Reference: /Create Promotion)

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
          - CreditCardChargeInstallment.Query
        """
        params = locals()
        del params["kwargs"]

        return CreditCardChargeInstallment.Query(**params)

    @staticmethod
    def helper_create_charge_promotion(
        *, reference_id=None, original_amount=None, **kwargs
    ):
        """Construct Promotion Object for Charge

        Args:
          - **reference_id (str)
          - **original_amount (float)

        Return:
          - CreditCardChargePromotion.Query
        """
        params = locals()
        del params["kwargs"]

        return CreditCardChargePromotion.Query(**params)

    @staticmethod
    def helper_create_billing_details(
        *,
        given_names,
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
          - given_names (str)
          - address (CreditCardCharge.Address)
          - **middle_name (str)
          - **surname (str)
          - **email (str)
          - **mobile_number (str)
          - **phone_number (str)

        Return:
          - CreditCardChargeBillingDetails.Query
        """
        params = locals()
        del params["kwargs"]

        return CreditCardChargeBillingDetails.Query(**params)

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
          - CreditCardChargeAddress.Query
        """
        params = locals()
        del params["kwargs"]

        return CreditCardChargeAddress.Query(**params)

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
        metadata=None,
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
          - **billing_details (CreditCardCharge.BillingDetails.Query)
          - **promotion (CreditCardCharge.Promotion.Query)
          - **installment (CreditCardCharge.Installment.Query)
          - **x_idempotency_key (str)
          - **for_user_id (str)
          - **x_api_version (str)
          - **metadata (dict)


        Returns:
          CreditCardCharge

        Raises:
          XenditError

        """
        params = locals()
        params = {**params, **kwargs}
        del params["kwargs"]

        return CreditCard.create_charge(**params)

    @staticmethod
    def reverse_authorization(
        *,
        credit_card_charge_id,
        external_id,
        x_idempotency_key=None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Send POST Request to reverse Credit Card Authorization (API Reference: Credit Card/Reverse Authorization)

        Args:
          - credit_card_charge_id (str)
          - external_id (str)
          - **x_idempotency_key (str)
          - **for_user_id (str)
          - **x_api_version

        Returns:
          CreditCardReverseAuthorization

        Raises:
          XenditError

        """
        url = f"/credit_card_charges/{credit_card_charge_id}/auth_reversal"
        headers, body = _extract_params(
            locals(),
            func_object=CreditCard.reverse_authorization,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=["credit_card_charge_id"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return CreditCardReverseAuthorization(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def create_charge(
        *,
        token_id,
        external_id,
        amount,
        capture=True,
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
        metadata=None,
        with_fee_rule=None,
        **kwargs,
    ):
        """Send POST Request to create Credit Card Charge (API Reference: Credit Card/Create Charge)

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
          - **billing_details (CreditCardCharge.BillingDetails.Query)
          - **promotion (CreditCardCharge.Promotion.Query)
          - **installment (CreditCardCharge.Installment.Query)
          - **x_idempotency_key (str)
          - **for_user_id (str) (XenPlatforms only)
          - **with_fee_rule (str) (XenPlatforms only)
          - **x_api_version (str)
          - **metadata (dict)

        Returns:
          CreditCardCharge

        Raises:
          XenditError

        """
        url = "/credit_card_charges"
        headers, body = _extract_params(
            locals(),
            func_object=CreditCard.create_charge,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version", "with_fee_rule"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return CreditCardCharge(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def capture_charge(
        *,
        credit_card_charge_id,
        amount,
        x_idempotency_key=None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Send POST Request to capture Credit Card Charge (API Reference: Credit Card/Capture Charge)

        Args:
          - credit_card_charge_id (str)
          - amount (str)
          - **x_idempotency_key (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          CreditCardCharge

        Raises:
          XenditError

        """
        url = f"/credit_card_charges/{credit_card_charge_id}/capture"
        headers, body = _extract_params(
            locals(),
            func_object=CreditCard.capture_charge,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=["credit_card_charge_id"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return CreditCardCharge(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def get_charge(
        *, credit_card_charge_id, for_user_id=None, x_api_version=None, **kwargs,
    ):
        """Get Detail of Credit Card Charge (API Reference: Credit Card/Get Charge)

        Args:
          - credit_card_charge_id (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          CreditCardCharge

        Raises:
          XenditError

        """
        url = f"/credit_card_charges/{credit_card_charge_id}"
        headers, _ = _extract_params(
            locals(),
            func_object=CreditCard.get_charge,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=["credit_card_charge_id"],
        )
        kwargs["headers"] = headers

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return CreditCardCharge(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def create_refund(
        *,
        credit_card_charge_id,
        amount,
        external_id,
        x_idempotency_key=None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Send POST Request to create refund for Credit Card (API Reference: Credit Card/Create Refund)

        Args:
          - credit_card_charge_id (str)
          - amount (str)
          - external_id (str)
          - **x_idempotency_key (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          CreditCardRefund

        Raises:
          XenditError

        """
        url = f"/credit_card_charges/{credit_card_charge_id}/refunds"
        headers, body = _extract_params(
            locals(),
            func_object=CreditCard.create_refund,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=["credit_card_charge_id"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return CreditCardRefund(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def create_promotion(
        *,
        reference_id,
        description,
        start_time,
        end_time,
        promo_code=None,
        bin_list=None,
        channel_code=None,
        discount_percent=None,
        discount_amount=None,
        currency=None,
        max_discount_amount=None,
        min_original_amount=None,
        x_idempotency_key=None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Send POST Request to create new Promotion (API Reference: Credit Card/Create Promotion)

        Args:
          - reference_id (str)
          - description (str)
          - start_time (str)
          - end_time (str)
          - **promo_code (str)
          - **bin_list (str[])
          - **channel_code (str)
          - **discount_percent (float)
          - **discount_amount (float)
          - **max_discount_amount (float)
          - **min_original_amount (float)
          - **currency (str)
          - **x_idempotency_key (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          CreditCardPromotion

        Raises:
          XenditError

        """
        url = "/promotions"
        headers, body = _extract_params(
            locals(),
            func_object=CreditCard.create_promotion,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return CreditCardPromotion(**resp.body)
        else:
            raise XenditError(resp)
