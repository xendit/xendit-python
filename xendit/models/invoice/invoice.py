from typing import List

from xendit.models._base_model import BaseModel

from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params

from xendit.xendit_error import XenditError

from .invoice_bank import InvoiceBank
from .invoice_retail_outlet import InvoiceRetailOutlet


class Invoice(BaseModel):
    """Invoice class (API Reference: Invoice)

    Related Classes:
      - InvoiceBank

    Static Methods:
      - Invoice.create (API Reference: /Create Invoice)
      - Invoice.get (API Reference: /Get Invoice)
      - Invoice.expire (API Reference: /Expire Invoice)
      - Invoice.list_all (API Reference: /List All Invoice)

    Attributes:
      - id (str)
      - external_id (str)
      - user_id (str)
      - status (str)
      - merchant_name (str)
      - merchant_profile_picture_url (str)
      - customer (object)
      - amount (int)
      - payer_email (str)
      - description (str)
      - expiry_date (str)
      - invoice_url (str)
      - available_banks (InvoiceBank[])
      - available_ewallets (?)
      - should_exclude_credit_card (bool)
      - should_send_email (bool)
      - created (str)
      - updated (str)
      - currency (str)

    """

    id: str
    external_id: str
    user_id: str
    status: str
    merchant_name: str
    merchant_profile_picture_url: str
    customer: object
    amount: int
    payer_email: str
    description: str
    invoice_url: str
    expiry_date: str
    available_banks: List[InvoiceBank]
    available_ewallets: List[None]
    available_retail_outlets: List[InvoiceRetailOutlet]
    should_exclude_credit_card: bool
    should_send_email: bool
    created: str
    updated: str
    currency: str

    @staticmethod
    def create(
        *,
        external_id,
        payer_email,
        description,
        amount,
        customer=None,
        should_send_email=None,
        callback_virtual_account_id=None,
        invoice_duration=None,
        success_redirect_url=None,
        failure_redirect_url=None,
        payment_methods=None,
        mid_label=None,
        currency=None,
        fixed_va=None,
        reminder_time=None,
        fees=None,
        items=None,
        for_user_id=None,
        x_idempotency_key=None,
        x_api_version=None,
        **kwargs,
    ):
        """Send POST Request to create Invoice (API Reference: Invoice/Create Invoice)

        Args:
          - external_id (str)
          - payer_email (str)
          - description (str)
          - amount (int)
          - **customer (object)
          - **should_send_email (bool)
          - **callback_virtual_account_id (str)
          - **invoice_duration (int)
          - **success_redirect_url (str)
          - **failure_redirect_url (str)
          - **payment_methods (str[])
          - **mid_label (str)
          - **currency (str)
          - **fixed_va (bool)
          - **reminder_time (int)
          - **fees (object[])
          - **items (object[])
          - **for_user_id (str) (XenPlatforms only)
          - **x_idempotency_key (str)
          - **x_api_version (str): API Version that will be used. If not provided will default to the latest

        Returns:
          Invoice

        Raises:
          XenditError

        """
        url = "/v2/invoices"
        headers, body = _extract_params(
            locals(),
            func_object=Invoice.create,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return Invoice(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def get(
        *, invoice_id, for_user_id=None, x_api_version=None, **kwargs,
    ):
        """Get Invoice (API Reference: Invoice/Get Invoice)

        Args:
          - invoice_id (str)
          - **for_user_id (str)
          - **x_api_version (str): API Version that will be used. If not provided will default to the latest

        Returns:
          Invoice

        Raises:
          XenditError

        """
        url = f"/v2/invoices/{invoice_id}"
        headers, _ = _extract_params(
            locals(),
            func_object=Invoice.get,
            headers_params=["for_user_id", "x_api_version"],
            ignore_params=["invoice_id"],
        )
        kwargs["headers"] = headers

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return Invoice(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def expire(
        *,
        invoice_id,
        for_user_id=None,
        x_idempotency_key=None,
        x_api_version=None,
        **kwargs,
    ):
        """Cancel an already created invoice (API Reference: Invoice/Expire Invoice)

        Args:
          - invoice_id (str)
          - **for_user_id (str)
          - **x_idempotency_key (str)
          - **x_api_version (str): API Version that will be used. If not provided will default to the latest

        Returns:
          Invoice

        Raises:
          XenditError

        """
        url = f"/invoices/{invoice_id}/expire!"
        headers, body = _extract_params(
            locals(),
            func_object=Invoice.expire,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=["invoice_id"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return Invoice(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def list_all(
        *,
        statuses=None,
        limit=None,
        created_after=None,
        created_before=None,
        paid_after=None,
        paid_before=None,
        expired_after=None,
        expired_before=None,
        last_invoice_id=None,
        client_types=None,
        payment_channels=None,
        on_demand_link=None,
        recurring_payment_id=None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """List all Invoice based on filter (API Reference: Invoice/List All Invoice)

        Args:
          - statuses (str[])
          - limit (int)
          - created_after (str)
          - created_before (str)
          - paid_after (str)
          - paid_before (str)
          - expired_after (str)
          - expired_before (str)
          - last_invoice_id (str)
          - client_types (str[])
          - payment_channels (str[])
          - on_demand_link (str)
          - recurring_payment_id (str)
          - **for_user_id (str)
          - **x_api_version (str): API Version that will be used. If not provided will default to the latest

        Returns:
          Invoice

        Raises:
          XenditError

        """
        url = "/v2/invoices"
        headers, params = _extract_params(
            locals(),
            func_object=Invoice.list_all,
            headers_params=["for_user_id", "x_api_version"],
            ignore_params=[],
        )
        kwargs["headers"] = headers
        kwargs["params"] = params

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            invoices = []
            for invoice in resp.body:
                invoices.append(Invoice(**invoice))
            return invoices
        else:
            raise XenditError(resp)
