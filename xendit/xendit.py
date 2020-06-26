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
        injected_params = (api_key, base_url, http_client)
        self.Balance = _XenditParamInjector.instantiate(Balance, injected_params)
        self.Disbursement = _XenditParamInjector.instantiate(
            Disbursement, injected_params
        )
        self.RetailOutlet = _XenditParamInjector.instantiate(
            RetailOutlet, injected_params
        )
        self.VirtualAccount = _XenditParamInjector.instantiate(
            VirtualAccount, injected_params
        )
