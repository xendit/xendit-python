from typing import Union

from xendit.models._base_model import BaseModel

from xendit.models.directdebit.token.direct_debit_card_link import DirectDebitCardLink
from xendit.models.directdebit.token.direct_debit_online_banking_link import (
    DirectDebitOnlineBankingLink,
)


class DirectDebitPaymentMethod(BaseModel):
    """Payment Method class in Direct Debit (API Reference: Direct Debit)

    Attributes:
      - id (str)
      - type (str)
      - properties (DirectDebitCardLink or DirectDebitOnlineBankingLink)
      - customer_id (str)
      - status (str)
      - created (str)
      - updated (str)
      - metadata (dict)

    """

    id: str
    type: str
    properties: Union[DirectDebitCardLink, DirectDebitOnlineBankingLink]
    customer_id: str
    status: str
    created: str
    updated: str
    metadata: dict
