import json


class VirtualAccountBank:
    """Bank class for Virtual Account (API Reference: Virtual Account)

    Attributes:
      - name (str)
      - code (str)
    """

    def __init__(self, xendit_response):
        self.name = xendit_response["name"]
        self.code = xendit_response["code"]

    def __repr__(self):
        return json.dumps(vars(self), indent=4)
