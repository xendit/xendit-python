import abc
from . import RequestMethod, XenditResponse


class HTTPClientInterface(metaclass=abc.ABCMeta):
    @staticmethod
    def request(method: RequestMethod, url, **kwargs) -> XenditResponse:
        """
        Optional params list:
        headers -> Dictionary of HTTP Headers to send with the request
        body -> Dictionary of the body that will be send with the request
        """
        raise NotImplementedError
