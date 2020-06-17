import responses
from xendit.network import RequestMethod
from xendit.network import XenditHTTPClient


@responses.activate
def test_request_correct_params():
    url = "https://mock-url.xendit.co"
    responses.add("GET", url, body="{}")

    XenditHTTPClient.request(RequestMethod.GET, url)
