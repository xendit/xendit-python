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
        body, kwargs = _APIRequestor._extract_body(**kwargs)

        return _APIRequestor._request("POST", url, **kwargs)

    @staticmethod
    def patch(url, **kwargs):
        body, kwargs = _APIRequestor._extract_body(**kwargs)

        return _APIRequestor._request("PATCH", url, **kwargs)

    @staticmethod
    def _extract_body(**kwargs):
        body = kwargs.copy()
        body.pop("api_key", None)
        body.pop("base_url", None)
        body.pop("http_client", None)
        kwargs["json"] = body
        return body, kwargs

    @staticmethod
    def _request(method, url, **kwargs):
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
        api_key = kwargs.get("api_key", xendit.api_key)
        url = kwargs.get("base_url", xendit.base_url) + url
        http_client = kwargs.get("http_client", requests)
        x_idempotency_key_header = kwargs.get("x_idempotency_key", None)
        for_user_id_header = kwargs.get("for_user_id", None)

        headers = _APIRequestor._get_headers(
            api_key, x_idempotency_key_header, for_user_id_header
        )
        if method == "GET":
            resp = http_client.request(method, url, headers=headers)
        else:
            resp = http_client.request(
                method, url, headers=headers, json=kwargs.get("json")
            )
        return XenditResponse(resp.status_code, resp.headers, resp.json())

    @staticmethod
    def _get_headers(api_key, x_idempotency_key_header=None, for_user_id_header=None):
        default_headers = {
            "Content-type": "application/json",
            "Authorization": f"Basic {_APIRequestor._generate_auth(api_key)}",
            "xendit-lib": "python",
            "xendit-lib-ver": "0.1.0",
        }
        if x_idempotency_key_header is not None:
            default_headers["X-IDEMPOTENCY-KEY"] = x_idempotency_key_header

        if for_user_id_header is not None:
            default_headers["for-user-id"] = for_user_id_header

        return default_headers

    @staticmethod
    def _generate_auth(api_key):
        auth_pair = api_key + ":"
        auth_base64 = base64.b64encode(auth_pair.encode())
        return auth_base64.decode("utf-8")
