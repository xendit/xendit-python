import json

from .batch_disbursement_item import BatchDisbursementItem

from xendit._init_from_xendit_response import _init_from_xendit_response
from xendit.xendit_error import XenditError
from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params


class BatchDisbursement:
    """BatchDisbursement class (API Reference: Batch Disbursement)

    Related Classes:
      - BatchDisbursementItem

    Static Methods:
      - BatchDisbursement.create_batch (API Reference: /Create Batch Disbursement)

    Attributes:
      - created (str)
      - reference (str)
      - total_uploaded_count (int)
      - total_uploaded_amount (int)
      - status (str)
      - id (str)
    """

    @_init_from_xendit_response(
        required=[
            "created",
            "reference",
            "total_uploaded_count",
            "total_uploaded_amount",
            "status",
            "id",
        ]
    )
    def __init__(self, xendit_response):
        pass

    def __repr__(self):
        return json.dumps(vars(self), indent=4)

    @staticmethod
    def create_batch(
        reference, disbursements, x_idempotency_key=None, for_user_id=None, **kwargs
    ):
        """Create a batch disbursements (API Reference: Batch Disbursement/Create Batch Disbursement)

        Args:
          - reference (str)
          - disbursements (BatchDisbursementItem)
          - **x_idempotency_key (str)
          - **for_user_id (str) (XenPlatform only)

        Returns
          Balance

        Raises
          XenditError

        """
        headers, _ = _extract_params(
            locals(),
            func_object=BatchDisbursement.create_batch,
            headers_params=["for_user_id"],
        )
        kwargs["headers"] = headers
        url = "/batch_disbursements"

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return BatchDisbursementItem(resp.body)
        else:
            raise XenditError(resp)
