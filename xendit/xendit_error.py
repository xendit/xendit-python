class XenditError(Exception):
    """Error that will be given when status code != 200."""

    def __init__(self, xendit_response):
        try:
            super(XenditError, self).__init__(xendit_response.body["message"])
        except KeyError:
            super(XenditError, self).__init__(
                xendit_response.body["errors"][0]["message"]
            )
        self.status_code = xendit_response.status_code
        self.error_code = xendit_response.body["error_code"]
        self.errors = xendit_response.body.get("errors", None)
