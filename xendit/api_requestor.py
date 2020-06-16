import requests
import base64
import xendit
from xendit.xendit_response import XenditResponse


class APIRequestor:
    @staticmethod
    def get(url, *args, **kwargs):
        api_key = kwargs.get("api_key", xendit.api_key)
        url = kwargs.get("base_url", xendit.base_url) + url
        headers = APIRequestor._get_headers(api_key)
        resp = requests.get(url, headers=headers)
        return XenditResponse(resp)

    @staticmethod
    def _get_headers(api_key):
        return {
            "Content-type": "application/json",
            "Authorization": f"Basic {APIRequestor._generate_auth(api_key)}",
            "xendit-lib": "python",
            "xendit-lib-ver": "0.1.0",
        }

    @staticmethod
    def _generate_auth(api_key):
        auth_pair = api_key + ":"
        auth_base64 = base64.b64encode(auth_pair.encode())
        return auth_base64.decode("utf-8")
