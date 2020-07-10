from .customer import DirectDebitCustomer, DirectDebitCustomerAddress
from .token import DirectDebitCardLink, DirectDebitOnlineBankingLink, DirectDebitToken
from xendit.models._base_model import BaseModel

from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params

from xendit.xendit_error import XenditError


class DirectDebit(BaseModel):
    """DirectDebit class (API Reference: Direct Debit)

    Related Classes:
      - DirectDebitCustomer
      - DirectDebitCustomerAddress
      - DirectDebitCardLink
      - DirectDebitOnlineBankingLinking
      - DirectDebitToken

    Static Methods:
      - DirectDebit.create_customer (API Reference: /Create Customer)
      - DirectDebit.get_customer_by_ref_id (API Reference: /Get Customer by Reference ID)
      - DirectDebit.initialize_tokenization (API Reference: /Initialize Linked Account Tokenization)
      - DirectDebit.validate_token_otp (API Reference: /Validate OTP for Linked Account Token)
      - DirectDebit.get_accessible_account_by_token (API Reference: /Retrieve Accessible Accounts by Linked Account Token)

    Static Methods for Object Creation:
      - DirectDebit.helper_create_customer_address (For Address in create_customer)
      - DirectDebit.helper_create_online_banking_link (For OnlineBankingLink in initialize_tokenization)
      - DirectDebit.helper_create_card_link (For CardLink in initialize_tokenization)
    """

    @staticmethod
    def helper_create_customer_address(
        *,
        country,
        street_line1=None,
        street_line2=None,
        city=None,
        province=None,
        state=None,
        postal_code=None,
        **kwargs,
    ):
        """Construct Address Object for DirectDebit Customer

        Args:
          - country (str)
          - **street_line1 (str)
          - **street_line2 (str)
          - **city (str)
          - **province (str)
          - **state (str)
          - **postal_code (str)

        Return:
          - DirectDebitCustomerAddress
        """
        params = locals()
        del params["kwargs"]

        return DirectDebitCustomerAddress.Query(**params)

    @staticmethod
    def helper_create_online_banking_link(
        *, success_redirect_url, failure_redirect_url=None, callback_url=None, **kwargs,
    ):
        """Construct OnlineBankingLink Object for DirectDebit Token

        Args:
          - success_redirect_url (str)
          - failure_redirect_url (str)
          - callback_url (str)

        Return:
          - DirectDebitOnlineBankingLink
        """
        params = locals()
        del params["kwargs"]

        return DirectDebitOnlineBankingLink.Query(**params)

    @staticmethod
    def helper_create_card_link(
        *, account_mobile_number, card_last_four, card_expiry, account_email, **kwargs,
    ):
        """Construct CardLink Object for DirectDebit Token

        Args:
          - account_mobile_number (str)
          - card_last_four (str)
          - card_expiry (str)
          - account_email (str)

        Return:
          - DirectDebitCardLink.Query
        """
        params = locals()
        del params["kwargs"]

        return DirectDebitCardLink.Query(**params)

    @staticmethod
    def create_customer(
        *,
        reference_id,
        given_names,
        mobile_number=None,
        email=None,
        middle_name=None,
        surname=None,
        description=None,
        phone_number=None,
        nationality=None,
        addresses=None,
        date_of_birth=None,
        metadata=None,
        x_idempotency_key=None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Send POST Request to create Customer (API Reference: Direct Debit/Create Customer)

        Args:
          - reference_id (str)
          - given_names (str)
          - **mobile_number (str) (Either mobile_number or email must be present)
          - **email (Either mobile_number or email must be present)
          - **middle_name (str)
          - **surname (str)
          - **description (str)
          - **phone_number (str)
          - **nationality (str)
          - **addresses (DirectDebitCustomerAddress[])
          - **date_of_birth (str)
          - **metadata (dict)
          - **for_user_id (str)
          - **x_idempotency_key (str)
          - **x_api_version (str)

        Returns:
          DirectDebitCustomer

        Raises:
          XenditError

        """
        url = "/customers"
        headers, body = _extract_params(
            locals(),
            func_object=DirectDebit.create_customer,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return DirectDebitCustomer(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def get_customer_by_ref_id(
        *, reference_id, for_user_id=None, x_api_version=None, **kwargs,
    ):
        """Get Customer by Reference ID (API Reference: Direct Debit/Get Customer by Reference ID)

        Args:
          - reference_id (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          DirectDebitCustomer

        Raises:
          XenditError

        """
        url = f"/customers?reference_id={reference_id}"
        headers, _ = _extract_params(
            locals(),
            func_object=DirectDebit.get_customer_by_ref_id,
            headers_params=["for_user_id", "x_api_version"],
            ignore_params=["reference_id"],
        )
        kwargs["headers"] = headers

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            customers = []
            for customer in resp.body:
                customers.append(DirectDebitCustomer(**customer))
            return customers
        else:
            raise XenditError(resp)

    @staticmethod
    def initialize_tokenization(
        *,
        customer_id,
        channel_code,
        properties=None,
        metadata=None,
        x_idempotency_key=None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Initialize Authorization Process and Account Token Creation
        (API Reference: Direct Debit/Initialize Linked Account Tokenization)

        Args:
          - customer_id (str)
          - channel_code (str)
          - **properties (DirectDebitCardLinking or DirectDebitOnlineBanking)
          - **metadata (dict)
          - **x_idempotency_key (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          DirectDebitToken

        Raises:
          XenditError

        """
        url = "/linked_account_tokens/auth"
        headers, body = _extract_params(
            locals(),
            func_object=DirectDebit.initialize_tokenization,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return DirectDebitToken(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def validate_token_otp(
        *,
        linked_account_token_id,
        otp_code,
        x_idempotency_key=None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Validates the Linked Account Token OTP
        (API Reference: Direct Debit/Validate OTP for Linked Account Token)

        Args:
          - linked_account_token_id (str)
          - otp_code (str)
          - **x_idempotency_key (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          DirectDebitToken

        Raises:
          XenditError

        """
        url = f"/linked_account_tokens/{linked_account_token_id}/validate_otp"
        headers, body = _extract_params(
            locals(),
            func_object=DirectDebit.validate_token_otp,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=["linked_account_token_id"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return
        else:
            raise XenditError(resp)
