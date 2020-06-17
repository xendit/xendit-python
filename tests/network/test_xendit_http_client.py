import responses
from xendit.network import RequestMethod
from xendit.network import _XenditHTTPClient


@responses.activate
def test_request_correct_params():
    url = "https://mock-url.xendit.co"
    responses.add("GET", url, body="{}")

    _XenditHTTPClient.request(RequestMethod.GET, url)
