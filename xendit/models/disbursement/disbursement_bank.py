import json
from xendit._init_from_xendit_response import _init_from_xendit_response


class DisbursementBank:
    """Bank class for Disbursement (API Reference: Disbursement)

    Attributes:
      - name (str)
      - code (str)
      - can_disburse (bool)
      - can_name_validate (bool)
    """

    @_init_from_xendit_response(
        required=["name", "code", "can_disburse", "can_name_validate"]
    )
    def __init__(self, xendit_response):
        pass

    def __repr__(self):
        return json.dumps(vars(self), indent=4)
