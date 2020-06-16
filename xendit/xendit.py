from xendit.api_key_injector import APIKeyInjector
from xendit.models import Balance


class Xendit:
    def __init__(self, api_key, base_url="https://api.xendit.co/"):
        self.api_key = api_key
        self.base_url = base_url
        self.Balance = APIKeyInjector(Balance, api_key, base_url)
