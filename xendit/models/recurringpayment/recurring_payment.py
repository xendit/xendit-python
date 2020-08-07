from xendit.models._base_model import BaseModel

from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params

from xendit.xendit_error import XenditError


class RecurringPayment(BaseModel):
    """RecurringPayment class (API Reference: RecurringPayment)

    Static Methods:
      - RecurringPayment.create (API Reference: /Create Recurring Payment)
      - RecurringPayment.get (API Reference: /Get Recurring Payment)
      - RecurringPayment.edit (API Reference: /Edit Recurring Payment)
      - RecurringPayment.stop (API Reference: /Stop Recurring Payment)
      - RecurringPayment.pause (API Reference: /Pause Recurring Payment)
      - RecurringPayment.resume (API Reference: /Resume Recurring Payment)

    Static Methods for Object Creation:
      - RecurringPayment.helper_create_installment (For Installment in create_authorization and create_charge)

    Attributes:
      - id (str)
      - user_id (str)
      - external_id (str)
      - status (str)
      - amount (float)
      - payer_email (str)
      - description (str)
      - should_send_email (bool)
      - interval (str)
      - interval_count (int)
      - recurrence_progress (int)
      - last_created_invoice_url (str)
      - credit_card_token (str)
      - created (str)
      - updated (str)
      - recharge (bool)
      - payment_method_id (str)

    Optional Attributes:
      - success_redirect_url (str)
      - failure_redirect_url (str)
      - invoice_duration (int)
      - charge_immediately (bool)
      - currency (str)
    """

    id: str
    user_id: str
    external_id: str
    status: str
    amount: float
    payer_email: str
    description: str
    should_send_email: bool
    interval: str
    interval_count: int
    recurrence_progress: int
    last_created_invoice_url: str
    credit_card_token: str
    created: str
    updated: str
    recharge: bool
    payment_method_id: str

    # Optional
    success_redirect_url: str
    failure_redirect_url: str
    invoice_duration: int
    charge_immediately: bool
    currency: str

    @staticmethod
    def create(
        *,
        external_id,
        payer_email,
        description,
        amount,
        interval,
        interval_count,
        total_recurrence=None,
        invoice_duration=None,
        should_send_email=None,
        missed_payment_action=None,
        credit_card_token=None,
        start_date=None,
        success_redirect_url=None,
        failure_redirect_url=None,
        recharge=None,
        charge_immediately=None,
        payment_method_id=None,
        currency=None,
        x_idempotency_key=None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Send POST Request to create refund for Credit Card (API Reference: Credit Card/Create Refund)

        Args:
          - external_id (str)
          - payer_email (str)
          - description (str)
          - amount (float)
          - interval (str)
          - interval_count (int)
          - **total_recurrence (int)
          - **invoice_duration (int)
          - **should_send_email (int)
          - **missed_payment_action (str)
          - **credit_card_token (str)
          - **start_date (str)
          - **success_redirect_url (str)
          - **failure_redirect_url (str)
          - **recharge (bool)
          - **charge_immediately (bool)
          - **payment_method_id (str)
          - **currency (str)
          - **x_idempotency_key (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          RecurringPayment

        Raises:
          XenditError

        """
        url = "/recurring_payments"
        headers, body = _extract_params(
            locals(),
            func_object=RecurringPayment.create,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return RecurringPayment(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def get(
        *, id, for_user_id=None, x_api_version=None, **kwargs,
    ):
        """Get Recurring Payment by ID (API Reference: Recurring Payment/Get Recurring Payment)

        Args:
          - id (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          RecurringPayment

        Raises:
          XenditError

        """
        url = f"/recurring_payments/{id}"
        headers, _ = _extract_params(
            locals(),
            func_object=RecurringPayment.get,
            headers_params=["for_user_id", "x_api_version"],
        )
        kwargs["headers"] = headers

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return RecurringPayment(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def edit(
        *,
        id,
        amount=None,
        credit_card_token=None,
        interval=None,
        interval_count=None,
        should_send_email=None,
        invoice_duration=None,
        missed_payment_action=None,
        payment_method_id=None,
        customer_id=None,
        x_idempotency_key=None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Edit Recurring Payment Data (API Reference: Recurring Payment/Edit Recurring Payment)

        Args:
          - id (str)
          - **amount (int)
          - **credit_card_token (str)
          - **interval (str)
          - **interval_count (int)
          - **should_send_email (bool)
          - **invoice_duration (int)
          - **missed_payment_action (str)
          - **payment_method_id (str)
          - **customer_id (str)
          - **x_idempotency_key (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          RecurringPayment

        Raises:
          XenditError

        """
        url = f"/recurring_payments/{id}"
        headers, body = _extract_params(
            locals(),
            func_object=RecurringPayment.edit,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=["id"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.patch(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return RecurringPayment(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def stop(
        *, id, x_idempotency_key=None, for_user_id=None, x_api_version=None, **kwargs,
    ):
        """Stop Recurring Payment (API Reference: Recurring Payment/Stop Recurring Payment)

        Args:
          - id (str)
          - **x_idempotency_key (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          RecurringPayment

        Raises:
          XenditError

        """
        url = f"/recurring_payments/{id}/stop!"
        headers, body = _extract_params(
            locals(),
            func_object=RecurringPayment.stop,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=["id"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return RecurringPayment(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def pause(
        *, id, x_idempotency_key=None, for_user_id=None, x_api_version=None, **kwargs,
    ):
        """Pause Recurring Payment (API Reference: Recurring Payment/Pause Recurring Payment)

        Args:
          - id (str)
          - **x_idempotency_key (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          RecurringPayment

        Raises:
          XenditError

        """
        url = f"/recurring_payments/{id}/pause!"
        headers, body = _extract_params(
            locals(),
            func_object=RecurringPayment.stop,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=["id"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return RecurringPayment(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def resume(
        *, id, x_idempotency_key=None, for_user_id=None, x_api_version=None, **kwargs,
    ):
        """Pause Recurring Payment (API Reference: Recurring Payment/Pause Recurring Payment)

        Args:
          - id (str)
          - **x_idempotency_key (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          RecurringPayment

        Raises:
          XenditError

        """
        url = f"/recurring_payments/{id}/resume!"
        headers, body = _extract_params(
            locals(),
            func_object=RecurringPayment.stop,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=["id"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return RecurringPayment(**resp.body)
        else:
            raise XenditError(resp)
