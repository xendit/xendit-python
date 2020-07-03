from typing import List

from .disbursement_bank import DisbursementBank

from xendit.models._base_model import BaseModel

from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params

from xendit.xendit_error import XenditError


class Disbursement(BaseModel):
    """Disbursement class (API Reference: Disbursement)

    Related Classes:
      - DisbursementBank

    Static Methods:
      - Disbursement.create (API Reference: /Create Disbursement)
      - Disbursement.get (API Reference: /Get Disbursement by ID)
      - Disbursement.get_by_ext_id (API Reference: /Get Disbursement by External ID)
      - Disbursement.get_available_banks (API Reference: /Get Available Banks)

    Attributes:
      - user_id (str)
      - external_id (str)
      - amount (int)
      - bank_code (str)
      - account_holder_name (str)
      - disbursement_description (str)
      - status (str)
      - id (str)

    Optional Attributes:
      - email_to (str[])
      - email_cc (str[])
      - email_bcc (str[])

    """

    user_id: str
    external_id: str
    amount: int
    bank_code: str
    account_holder_name: str
    disbursement_description: str
    status: str
    id: str

    # Optional
    email_to: List[str]
    email_cc: List[str]
    email_bcc: List[str]

    @staticmethod
    def create(
        *,
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
        x_api_version=None,
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
          - **for_user_id (str)
          - **x_idempotency_key (str)
          - **x_api_version (str): API Version that will be used. If not provided will default to the latest

        Returns:
          Disbursement

        Raises:
          XenditError

        """
        url = "/disbursements"
        headers, body = _extract_params(
            locals(),
            func_object=Disbursement.create,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return Disbursement(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def get(*, id, for_user_id=None, x_api_version=None, **kwargs):
        """Get Disbursement detail by ID (API Reference: Disbursement/Get Disbursement by ID)

        Args:
          - id (str)
          - **for_user_id (str)
          - **x_api_version (str): API Version that will be used. If not provided will default to the latest

        Returns:
          Disbursement

        Raises:
          XenditError

        """
        url = f"/disbursements/{id}"
        headers, _ = _extract_params(
            locals(),
            func_object=Disbursement.get,
            headers_params=["for_user_id", "x_api_version"],
            ignore_params=["id"],
        )
        kwargs["headers"] = headers

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return Disbursement(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def get_by_ext_id(*, external_id, for_user_id=None, x_api_version=None, **kwargs):
        """Get Disbursement detail by external ID (API Reference: Disbursement/Get Disbursement by External ID)

        Args:
          - external_id (str)
          - **for_user_id (str)
          - **x_api_version (str): API Version that will be used. If not provided will default to the latest

        Returns:
          Disbursement

        Raises:
          XenditError

        """
        url = f"/disbursements?external_id={external_id}"
        headers, _ = _extract_params(
            locals(),
            func_object=Disbursement.get_by_ext_id,
            headers_params=["for_user_id", "x_api_version"],
            ignore_params=["external_id"],
        )
        kwargs["headers"] = headers

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            disbursements = []
            for disbursement in resp.body:
                disbursements.append(Disbursement(**disbursement))
            return disbursements
        else:
            raise XenditError(resp)

    @staticmethod
    def get_available_banks(*, for_user_id=None, x_api_version=None, **kwargs):
        """Get Available Banks (API Reference: Disbursement/Get Available Banks)

        Args:
          - **for_user_id (str)
          - **x_api_version (str): API Version that will be used. If not provided will default to the latest

        Returns:
          List of DisbursementBank

        Raises:
          XenditError

        """
        url = "/available_disbursements_banks"
        headers, _ = _extract_params(
            locals(),
            func_object=Disbursement.get_available_banks,
            headers_params=["for_user_id", "x_api_version"],
        )
        kwargs["headers"] = headers

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            disbursement_banks = []
            for bank in resp.body:
                disbursement_banks.append(DisbursementBank(**bank))
            return disbursement_banks
        else:
            raise XenditError(resp)
