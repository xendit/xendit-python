class XenditResponse:
    def __init__(self, response):
        self.status_code = response.status_code
        self.headers = response.headers
        self.body = response.json()
