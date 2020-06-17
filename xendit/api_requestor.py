import base64
import xendit
from xendit.network import RequestMethod
from xendit.network import XenditHTTPClient


class APIRequestor:
    @staticmethod
    def get(url, **kwargs):
        return APIRequestor._request(RequestMethod.GET, url, **kwargs)

    @staticmethod
    def post(url, **kwargs):
        return APIRequestor._request(RequestMethod.POST, url, **kwargs)

    @staticmethod
    def patch(url, **kwargs):
        return APIRequestor._request(RequestMethod.PATCH, url, **kwargs)

    @staticmethod
    def _request(method, url, **kwargs):
        """
        Optional params list:
        api_key -> API Key from xendit instance
        base_url -> Base url of the API
        http_client -> HTTP Client that adhere to HTTPClientInterface
        """
        api_key = kwargs.get("api_key", xendit.api_key)
        url = kwargs.get("base_url", xendit.base_url) + url
        http_client = kwargs.get("http_client", XenditHTTPClient)
        x_idempotency_key_header = kwargs.get("x_idempotency_key", None)
        for_user_id_header = kwargs.get("for_user_id", None)
        headers = APIRequestor._get_headers(
            api_key, x_idempotency_key_header, for_user_id_header
        )
        return http_client.request(method, url, headers=headers)

    @staticmethod
    def _get_headers(api_key, x_idempotency_key_header=None, for_user_id_header=None):
        default_headers = {
            "Content-type": "application/json",
            "Authorization": f"Basic {APIRequestor._generate_auth(api_key)}",
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
