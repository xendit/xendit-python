import base64
import requests
import xendit
from xendit.network import XenditResponse


class _APIRequestor:
    @staticmethod
    def get(url, **kwargs):
        return _APIRequestor._request("GET", url, **kwargs)

    @staticmethod
    def post(url, **kwargs):
        return _APIRequestor._request("POST", url, **kwargs)

    @staticmethod
    def patch(url, **kwargs):
        return _APIRequestor._request("PATCH", url, **kwargs)

    @staticmethod
    def _request(
        method, url, api_key=None, base_url=None, http_client=requests, headers={}
    ):
        """Send HTTP Method to given url

        Args:
          - method (str): HTTP Method that will be send
          - url (str): URL Directory that will be searched (not including base_url)
          - **api_key (string): API Key from xendit instance. Default to config if not provided
          - **base_url (string): Base url of the API. Default to config if not provided
          - **http_client (HTTPClientInterface): HTTP Client that adhere to HTTPClientInterface. Default to config if not provided
          - **x_idempotency_key (string): X-IDEMPOTENCY-KEY header that will be used
          - **for_user_id (string): for-user-id header that will be used
        """
        if api_key is None:
            api_key = xendit.api_key
        if base_url is None:
            base_url = xendit.base_url
        url = base_url + url

        headers = _APIRequestor._add_default_headers(api_key, headers)
        resp = http_client.request(method, url, headers=headers)
        return XenditResponse(resp.status_code, resp.headers, resp.json())

    @staticmethod
    def _add_default_headers(api_key, headers):
        headers["Content-type"] = "application/json"
        headers["Authorization"] = f"Basic {_APIRequestor._generate_auth(api_key)}"
        headers["xendit-lib"] = "python"
        headers["xendit-lib-ver"] = "0.1.0"

        return headers

    @staticmethod
    def _generate_auth(api_key):
        auth_pair = api_key + ":"
        auth_base64 = base64.b64encode(auth_pair.encode())
        return auth_base64.decode("utf-8")
