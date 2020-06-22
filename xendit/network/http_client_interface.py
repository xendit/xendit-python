import abc
import requests


class HTTPClientInterface(metaclass=abc.ABCMeta):
    """Interface for HTTP Client. Inject it to your xendit instance to use it."""

    @staticmethod
    def request(method, url, **kwargs) -> requests.Response:
        """
        Args:
          - method (str): HTTP Method that will be sent. For Xendit we will mainly use "GET", "POST", "PATCH"
          - url (str): URL for the request
          - **headers (dict): HTTP Headers to send with the request
          - **json (dict): Body that will be send with the request

        Returns:
          requests.Response
        """
        raise NotImplementedError
