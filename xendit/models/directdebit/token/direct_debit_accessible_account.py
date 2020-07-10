from typing import Union

from .direct_debit_card_link import DirectDebitCardLink
from .direct_debit_online_banking_link import DirectDebitOnlineBankingLink

from xendit.models._base_model import BaseModel


class DirectDebitAccessibleAccount(BaseModel):
    """Accessible Account in Direct Debit (API Reference: Direct Debit)

    Attributes:
      - channel_code (str)
      - id (str)
      - properties (DirectDebitCardLink or DirectDebitOnlineBankingLink)
      - type (str)

    """

    channel_code: str
    id: str
    properties: Union[DirectDebitCardLink, DirectDebitOnlineBankingLink]
    type: str
