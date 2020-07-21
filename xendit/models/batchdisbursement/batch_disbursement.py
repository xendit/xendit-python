from .batch_disbursement_item import BatchDisbursementItem

from xendit.models._base_model import BaseModel
from xendit.xendit_error import XenditError
from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params


class BatchDisbursement(BaseModel):
    """BatchDisbursement class (API Reference: Batch Disbursement)

    Related Classes:
      - BatchDisbursementItem

    Static Methods:
      - BatchDisbursement.create_batch (API Reference: /Create Batch Disbursement)

    Static Methods for Object Creation:
      - BatchDisbursement.helper_create_batch_item (For BatchDisbursementItem in create_batch)

    Attributes:
      - created (str)
      - reference (str)
      - total_uploaded_count (int)
      - total_uploaded_amount (int)
      - status (str)
      - id (str)
    """

    created: str
    reference: str
    total_uploaded_count: int
    total_uploaded_amount: int
    status: str
    id: str

    def helper_create_batch_item(
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
          - created (str)
          - reference (str)
          - total_uploaded_count (int)
          - total_uploaded_amount (int)
          - status (str)
          - id (str)

        Return:
          - BatchDisbursementItem
        """
        params = locals()
        del params["kwargs"]

        return BatchDisbursementItem.Query(**params)

    @staticmethod
    def create_batch(
        reference,
        disbursements,
        x_idempotency_key=None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Create a batch disbursements (API Reference: Batch Disbursement/Create Batch Disbursement)

        Args:
          - reference (str)
          - disbursements (BatchDisbursementItem)
          - **x_idempotency_key (str)
          - **for_user_id (str) (XenPlatform only)
          - **x_api_version (str)

        Returns
          BatchDisbursement

        Raises
          XenditError

        """
        url = "/batch_disbursements"
        headers, body = _extract_params(
            locals(),
            func_object=BatchDisbursement.create_batch,
            headers_params=["for_user_id", "for_user_id", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return BatchDisbursement(resp.body)
        else:
            raise XenditError(resp)
