from .api_key_injector import APIKeyInjector
from .models import Balance
from .network import HTTPClientInterface, XenditHTTPClient


class Xendit:
    def __init__(
        self,
        api_key,
        base_url="https://api.xendit.co/",
        http_client: HTTPClientInterface = XenditHTTPClient,
    ):
        self.Balance = APIKeyInjector(Balance, api_key, base_url, http_client)
