import json

from .virtual_acount_bank import VirtualAccountBank
from .virtual_account_payment import VirtualAccountPayment

from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params

from xendit.xendit_error import XenditError


class VirtualAccount:
    """Virtual Account class (API Reference: Virtual Account)

    Related Classes:
      - VirtualAccountBanks
      - VirtualAccountPayment

    Static Methods:
      - VirtualAccount.create (API Reference: /Create Virtual Account)
      - VirtualAccount.get_banks (API Reference: /Get Virtual Account Banks)
      - VirtualAccount.get (API Reference: /Get Virtual Account)
      - VirtualAccount.update (API Reference: /Update Virtual Account)
      - VirtualAccount.get_payment (API Reference: /Get Virtual Account Payment)

    Attributes:
      - owner_id (str)
      - external_id (str)
      - bank_code (str)
      - merchant_code (str)
      - name (str)
      - account_number (str)
      - is_closed (bool)
      - id (str)
      - is_single_use (bool)
      - status (str)
      - expiration_date (str) (ISO 8601 Date)

    Optional Attributes:
      - suggested_amount (str)
      - expected_amount (str)
      - description (str)

    """

    def __init__(self, xendit_response):
        self.owner_id = xendit_response["owner_id"]
        self.external_id = xendit_response["external_id"]
        self.bank_code = xendit_response["bank_code"]
        self.merchant_code = xendit_response["merchant_code"]
        self.name = xendit_response["name"]
        self.account_number = xendit_response["account_number"]
        self.is_single_use = xendit_response["is_single_use"]
        self.status = xendit_response["status"]
        self.expiration_date = xendit_response["expiration_date"]
        self.is_closed = xendit_response["is_closed"]
        self.id = xendit_response["id"]

        if xendit_response.get("suggested_amount", None) is not None:
            self.suggested_amount = xendit_response["suggested_amount"]
        if xendit_response.get("expected_amount", None) is not None:
            self.expected_amount = xendit_response["expected_amount"]
        if xendit_response.get("description", None) is not None:
            self.description = xendit_response["description"]

    def __repr__(self):
        return json.dumps(vars(self), indent=4)

    @staticmethod
    def create(
        external_id,
        bank_code,
        name,
        virtual_account_number=None,
        suggested_amount=None,
        is_closed=None,
        expected_amount=None,
        expiration_date=None,
        is_single_use=None,
        description=None,
        for_user_id=None,
        x_idempotency_key=None,
        x_api_version=None,
        **kwargs,
    ):
        """Send POST Request to create VirtualAccount (API Reference: Virtual Account/Create Virtual Account)

        Args:
          - external_id (str)
          - bank_code (str)
          - name (str)
          - **virtual_account_number (str)
          - **suggested_amount (int)
          - **is_closed (bool)
          - **expected_amount (int)
          - **expiration_date (str) (ISO 8601 Date)
          - **is_single_use (bool)
          - **description (str)
          - **for_user_id (str) (XenPlatforms only)
          - **x_idempotency_key (str)
          - **x_api_version (str): API Version that will be used. If not provided will default to the latest

        Returns:
          VirtualAccount

        Raises:
          XenditError

        """
        url = "/callback_virtual_accounts"
        headers, body = _extract_params(
            locals(),
            func_object=VirtualAccount.create,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return VirtualAccount(resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def get_banks(for_user_id=None, x_api_version=None, **kwargs):
        """Get available banks (API Reference: Virtual Account/Get Virtual Account Banks)

        Args:
          - **for_user_id (str) (XenPlatforms only)
          - **x_api_version (str): API Version that will be used. If not provided will default to the latest

        Returns:
          List of VirtualAccountBank

        Raises:
          XenditError

        """
        url = "/available_virtual_account_banks"
        headers, _ = _extract_params(
            locals(),
            func_object=VirtualAccount.get_banks,
            headers_params=["for_user_id", "x_api_version"],
            ignore_params=["id"],
        )
        kwargs["headers"] = headers

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            virtual_account_banks = []
            for bank in resp.body:
                virtual_account_banks.append(VirtualAccountBank(bank))
            return virtual_account_banks
        else:
            raise XenditError(resp)

    @staticmethod
    def get(id, for_user_id=None, x_api_version=None, **kwargs):
        """Get the detail of Virtual Account (API Reference: Virtual Account/Get Virtual Account

        Args:
          - id (str)
          - **for_user_id (str) (XenPlatforms only)
          - **x_api_version (str): API Version that will be used. If not provided will default to the latest

        Returns:
          VirtualAccount

        Raises:
          XenditError
        """
        url = f"/callback_virtual_accounts/{id}"
        headers, _ = _extract_params(
            locals(),
            func_object=VirtualAccount.get,
            headers_params=["for_user_id", "x_api_version"],
            ignore_params=["id"],
        )
        kwargs["headers"] = headers

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return VirtualAccount(resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def update(
        id,
        suggested_amount=None,
        expected_amount=None,
        expiration_date=None,
        is_single_use=None,
        description=None,
        for_user_id=None,
        x_idempotency_key=None,
        x_api_version=None,
        **kwargs,
    ):
        """Update Virtual Account detail (API Reference: Virtual Account/Update Virtual Account

        Args:
          - id (str)
          - **suggested_amount (int)
          - **expected_amount (int)
          - **expiration_date (str) (ISO 8601 Date)
          - **is_single_use (bool)
          - **description (str)
          - **for_user_id (str) (XenPlatforms only)
          - **x_idempotency_key (str)
          - **x_api_version (str): API Version that will be used. If not provided will default to the latest

        Returns:
          VirtualAccount

        Raises:
          XenditError
        """
        url = f"/callback_virtual_accounts/{id}"
        headers, body = _extract_params(
            locals(),
            func_object=VirtualAccount.update,
            headers_params=["x_idempotency_key", "for_user_id", "x_api_version"],
            ignore_params=["id"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.patch(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return VirtualAccount(resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def get_payment(payment_id, for_user_id=None, x_api_version=None, **kwargs):
        """Get payment from virtual account (API Reference: Virtual Account/Get Virtual Account Payment

        Args:
          - payment_id (str)

        Returns:
          VirtualAccountPayment

        Raises:
          XenditError
        """
        url = f"/callback_virtual_account_payments/payment_id={payment_id}"
        headers, _ = _extract_params(
            locals(),
            func_object=VirtualAccount.get_payment,
            headers_params=["for_user_id", "x_api_version"],
            ignore_params=["payment_id"],
        )
        kwargs["headers"] = headers

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return VirtualAccountPayment(resp.body)
        else:
            raise XenditError(resp)
