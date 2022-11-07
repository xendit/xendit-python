from typing import List

from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params
from xendit.models._base_model import BaseModel, BaseListModel
from xendit.models.paymentmethod.payment_method import PaymentMethod
from xendit.xendit_error import XenditError


class PaymentRequest(BaseModel):
    """PaymentRequest class (API Reference: PaymentRequests)

    Related Classes:
      - paymentmethod.PaymentMethod
      - payment.Payment
      - refund.Refund

    Static Methods:
      - PaymentRequest.create (API Reference: /Create Payment Request)
      - PaymentRequest.get (API Reference: /Get Payment Request by ID)
      - PaymentRequest.confirm (API Reference: /Confirm Payment Request)
      - PaymentRequest.resend_auth (API Reference: /Resend Auth for Payment Request)
      - PaymentRequest.list (API Reference: /Fetch Payment Requests)

    """

    id: str
    created: str
    type: str
    updated: str
    reference_id: str
    business_id: str
    customer_id: str
    amount: float
    country: str
    currency: str
    payment_method: PaymentMethod
    channel_properties: dict
    description: str
    failure_code: str
    capture_method: str
    initiator: str
    card_verification_results: dict
    status: str
    actions: List[dict]
    metadata: dict
    shipping_information: dict

    def create(
        *,
        currency: str,
        amount: float = None,
        reference_id: str = None,
        customer_id: str = None,
        country: str = None,
        description: str = None,
        payment_method: PaymentMethod.Query = None,
        payment_method_id: str = None,
        channel_properties: dict = None,
        metadata: dict = None,
        shipping_information: dict = None,
        capture_method: str = None,
        initiator: str = None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Send POST Request to create Payment Request
        (API Reference: Payment Requests/Create Payment Request)

        Args:
          - type (str)
          - reusability (str)
          - **reference_id (str)
          - **description (str)
          - **country (str)
          - **customer_id (str)
          - **payment_method (paymentmethod.PaymentRequest)
          - **payment_method_id (str)
          - **channel_properties (ChannelProperties)
          - **metadata (dict)
          - **shipping_information (dict)
          - **capture_method (str)
          - **initiator (str)
          - **for_user_id (str)
          - **x_api_version  (str)

        Returns:
          PaymentRequest

        Raises:
          XenditError
        """

        url = "/payment_requests"
        headers, body = _extract_params(
            locals(),
            func_object=PaymentRequest.create,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return PaymentRequest(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def get(
        *,
        payment_request_id: str,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Get Payment Request by Payment Request ID (API Reference: Payment Requests/Get Payment Request by ID)

        Args:
          - payment_request_id (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          PaymentRequest

        Raises:
          XenditError

        """
        url = f"/payment_requests/{payment_request_id}"
        headers, _ = _extract_params(
            locals(),
            func_object=PaymentRequest.get,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=["payment_request_id"],
        )
        kwargs["headers"] = headers

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return PaymentRequest(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def confirm(
        *,
        payment_request_id: str,
        auth_code: str,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """This endpoint only applies to BRI Direct Debit. This is only applicable for select payment DIRECT_DEBIT channels (BRI Direct Debit, BPI, RCBC, UBP, CHINABANK)
        This is used when an additional authorization (ex. OTP Validation, PIN validation) is required in order to successfully activate a payment method. This is equivalent to the POST - AUTH action provided when a Payment Method has the status REQUIRES_ACTION.
        (API Reference: Payment Requests/Confirm Payment Request)

        Args:
          - payment_request_id (str)
          - auth_code (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          PaymentRequest

        Raises:
          XenditError

        """
        url = f"/payment_requests/{payment_request_id}/auth"
        headers, body = _extract_params(
            locals(),
            func_object=PaymentRequest.confirm,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=["payment_request_id"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return PaymentRequest(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def resend_auth(
        *,
        payment_request_id: str,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """This endpoint only applies to BRI Direct Debit. This is only applicable for select payment DIRECT_DEBIT channels (BRI Direct Debit, BPI, UBP, CHINABANK)
        This is used when an additional authorization (ex. OTP Validation) is required in order to successfully activate a payment method. This is equivalent to the POST - AUTH action provided when a Payment Method has the status REQUIRES_ACTION.
        API Reference: Payment Requests/Resend Auth for Payment Request)

        Args:
          - payment_request_id (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          PaymentRequest

        Raises:
          XenditError

        """
        url = f"/payment_requests/{payment_request_id}/auth/resend"
        headers, _ = _extract_params(
            locals(),
            func_object=PaymentRequest.resend_auth,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=["payment_request_id"],
        )
        kwargs["headers"] = headers

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return PaymentRequest(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def list(
        *,
        after_id: str = None,
        before_id: str = None,
        channel_code: str = None,
        customer_id: str = None,
        payment_request_id: str = None,
        reusability: str = None,
        status: str = None,
        type: str = None,
        limit: int = None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """List retrieves an array of Payment Request objects that match the provided filter.
        An empty array [] will be returned if no records match the provided parameters.
        (API Reference: Payment Requests/Fetch Payment Requests)

        Args:
          - **after_id (str)
          - **before_id (str)
          - **channel_code (str)
          - **customer_id (str)
          - **payment_request_id (str)
          - **reusability (str)
          - **status (str)
          - **type (str)
          - **limit (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          PaymentRequest[]

        Raises:
          XenditError

        """
        url = "/payment_requests"
        headers, params = _extract_params(
            locals(),
            func_object=PaymentRequest.list,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=[],
        )
        kwargs["headers"] = headers
        kwargs["params"] = params

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            has_more = resp.body["has_more"]
            data = [PaymentRequest(**pm) for pm in resp.body["data"]]
            return PaymentRequestList(has_more=has_more, data=data)
        else:
            raise XenditError(resp)


class PaymentRequestList(BaseListModel):
    pass
