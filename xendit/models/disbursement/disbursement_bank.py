import json


class DisbursementBank:
    """Bank class for Disbursement (API Reference: Disbursement)

    Attributes:
      - name (str)
      - code (str)
      - can_disburse (bool)
      - can_name_validate (bool)
    """

    def __init__(self, xendit_response):
        self.name = xendit_response["name"]
        self.code = xendit_response["code"]
        self.can_disburse = xendit_response["can_disburse"]
        self.can_name_validate = xendit_response["can_name_validate"]

    def __repr__(self):
        return json.dumps(vars(self), indent=4)
