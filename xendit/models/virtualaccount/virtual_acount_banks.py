from xendit._init_from_xendit_response import _init_from_xendit_response


class VirtualAccountBanks:
    """Bank class for Virtual Account (API Reference: Virtual Account)

    Attributes:
      - name (str)
      - code (str)
    """

    @_init_from_xendit_response(required=["name", "code"])
    def __init__(self, xendit_response):
        self.name = xendit_response["name"]
        self.code = xendit_response["code"]
