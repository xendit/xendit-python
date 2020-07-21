from typing import List
from xendit.models._base_model import BaseModel
from xendit.models._base_query import BaseQuery


class BatchDisbursementItem(BaseModel):
    """Item to be sent for Batch Disbursement (API Reference: BatchDisbursement)"""

    class Query(BaseQuery):
        """Item to be sent for Batch Disbursement (API Reference: Batch Disbursement)

        Use this to initialize create_batch

        Attributes:
        - amount (int)
        - bank_code (str)
        - bank_account_name (str)
        - bank_account_number (str)
        - description (str)
        - external_id (str)

        Optional Attributes:
        - email_to (str[])
        - email_cc (str[])
        - email_bcc (str[])

        """

        amount: int
        bank_code: str
        bank_account_name: str
        bank_account_number: str
        description: str
        external_id: str

        # Optional
        email_to: List[str]
        email_cc: List[str]
        email_bcc: List[str]
