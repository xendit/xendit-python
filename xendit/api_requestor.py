import requests
import xendit
import base64
from xendit.xendit_response import XenditResponse


class APIRequestor:
    @staticmethod
    def get(url):
        url = xendit._base_url + url
        headers = APIRequestor._get_headers()
        resp = requests.get(url, headers=headers)
        return XenditResponse(resp)

    @staticmethod
    def _get_headers():
        return {
            "Content-type": "application/json",
            "Authorization": f"Basic {APIRequestor._generate_auth()}",
            "xendit-lib": "python",
            "xendit-lib-ver": "0.1.0",
        }

    @staticmethod
    def _generate_auth():
        auth_pair = xendit.api_key + ":"
        auth_base64 = base64.b64encode(auth_pair.encode())
        return auth_base64.decode("utf-8")
