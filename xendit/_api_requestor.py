import base64
import requests
import xendit
import sys
from xendit.network import XenditResponse

if sys.version_info[1] < 8:
    from importlib_metadata import version
else:
    from importlib.metadata import version


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
        method,
        url,
        api_key=None,
        base_url=None,
        http_client=requests,
        headers={},
        body={},
        params={},
    ):
        """Send HTTP Method to given url

        Args:
            - method (str): HTTP Method that will be send
            - url (str): URL Directory that will be searched (not including base_url)
            - **api_key (string): API Key from xendit instance. Default to config if not provided
            - **base_url (string): Base url of the API. Default to config if not provided
            - **http_client (HTTPClientInterface): HTTP Client that adhere to HTTPClientInterface. Default to config if not provided
            - **headers: Headers of the request
            - **body: Body of the request. Only used on POST and PATCH request
            - **params: Parameters of the request. Only used on GET request
        """
        if api_key is None:
            api_key = xendit.api_key
        if base_url is None:
            base_url = xendit.base_url
        url = base_url + url

        headers = _APIRequestor._add_default_headers(api_key, headers)
        if method == "GET":
            resp = http_client.request(method, url, headers=headers, params=params)
        else:
            resp = http_client.request(method, url, headers=headers, json=body)
        return XenditResponse(resp.status_code, resp.headers, resp.json())

    @staticmethod
    def _add_default_headers(api_key, headers):
        headers["Content-type"] = "application/json"
        headers["Authorization"] = f"Basic {_APIRequestor._generate_auth(api_key)}"
        headers["xendit-lib"] = "python"
        headers["xendit-lib-ver"] = version("xendit-python")
        return headers

    @staticmethod
    def _generate_auth(api_key):
        auth_pair = api_key + ":"
        auth_base64 = base64.b64encode(auth_pair.encode())
        return auth_base64.decode("utf-8")
