import base64
import json
import pytest
import requests
import responses
import xendit

from xendit._api_requestor import _APIRequestor


def generate_auth(api_key):
    auth_pair = api_key + ":"
    auth_base64 = base64.b64encode(auth_pair.encode())
    return f'Basic {auth_base64.decode("utf-8")}'


def substitute_callback(request):
    resp_body = {"method": request.method}
    return (200, request.headers, json.dumps(resp_body))


@pytest.fixture
def default_params():
    api_key = "test-123"
    base_url = "https://mock-url.xendit.co"
    section = "/balance"
    http_client = requests
    url = base_url + section
    custom_headers = {
        "X-IDEMPOTENCY-KEY": "key-123",
        "for-user-id": "id-123",
    }
    return api_key, base_url, section, http_client, url, custom_headers


@responses.activate
def test_get_call_get_method(default_params):
    api_key, base_url, section, http_client, url, custom_headers = default_params
    responses.add_callback(method="GET", url=url, callback=substitute_callback)

    _APIRequestor.get(
        section, api_key=api_key, base_url=base_url, http_client=http_client,
    )


@responses.activate
def test_post_call_post_method(default_params):
    api_key, base_url, section, http_client, url, custom_headers = default_params
    responses.add_callback(method="POST", url=url, callback=substitute_callback)

    _APIRequestor.post(
        section, api_key=api_key, base_url=base_url, http_client=http_client,
    )


@responses.activate
def test_patch_call_patch_method(default_params):
    api_key, base_url, section, http_client, url, custom_headers = default_params
    responses.add_callback(method="PATCH", url=url, callback=substitute_callback)

    _APIRequestor.patch(
        section, api_key=api_key, base_url=base_url, http_client=http_client,
    )


@responses.activate
def test_request_send_correct_params_on_given_params(default_params):
    api_key, base_url, section, http_client, url, custom_headers = default_params
    responses.add_callback(method="GET", url=url, callback=substitute_callback)

    xendit_response = _APIRequestor._request(
        "GET", section, api_key=api_key, base_url=base_url, http_client=http_client,
    )

    assert xendit_response.headers["Authorization"] == generate_auth(api_key)


@responses.activate
def test_request_send_default_config_on_empty_params(default_params):
    api_key, base_url, section, http_client, url, custom_headers = default_params
    xendit.api_key = api_key
    xendit.base_url = base_url
    responses.add_callback(method="GET", url=url, callback=substitute_callback)

    xendit_response = _APIRequestor._request("GET", section, http_client=http_client,)

    assert xendit_response.headers["Authorization"] == generate_auth(api_key)


@responses.activate
def test_request_header_have_custom_header_when_inserted(default_params):
    api_key, base_url, section, http_client, url, custom_headers = default_params

    responses.add_callback(method="POST", url=url, callback=substitute_callback)
    xendit_response = _APIRequestor._request(
        "POST",
        section,
        api_key=api_key,
        base_url=base_url,
        http_client=http_client,
        x_idempotency_key=custom_headers["X-IDEMPOTENCY-KEY"],
        for_user_id=custom_headers["for-user-id"],
    )

    assert xendit_response.headers["X-IDEMPOTENCY-KEY"] == "key-123"
    assert xendit_response.headers["for-user-id"] == "id-123"
