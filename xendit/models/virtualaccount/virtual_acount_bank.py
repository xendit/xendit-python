import json
from xendit._init_from_xendit_response import _init_from_xendit_response


class VirtualAccountBank:
    """Bank class for Virtual Account (API Reference: Virtual Account)

    Attributes:
      - name (str)
      - code (str)
    """

    @_init_from_xendit_response(required=["name", "code"])
    def __init__(self, xendit_response):
        pass

    def __repr__(self):
        return json.dumps(vars(self), indent=4)
