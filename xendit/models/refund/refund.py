from typing import List

from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params
from xendit.models._base_model import BaseModel, BaseListModel
from xendit.xendit_error import XenditError


class Refund(BaseModel):
    """Refund class (API Reference: Payment Method)

    Related Classes:
      - paymentrequest.PaymentRequest
      - payment.Payment

    Static Methods:
      - Refund.create (API Reference: /Create Refund)
      - Refund.get (API Reference: /Get Refund by ID)
      - Refund.list (API Reference: /Fetch Refunds)
    """

    id: str
    payment_request_id: str
    invoice_id: str
    payment_method_type: str
    reference_id: str
    country: str
    status: str
    channel_code: str
    reason: str
    failure_code: str
    refund_fee_amount: float
    created: str
    updated: str
    metadata: dict

    @staticmethod
    def create(
        *,
        payment_request_id: str = None,
        reference_id: str = None,
        invoice_id: str = None,
        currency: str = None,
        amount: float = None,
        reason: str = None,
        metadata: dict = None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Send POST Request to create Refund
        (API Reference: Refunds/Create Refund)

        Args:
          - **reference_id (str)
          - **payment_request_id (str)
          - **invoice_id (str)
          - **currency (str)
          - **amount (float)
          - **reason (str)
          - **metadata (dict)
          - **for_user_id (str)
          - **x_api_version  (str)

        Returns:
          Refund

        Raises:
          XenditError
        """

        url = "/refunds"
        headers, body = _extract_params(
            locals(),
            func_object=Refund.create,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return Refund(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def get(
        *,
        refund_id,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Get Refund by Refund ID (API Reference: Refunds/Get Refund by ID)

        Args:
          - refund_id (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          Refund

        Raises:
          XenditError

        """
        url = f"/refunds/{refund_id}"
        headers, _ = _extract_params(
            locals(),
            func_object=Refund.get,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=["refund_id"],
        )
        kwargs["headers"] = headers

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return Refund(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def list(
        *,
        payment_request_id: str = None,
        invoice_id: str = None,
        payment_method_type: str = None,
        channel_code: str = None,
        after_id: str = None,
        before_id: str = None,
        limit: int = None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """List retrieves an array of Payment Method objects that match the provided filter.
        An empty array [] will be returned if no records match the provided parameters.
        (API Reference: Payment Methods/Fetch Payment Methods)

        Args:
          - **payment_request_id (str)
          - **invoice_id (str)
          - **payment_method_type (str)
          - **channel_code (str)
          - **after_id (str)
          - **before_id (str)
          - **limit (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          Refund[]

        Raises:
          XenditError

        """
        url = "refunds"
        headers, params = _extract_params(
            locals(),
            func_object=Refund.list,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=[],
        )
        kwargs["headers"] = headers
        kwargs["params"] = params

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            has_more = resp.body["has_more"]
            data = [Refund(**pm) for pm in resp.body["data"]]
            return RefundList(has_more=has_more, data=data)
        else:
            raise XenditError(resp)


class RefundList(BaseListModel):
    pass
