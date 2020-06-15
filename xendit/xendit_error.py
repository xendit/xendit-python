class XenditError(Exception):
    def __init__(self, xendit_response):
        super(XenditError, self).__init__(xendit_response.body["message"])
        self.status_code = xendit_response.status_code
        self.error_code = xendit_response.body["error_code"]
