from xendit.models._base_model import BaseModel
from xendit.xendit_error import XenditError
from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params


class Payout(BaseModel):
    """Payout class (API Reference: Payout)

    Static Methods:
      - Payout.create (API Reference: /Create Payout)
      - Payout.get (API Reference: /Get Payout)
      - Payout.void (API Reference: /Void a Payout)

    Attributes:
      - id (str)
      - external_id (str)
      - amount (int)
      - merchant_name (str)
      - status (str)

    Optional Attributes:
      - expiration_timestamp (str)
      - createad (str)
      - payout_url (str)
      - email (str)
      - bank_code (str)
      - account_holder_name (str)
      - account_number (str)
      - disbursement_id (str)
      - failure_reason (str)
      - claimed_timestamp (str)
      - completed_timestamp (str)
      - failed_timestamp (str)
      - payment_id (str)
    """

    id: str
    external_id: str
    amount: int
    merchant_name: str
    status: str

    # Optional
    expiration_timestamp: str
    created: str
    payout_url: str
    email: str
    bank_code: str
    account_holder_name: str
    account_number: str
    disbursement_id: str
    failure_reason: str
    claimed_timestamp: str
    completed_timestamp: str
    failed_timestamp: str
    payment_id: str

    @staticmethod
    def create(
        *,
        external_id,
        amount,
        email,
        x_idempotency_key=None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Create a payout (API Reference: Payout/Create Payout)

        Args:
          - external_id (str)
          - amount (int)
          - email (str)
          - **for_user_id (str) (XenPlatform only)
          - **x_idempotency_key (str)
          - **x_api_version (str)

        Returns
          Payout

        Raises
          XenditError

        """
        url = "/payouts"
        headers, body = _extract_params(
            locals(),
            func_object=Payout.create,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return Payout(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def get(
        *, id, for_user_id=None, x_api_version=None, **kwargs,
    ):
        """Get payout (API Reference: Payout/Get Payout)

        Args:
          - id (str)
          - **for_user_id (str) (XenPlatform only)
          - **x_api_version (str)

        Returns
          Payout

        Raises
          XenditError

        """
        url = f"/payouts/{id}"
        headers, _ = _extract_params(
            locals(),
            func_object=Payout.get,
            headers_params=["for_user_id", "x_api_version"],
            ignore_params=["id"],
        )
        kwargs["headers"] = headers

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return Payout(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def void(
        *, id, x_idempotency_key=None, for_user_id=None, x_api_version=None, **kwargs,
    ):
        """Void a payout (API Reference: Payout/Void a Payout)

        Args:
          - id (str)
          - **for_user_id (str) (XenPlatform only)
          - **x_idempotency_key (str)
          - **x_api_version (str)

        Returns
          Payout

        Raises
          XenditError

        """
        url = f"/payouts/{id}/void"
        headers, body = _extract_params(
            locals(),
            func_object=Payout.void,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=["id"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return Payout(**resp.body)
        else:
            raise XenditError(resp)
