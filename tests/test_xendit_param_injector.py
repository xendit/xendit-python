from xendit.xendit_param_injector import XenditParamInjector


class SampleMockClass:
    @staticmethod
    def mock_function(*args, **kwargs):
        return kwargs


def test_method_correctly_injected(mocker):
    api_key = "test-123"
    base_url = "https://mock-url.xendit.co"
    http_client = mocker.Mock()

    MockInjectedClass = XenditParamInjector(
        SampleMockClass, api_key=api_key, base_url=base_url, http_client=http_client
    )

    received_args = MockInjectedClass.mock_function()
    assert received_args["api_key"] == api_key
    assert received_args["base_url"] == base_url
    assert received_args["http_client"] == http_client
