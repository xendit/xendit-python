import requests
from . import HTTPClientInterface, RequestMethod, XenditResponse


class XenditHTTPClient(HTTPClientInterface):
    @staticmethod
    def request(method, url, **kwargs):
        method_name = XenditHTTPClient._parse_request_method(method)
        kwargs["json"] = kwargs.pop("body", None)

        resp = requests.request(method_name, url, **kwargs)

        return XenditResponse(resp.status_code, resp.headers, resp.json())

    @staticmethod
    def _parse_request_method(method):
        if isinstance(method, RequestMethod):
            return method.name
        else:
            return method
