from xendit.models._base_model import BaseModel
from xendit.xendit_error import XenditError
from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params


class CardlessCredit(BaseModel):
    """CardlessCredit class (API Reference: CardlessCredit)

    Static Methods:
      - CardlessCredit.create_payment (API Reference: /Create Payment or Generate Checkout URL)
      - CardlessCredit.calculate_payment_type (API Reference: /Get Payment Status)
    """

    id: str

    # Optional
    expiration_timestamp: str

    @staticmethod
    def create_payment(
        *, x_idempotency_key=None, for_user_id=None, x_api_version=None, **kwargs,
    ):
        """Create a cardless credit payment (API Reference: Cardless Credit/Create Payment or Generate Checkout URL)

        Args:
          - **for_user_id (str) (XenPlatform only)
          - **x_idempotency_key (str)
          - **x_api_version (str)

        Returns
          CardlessCredit

        Raises
          XenditError

        """
        url = "/cardless-credit"
        headers, body = _extract_params(
            locals(),
            func_object=CardlessCredit.create_payment,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return CardlessCredit(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def calculate_payment_type(
        *, x_idempotency_key=None, for_user_id=None, x_api_version=None, **kwargs,
    ):
        """Calculate Payment Types feature helps merchants to get an accurate value of the installment offered to end customers by the cardless credit provider
        (API Reference: Cardless Credit/Calculate Payment Types)

        Args:
          -
          - **for_user_id (str) (XenPlatform only)
          - **x_idempotency_key (str)
          - **x_api_version (str)

        Returns
          CardlessCredit

        Raises
          XenditError

        """
        url = "/cardless-credit/payment-types"
        headers, body = _extract_params(
            locals(),
            func_object=CardlessCredit.calculate_payment_type,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return CardlessCredit(**resp.body)
        else:
            raise XenditError(resp)
