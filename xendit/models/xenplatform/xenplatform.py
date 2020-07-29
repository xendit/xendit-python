from xendit.models._base_model import BaseModel
from xendit.xendit_error import XenditError
from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params

from .response import XenPlatformAccount, XenPlatformCallbackURL, XenPlatformTransfers
from .xenplatform_business_profile import XenPlatformBusinessProfile


class XenPlatform(BaseModel):
    """XenPlatform class (API Reference: xenPlatform)

    Static Methods:
      - XenPlatform.create_account (API Reference: /Create Account)
      - XenPlatform.set_callback_url (API Reference: /Set Callback URLs)
      - XenPlatform.transfers (API Reference: /Transfers)

    Static Methods for Object Creation:
      - XenPlatform.helper_create_business_profile (For BusinessProfile in create_account)
    """

    def helper_create_business_profile(
        *, business_name, **kwargs,
    ):
        """Construct xenPlatform business profile

        Args:
          - business_name (str)

        Return:
          - XenPlatformBusinessProfile
        """
        params = locals()
        del params["kwargs"]

        return XenPlatformBusinessProfile.Query(**params)

    @staticmethod
    def create_account(
        *,
        account_email,
        type,
        business_profile=None,
        x_idempotency_key=None,
        x_api_version=None,
        **kwargs,
    ):
        """Create a subaccount (API Reference: xenPlatform/Create Account)

        Args:
          - account_email (str)
          - type (XenPlatformAccountType)
          - **business_profile (XenPlatformBusinessType) (Required if type == OWNED)
          - **x_idempotency_key (str)
          - **x_api_version (str)

        Returns
          XenPlatformAccount

        Raises
          XenditError

        """
        type = XenPlatform._parse_type(type)
        url = "/accounts"
        headers, body = _extract_params(
            locals(),
            func_object=XenPlatform.create_account,
            headers_params=["x_idempotency_key", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return XenPlatformAccount(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def set_callback_url(
        *,
        type,
        url,
        x_idempotency_key=None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Set a callback URL (API Reference: xenPlatform/Set Callback URLs)

        Args:
          - type (XenPlatformURLType)
          - url (str)
          - **x_idempotency_key (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns
          XenPlatformCallbackURL

        Raises
          XenditError

        """
        type = XenPlatform._parse_type(type)
        headers, body = _extract_params(
            locals(),
            func_object=XenPlatform.set_callback_url,
            headers_params=["x_idempotency_key", "for_user_id", "x_api_version"],
            ignore_params=["type"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body
        url = f"/callback_urls/{type}"

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return XenPlatformCallbackURL(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def transfers(
        *,
        reference,
        amount,
        source_user_id,
        destination_user_id,
        x_idempotency_key=None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Transfers balance from sub-account to main account and vice versa (API Reference: xenPlatform/Transfers)

        Args:
          - reference (str)
          - amount (int)
          - source_user_id (str)
          - destination_user_id (str)
          - **x_idempotency_key (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns
          XenPlatformTransfers

        Raises
          XenditError

        """
        url = "/transfers"
        headers, body = _extract_params(
            locals(),
            func_object=XenPlatform.transfers,
            headers_params=["x_idempotency_key", "for_user_id", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return XenPlatformTransfers(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def _parse_type(enum_type):
        try:
            return enum_type.value
        except AttributeError:
            return enum_type
