import requests

from ._xendit_param_injector import _XenditParamInjector
from .models import Balance
from .network import HTTPClientInterface


class Xendit:
    """Xendit instance. Initialize this with your API Key."""

    def __init__(
        self,
        api_key,
        base_url="https://api.xendit.co/",
        http_client: HTTPClientInterface = requests,
    ):
        self.Balance = _XenditParamInjector(Balance, api_key, base_url, http_client)
