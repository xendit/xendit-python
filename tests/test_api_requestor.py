import responses
from xendit.api_requestor import APIRequestor


@responses.activate
def test_get_call_correct_api():
    base_url = "https://api.xendit.co/"
    section = "balance"
    url = base_url + section

    responses.add(responses.GET, url, json={"balance": 1000})

    APIRequestor.get(section)
