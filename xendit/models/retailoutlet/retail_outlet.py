import json

from xendit._api_requestor import _APIRequestor
from xendit._init_from_xendit_response import _init_from_xendit_response
from xendit._extract_params import _extract_params

from xendit.xendit_error import XenditError


class RetailOutlet:
    """RetailOutlet class (API Reference: Retail Outlets)

    Static Methods:
      - RetailOutlet.create_fixed_payment_code (API Reference: /Create Fixed Payment Code)
      - RetailOutlet.update_fixed_payment_code (API Reference: /Update Fixed Payment Code)
      - RetailOutlet.get_fixed_payment_code (API Reference: /Get Fixed Payment Code)

    Attributes:
      - owner_id (str)
      - external_id (str)
      - retail_outlet_name (str)
      - prefix (str)
      - name (str)
      - payment_code (str)
      - expected_amount (int)
      - is_single_use (bool)
      - expiration_date (str) (ISO 8601 Date)
      - id (str)

    """

    @_init_from_xendit_response(
        required=[
            "owner_id",
            "external_id",
            "retail_outlet_name",
            "prefix",
            "name",
            "payment_code",
            "expected_amount",
            "is_single_use",
            "expiration_date",
            "id",
        ],
    )
    def __init__(self, xendit_response):
        pass

    def __repr__(self):
        return json.dumps(vars(self), indent=4)

    @staticmethod
    def create_fixed_payment_code(
        external_id,
        retail_outlet_name,
        name,
        expected_amount,
        payment_code=None,
        expiration_date=None,
        is_single_use=None,
        x_idempotency_key=None,
        for_user_id=None,
        **kwargs,
    ):
        """Send POST Request to create fixed payment code (API Reference: Retail Outlets/Create Fixed Payment Code)

        Args:
          - external_id (str)
          - retail_outlet_name (str)
          - name (str)
          - expected_amount (int)
          - **payment_code (str)
          - **expiration_date (str) (ISO 8601 Date)
          - **is_single_use (bool)
          - **x_idempotency_key (str)
          - **for_user_id (str)

        Returns:
          RetailOutlet

        Raises:
          XenditError

        """
        url = "/fixed_payment_code"
        headers, body = _extract_params(
            locals(),
            func_object=RetailOutlet.create_fixed_payment_code,
            headers_params=["for_user_id", "x_idempotency_key"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body
        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return RetailOutlet(resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def update_fixed_payment_code(
        fixed_payment_code_id,
        name=None,
        expected_amount=None,
        expiration_date=None,
        x_idempotency_key=None,
        for_user_id=None,
        **kwargs,
    ):
        """Update fixed payment code (API Reference: Retail Outlets/Update Fixed Payment Code)

        Args:
          - fixed_payment_code_id (str)
          - **name (str)
          - **expected_amount (int)
          - **expiration_date (str) (ISO 8601 Date)
          - **x_idempotency_key (str)
          - **for_user_id (str)

        Returns:
          RetailOutlet

        Raises:
          XenditError

        """
        url = f"/fixed_payment_code/{fixed_payment_code_id}"
        headers, body = _extract_params(
            locals(),
            func_object=RetailOutlet.update_fixed_payment_code,
            headers_params=["for_user_id", "x_idempotency_key"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body
        resp = _APIRequestor.patch(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return RetailOutlet(resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def get_fixed_payment_code(fixed_payment_code_id, for_user_id=None, **kwargs):
        """Get the detail of given Fixed Payment Code (API Reference: Retail Outlets/Get Fixed Payment Code)

        Args:
          - fixed_payment_code_id (str)
          - **for_user_id (str) (XenPlatforms only)

        """
        url = f"/fixed_payment_code/{fixed_payment_code_id}"
        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return RetailOutlet(resp.body)
        else:
            raise XenditError(resp)
