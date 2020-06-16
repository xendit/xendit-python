import base64
import json
import responses
from xendit.api_requestor import APIRequestor


def generate_auth(api_key):
    auth_pair = api_key + ":"
    auth_base64 = base64.b64encode(auth_pair.encode())
    return f'Basic {auth_base64.decode("utf-8")}'


@responses.activate
def test_get_call_correct_api():
    base_url = "https://api.xendit.co/"
    section = "balance"
    url = base_url + section

    responses.add(responses.GET, url, json={"balance": 1000})

    APIRequestor.get(section, base_url=base_url)


@responses.activate
def test_get_use_config_on_empty_params():
    import xendit

    section = "balance"
    xendit.base_url = "https://mock-test.xendit.co"
    xendit.api_key = "123456"
    url = xendit.base_url + section

    def assert_request(request):
        resp_body = {"message": "mock_request"}
        assert request.headers["Authorization"] == generate_auth(xendit.api_key)
        return (200, {}, json.dumps(resp_body))

    responses.add_callback(responses.GET, url, callback=assert_request)

    APIRequestor.get(section)
