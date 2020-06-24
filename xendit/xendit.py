import requests

from ._xendit_param_injector import _XenditParamInjector

from .models import Balance
from .models import Disbursement
from .models import RetailOutlet
from .models import VirtualAccount

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
        self.Disbursement = _XenditParamInjector(
            Disbursement, api_key, base_url, http_client
        )
        self.RetailOutlet = _XenditParamInjector(
            RetailOutlet, api_key, base_url, http_client
        )
        self.VirtualAccount = _XenditParamInjector(
            VirtualAccount, api_key, base_url, http_client
        )
