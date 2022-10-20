from lib2to3.pytree import Base
from typing import List
from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params
from xendit.models._base_model import BaseModel
from xendit.models.paymentmethod.billing_information import BillingInformation
from xendit.models.paymentmethod.card.card import Card

from xendit.models.paymentmethod.direct_debit.direct_debit import DirectDebit
from xendit.models.paymentmethod.ewallet.ewallet import EWallet
from xendit.models.paymentmethod.over_the_counter.over_the_counter import (
    OverTheCounter,
)
from xendit.models.paymentmethod.qr_code.qr_code import QRCode
from xendit.models.paymentmethod.virtual_account.virtual_account import (
    VirtualAccount,
)
from xendit.xendit_error import XenditError


class PaymentMethod(BaseModel):
    """PaymentMethod class (API Reference: Payment Method)

    Related Classes:
      - Card
      - DirectDebit
      - EWallet
      - OverTheCounter
      - QRCode
      - VirtualAccount

    Static Methods:
      - PaymentMethod.create (API Reference: /Create a payment method)
      - PaymentMethod.get (API Reference: /Get payment method information)
      - PaymentMethod.update (API Reference: /Update payment method information)
      - PaymentMethod.expire (API Reference: /Expire payment method)
      - PaymentMethod.authorize (API Reference: /Authorize payment method for activation)
      - PaymentMethod.list (API Reference: /Fetch matching payment methods)
    """

    id: str
    type: str
    country: str
    reusability: str
    customer_id: str
    reference_id: str
    description: str
    status: str
    card: Card
    direct_debit: DirectDebit
    ewallet: EWallet
    over_the_counter: OverTheCounter
    qr_code: QRCode
    virtual_account: VirtualAccount
    metadata: dict
    billing_information: BillingInformation
    failure_code: str
    created: str
    updated: str

    @staticmethod
    def create(
        *,
        type: str,
        reusability: str,
        reference_id: str = None,
        description: str = None,
        metadata: dict = None,
        country: str = None,
        customer_id: str = None,
        card: Card.Query = None,
        direct_debit: DirectDebit.Query = None,
        ewallet: EWallet.Query = None,
        over_the_counter: OverTheCounter.Query = None,
        qr_code: QRCode.Query = None,
        virtual_account: VirtualAccount.Query = None,
        billing_information: BillingInformation = None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Send POST Request to create Payment Method
        (API Reference: Unified Payments API/Create a payment method)

        Args:
          - type (str)
          - reusability (str)
          - **reference_id (str)
          - **description (str)
          - **metadata (dict)
          - **country (str)
          - **customer_id (str)
          - **card (Card.Query)
          - **direct_debit (DirectDebit.Query)
          - **ewallet (EWallet.Query)
          - **over_the_counter (OverTheCounter.Query)
          - **qr_code (QRCode.Query)
          - **virtual_account (VirtualAccount.Query)
          - **billing_information (BillingInformation)
          - **for_user_id (str)
          - **x_api_version  (str)

        Returns:
          PaymentMethod

        Raises:
          XenditError
        """

        url = "/v2/payment_methods"
        headers, body = _extract_params(
            locals(),
            func_object=PaymentMethod.create,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return PaymentMethod(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def get(
        *,
        payment_method_id,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Get Payment Method by Payment Method ID (API Reference: Unified Payments API/Get payment method information)

        Args:
          - payment_method_id (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          Payment Method

        Raises:
          XenditError

        """
        url = f"/v2/payment_methods/{payment_method_id}"
        headers, _ = _extract_params(
            locals(),
            func_object=PaymentMethod.get,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=["payment_method_id"],
        )
        kwargs["headers"] = headers

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return PaymentMethod(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def update(
        *,
        payment_method_id: str,
        description: str = None,
        status: str = None,
        reusability: str = None,
        reference_id: str = None,
        over_the_counter=OverTheCounter.Query,
        virtual_account=VirtualAccount.Query,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Update specific information of a particular Payment Method by Payment Method ID (API Reference: Unified Payments API/Update payment method information)

        Args:
          - payment_method_id (str)
          - **description (str)
          - **status (str)
          - **reusability (str)
          - **over_the_counter (OverTheCounter.Query)
          - **virtual_account (VirtualAccount.Query)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          PaymentMethod

        Raises:
          XenditError

        """
        url = f"/v2/payment_methods/{payment_method_id}"
        headers, body = _extract_params(
            locals(),
            func_object=PaymentMethod.update,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=["payment_method_id"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.patch(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return PaymentMethod(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def expire(
        *,
        payment_method_id: str,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Expire forces expiry or revokes authorization to an active Payment Method.
        For VIRTUAL_ACCOUNT, this will also set the expires_at to the current time. (API Reference: Unified Payments API/Expire payment method)

        Args:
          - payment_method_id (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          Payment Method

        Raises:
          XenditError

        """
        url = f"/v2/payment_methods/{payment_method_id}/expire"
        headers, _ = _extract_params(
            locals(),
            func_object=PaymentMethod.expire,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=["payment_method_id"],
        )
        kwargs["headers"] = headers

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return PaymentMethod(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def list(
        *,
        after_id: str = None,
        before_id: str = None,
        channel_code: str = None,
        customer_id: str = None,
        id: str = None,
        reusability: str = None,
        status: str = None,
        type: str = None,
        limit: int = None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """List retrieves an array of Payment Method objects that match the provided filter.
        An empty array [] will be returned if no records match the provided parameters.
        (API Reference: Unified Payments API/Fetch matching payment methods)

        Args:
          - **after_id (str)
          - **before_id (str)
          - **channel_code (str)
          - **customer_id (str)
          - **id (str)
          - **reusability (str)
          - **status (str)
          - **type (str)
          - **limit (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          PaymentMethod[]

        Raises:
          XenditError

        """
        url = "/v2/payment_methods"
        headers, params = _extract_params(
            locals(),
            func_object=PaymentMethod.list,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=[],
        )
        kwargs["headers"] = headers
        kwargs["params"] = params

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            has_more = resp.body["has_more"]
            data = [PaymentMethod(**pm) for pm in resp.body["data"]]
            return PaymentMethodList(has_more=has_more, data=data)
        else:
            raise XenditError(resp)

    @staticmethod
    def authorize(
        *,
        payment_method_id: str,
        auth_code: str,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Authorize is used when an additional authorization (ex. OTP Validation) is required in order to successfully activate a Payment Method.
        (API Reference: Unified Payments API/Authorize payment method for activation)

        Args:
          - payment_method_id (str)
          - auth_code (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          PaymentMethod

        Raises:
          XenditError
        """

        url = f"/v2/payment_methods/{payment_method_id}/auth"
        headers, body = _extract_params(
            locals(),
            func_object=PaymentMethod.authorize,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=["payment_method_id"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return PaymentMethod(**resp.body)
        else:
            raise XenditError(resp)


class PaymentMethodList(BaseModel):
    has_more: bool
    data: List[PaymentMethod]
