from xendit.models._base_model import BaseModel

from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params

from xendit.xendit_error import XenditError


class RetailOutlet(BaseModel):
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

    owner_id: str
    external_id: str
    retail_outlet_name: str
    prefix: str
    name: str
    payment_code: str
    expected_amount: int
    is_single_use: bool
    expiration_Date: str
    id: str
    status: str
    type: str

    @staticmethod
    def create_fixed_payment_code(
        *,
        external_id,
        retail_outlet_name,
        name,
        expected_amount,
        payment_code=None,
        expiration_date=None,
        is_single_use=None,
        for_user_id=None,
        x_idempotency_key=None,
        x_api_version=None,
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
          - **for_user_id (str)
          - **x_idempotency_key (str)
          - **x_api_version (str): API Version that will be used. If not provided will default to the latest

        Returns:
          RetailOutlet

        Raises:
          XenditError

        """
        url = "/fixed_payment_code"
        headers, body = _extract_params(
            locals(),
            func_object=RetailOutlet.create_fixed_payment_code,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return RetailOutlet(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def update_fixed_payment_code(
        *,
        fixed_payment_code_id,
        name=None,
        expected_amount=None,
        expiration_date=None,
        for_user_id=None,
        x_idempotency_key=None,
        x_api_version=None,
        **kwargs,
    ):
        """Update fixed payment code (API Reference: Retail Outlets/Update Fixed Payment Code)

        Args:
          - fixed_payment_code_id (str)
          - **name (str)
          - **expected_amount (int)
          - **expiration_date (str) (ISO 8601 Date)
          - **for_user_id (str)
          - **x_idempotency_key (str)
          - **x_api_version (str): API Version that will be used. If not provided will default to the latest

        Returns:
          RetailOutlet

        Raises:
          XenditError

        """
        url = f"/fixed_payment_code/{fixed_payment_code_id}"
        headers, body = _extract_params(
            locals(),
            func_object=RetailOutlet.update_fixed_payment_code,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.patch(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return RetailOutlet(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def get_fixed_payment_code(
        *, fixed_payment_code_id, for_user_id=None, x_api_version=None, **kwargs
    ):
        """Get the detail of given Fixed Payment Code (API Reference: Retail Outlets/Get Fixed Payment Code)

        Args:
          - fixed_payment_code_id (str)
          - **for_user_id (str) (XenPlatforms only)
          - **x_api_version (str): API Version that will be used. If not provided will default to the latest

        Returns:
          RetailOutlet

        Raises:
          XenditError

        """
        url = f"/fixed_payment_code/{fixed_payment_code_id}"
        headers, _ = _extract_params(
            locals(),
            func_object=RetailOutlet.update_fixed_payment_code,
            headers_params=["for_user_id", "x_api_version"],
        )
        kwargs["headers"] = headers

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return RetailOutlet(**resp.body)
        else:
            raise XenditError(resp)
