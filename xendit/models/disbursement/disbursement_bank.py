from xendit.models._base_model import BaseModel


class DisbursementBank(BaseModel):
    """Bank class for Disbursement (API Reference: Disbursement)

    Attributes:
      - name (str)
      - code (str)
      - can_disburse (bool)
      - can_name_validate (bool)
    """

    name: str
    code: str
    can_disburse: bool
    can_name_validate: bool
