import json

from .disbursement_bank import DisbursementBank

from xendit._api_requestor import _APIRequestor
from xendit._init_from_xendit_response import _init_from_xendit_response
from xendit._extract_params import _extract_params

from xendit.xendit_error import XenditError


class Disbursement:
    """Disbursement class (API Reference: Disbursement and Batch Disbursement)

    Related Classes:
      - DisbursementBank

    Static Methods:
      - Disbursement.create (API Reference: Disbursement/Create Disbursement)
      - Disbursement.get (API Reference: Disbursement/Get Disbursement by ID)
      - Disbursement.get_by_ext_id (API Reference: Disbursement/Get Disbursement by External ID)
      - Disbursement.get_available_banks (API Reference: Disbursement/Get Available Banks)

    Attributes:
      - user_id
      - external_id
      - amount
      - bank-code
      - account_holder_name
      - disbursement_description
      - status
      - id

    Optional Attributes:
      - email_to
      - email_cc
      - email_bcc

    """

    @_init_from_xendit_response(
        required=[
            "user_id",
            "external_id",
            "amount",
            "bank_code",
            "account_holder_name",
            "disbursement_description",
            "status",
            "id",
        ],
        optional=["email_to", "email_cc", "email_bcc"],
    )
    def __init__(self, xendit_response):
        pass

    def __repr__(self):
        return json.dumps(vars(self), indent=4)

    @staticmethod
    def create(
        external_id,
        bank_code,
        account_holder_name,
        account_number,
        description,
        amount,
        email_to=[],
        email_cc=[],
        email_bcc=[],
        x_idempotency_key=None,
        for_user_id=None,
        **kwargs,
    ):
        """Send POST Request to create Disbursement (API Reference: Disbursement/Create Disbursement)

        Args:
          - external_id (str)
          - bank_code (str)
          - account_holder_name (str)
          - account_number (str)
          - description (str)
          - amount (int)
          - **email_to (str[])
          - **email_cc (str[])
          - **email_bcc (str[])
          - **x_idempotency_key (str)
          - **for_user_id (str)

        Returns:
          Disbursement

        Raises:
          XenditError

        """
        url = "/disbursements"
        headers, body = _extract_params(
            locals(),
            func_object=Disbursement.create,
            headers_params=["for_user_id", "x_idempotency_key"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body
        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return Disbursement(resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def get(id, **kwargs):
        """Get Disbursement detail by ID (API Reference: Disbursement/Get Disbursement by ID)

        Args:
          - id (str)

        Returns:
          Disbursement

        Raises:
          XenditError

        """
        url = f"/disbursements/{id}"
        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return Disbursement(resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def get_by_ext_id(external_id, **kwargs):
        """Get Disbursement detail by external ID (API Reference: Disbursement/Get Disbursement by External ID)

        Args:
          - external_id (str)

        Returns:
          Disbursement

        Raises:
          XenditError

        """
        url = f"/disbursements?external_id={external_id}"
        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            disbursements = []
            for disbursement in resp.body:
                disbursements.append(Disbursement(disbursement))
            return disbursements
            return Disbursement(resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def get_available_banks(**kwargs):
        """Get Available Banks (API Reference: Disbursement/Get Available Banks)

        Returns:
          List of DisbursementBank

        Raises:
          XenditError

        """
        url = "/available_disbursements_banks"
        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            disbursement_banks = []
            for bank in resp.body:
                disbursement_banks.append(DisbursementBank(bank))
            return disbursement_banks
        else:
            raise XenditError(resp)
