import json

from .virtual_acount_banks import VirtualAccountBanks
from .virtual_account_payment import VirtualAccountPayment

from xendit._api_requestor import _APIRequestor
from xendit._init_from_xendit_response import _init_from_xendit_response

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

    @_init_from_xendit_response(
        required=[
            "owner_id",
            "external_id",
            "bank_code",
            "merchant_code",
            "name",
            "account_number",
            "is_single_use",
            "status",
            "expiration_date",
            "is_closed",
            "id",
        ],
        optional=["suggested_amount", "expected_amount", "description"],
    )
    def __init__(self, xendit_response):
        pass

    def __repr__(self):
        return json.dumps(vars(self), indent=4)

    @staticmethod
    def create(external_id, bank_code, name, **kwargs):
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

        Returns:
          VirtualAccount

        Raises:
          XenditError

        """
        url = "/callback_virtual_accounts"
        kwargs["external_id"] = external_id
        kwargs["bank_code"] = bank_code
        kwargs["name"] = name
        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return VirtualAccount(resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def get_banks(**kwargs):
        """Get available banks (API Reference: Virtual Account/Get Virtual Account Banks)

        Returns:
          VirtualAccountBanks

        Raises:
          XenditError

        """
        url = "/available_virtual_account_banks"
        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return VirtualAccountBanks(resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def get(id, **kwargs):
        """Get the detail of Virtual Account (API Reference: Virtual Account/Get Virtual Account

        Args:
          - id (str)

        Returns:
          VirtualAccount

        Raises:
          XenditError
        """
        url = f"/callback_virtual_accounts/{id}"
        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return VirtualAccount(resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def update(id, **kwargs):
        """Update Virtual Account detail (API Reference: Virtual Account/Update Virtual Account

        Args:
          - id (str)
          - **suggested_amount (int)
          - **expected_amount (int)
          - **expiration_date (str) (ISO 8601 Date)
          - **is_single_use (bool)
          - **description (str)

        Returns:
          VirtualAccount

        Raises:
          XenditError
        """
        url = f"/callback_virtual_accounts/{id}"
        resp = _APIRequestor.patch(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return VirtualAccount(resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def get_payment(payment_id, **kwargs):
        """Get payment from virtual account (API Reference: Virtual Account/Get Virtual Account Payment

        Args:
          - payment_id (str)

        Returns:
          VirtualAccountPayment

        Raises:
          XenditError
        """
        url = f"/callback_virtual_account_payments/payment_id={payment_id}"
        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return VirtualAccountPayment(resp.body)
        else:
            raise XenditError(resp)
