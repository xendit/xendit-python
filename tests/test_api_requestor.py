import base64
import pytest
import xendit

from xendit.api_requestor import APIRequestor
from xendit.network import RequestMethod
from xendit.network import XenditHTTPClient


def generate_auth(api_key):
    auth_pair = api_key + ":"
    auth_base64 = base64.b64encode(auth_pair.encode())
    return f'Basic {auth_base64.decode("utf-8")}'


def substitute_http_client_request(method, url, **kwargs):
    return method, url, kwargs


@pytest.fixture
def mocked_http_client(mocker):
    mocker.patch.object(XenditHTTPClient, "request")
    XenditHTTPClient.request = substitute_http_client_request
    return XenditHTTPClient


@pytest.fixture
def default_params(mocked_http_client):
    api_key = "test-123"
    base_url = "https://mock-url.xendit.co"
    section = "/balance"
    http_client = mocked_http_client
    url = base_url + section
    return api_key, base_url, section, http_client, url


def test_get_call_get_method(default_params):
    api_key, base_url, section, http_client, url = default_params

    method_received, url_received, kwargs_received = APIRequestor.get(
        section, api_key=api_key, base_url=base_url, http_client=http_client,
    )
    assert method_received == RequestMethod.GET


def test_post_call_post_method(default_params):
    api_key, base_url, section, http_client, url = default_params

    method_received, url_received, kwargs_received = APIRequestor.post(
        section, api_key=api_key, base_url=base_url, http_client=http_client,
    )
    assert method_received == RequestMethod.POST


def test_patch_call_patch_method(default_params):
    api_key, base_url, section, http_client, url = default_params

    method_received, url_received, kwargs_received = APIRequestor.patch(
        section, api_key=api_key, base_url=base_url, http_client=http_client,
    )
    assert method_received == RequestMethod.PATCH


def test_request_send_correct_params_on_given_params(default_params):
    api_key, base_url, section, http_client, url = default_params

    method_received, url_received, kwargs_received = APIRequestor._request(
        RequestMethod.GET,
        section,
        api_key=api_key,
        base_url=base_url,
        http_client=http_client,
    )
    assert url_received == url
    assert kwargs_received["headers"]["Authorization"] == generate_auth(api_key)


def test_request_send_default_config_on_empty_params(default_params):
    api_key, base_url, section, http_client, url = default_params
    xendit.api_key = api_key
    xendit.base_url = base_url

    method_received, url_received, kwargs_received = APIRequestor._request(
        RequestMethod.GET, section, http_client=http_client,
    )
    assert url_received == url
    assert kwargs_received["headers"]["Authorization"] == generate_auth(api_key)


def test_request_header_have_custom_header_when_inserted(default_params):
    api_key, base_url, section, http_client, url = default_params

    method_received, url_received, kwargs_received = APIRequestor._request(
        RequestMethod.POST,
        section,
        api_key=api_key,
        base_url=base_url,
        http_client=http_client,
        x_idempotency_key="key-123",
        for_user_id="id-123",
    )

    assert kwargs_received["headers"]["X-IDEMPOTENCY-KEY"] == "key-123"
    assert kwargs_received["headers"]["for-user-id"] == "id-123"
