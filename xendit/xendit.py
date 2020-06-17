from .xendit_param_injector import XenditParamInjector
from .models import Balance
from .network import HTTPClientInterface, XenditHTTPClient


class Xendit:
    """Xendit instance. Initialize this with your API Key
    """

    def __init__(
        self,
        api_key,
        base_url="https://api.xendit.co/",
        http_client: HTTPClientInterface = XenditHTTPClient,
    ):
        self.Balance = XenditParamInjector(Balance, api_key, base_url, http_client)
