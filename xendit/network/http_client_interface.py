import abc
from . import RequestMethod, XenditResponse


class HTTPClientInterface(metaclass=abc.ABCMeta):
    """Interface for HTTP Client. Inject it to your xendit instance to use it."""

    @staticmethod
    def request(method: RequestMethod, url, **kwargs) -> XenditResponse:
        """
        Args:
          - method (RequestMethod): HTTP Method that will be sent
          - url (str): URL for the request
          - **headers (dict): HTTP Headers to send with the request
          - **body (dict): Body that will be send with the request

        Returns: XenditResponse
        """
        raise NotImplementedError
