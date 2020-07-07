import pytest
from xendit import Xendit, XenditError
from xendit._api_requestor import _APIRequestor


# fmt: off
class ModelBaseTest:
    def base_test_return_class_on_correct_params(
        self, tested_class_name, tested_method_name, params, expected_result
    ):
        xendit = Xendit(api_key="mock_key")
        args, kwargs = params
        tested_object = getattr(xendit, tested_class_name)
        tested_method = getattr(tested_object, tested_method_name)
        returned_object = tested_method(*args, **kwargs)
        try:
            assert vars(returned_object) == expected_result
        except TypeError:
            for idx, singular_data in enumerate(returned_object):
                assert vars(singular_data) == expected_result[idx]

    def base_test_raises_error_on_response_error(
        self, tested_class_name, tested_method_name, params
    ):
        xendit = Xendit(api_key="mock_key")
        args, kwargs = params
        tested_object = getattr(xendit, tested_class_name)
        tested_method = getattr(tested_object, tested_method_name)
        with pytest.raises(XenditError):
            print(tested_method(*args, **kwargs))

    def run_success_return_test_on_xendit_instance(self, mocker, mock_correct_response, default_tested_class_data):
        """Using xendit instance for API key and receive result from API, it should return correct result

        Args:
            mocker (fixture): Default mocker fixture
            mock_correct_response (function): Mock correct response that sent by APIRequestor
            default_tested_class_data (tuple): Tuple with 7 item that contain:
            - tested_class (class): Class that will be tested
            - class_name (str): String representation for the class
            - method_name (str): Method name that will be tested
            - http_method_name (str): HTTP Method name that will be used in the API Requestor
            - url (str): URL for the request
            - params (tuple): Params with format (args, kwargs)
            - expected_correct_result (dict): Expected Correct Result
        """
        tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result = default_tested_class_data
        mocker.patch.object(_APIRequestor, http_method_name)
        api_requestor_used_method = getattr(_APIRequestor, http_method_name)
        setattr(api_requestor_used_method, "return_value", mock_correct_response)
        self.base_test_return_class_on_correct_params(
            tested_method_name=method_name,
            tested_class_name=class_name,
            params=params,
            expected_result=expected_correct_result,
        )

    def run_raises_error_test_on_xendit_instance(self, mocker, mock_error_request_response, default_tested_class_data):
        """Using xendit instance for API key and receive error from API, it should return XenditError

        Args:
            mocker (fixture): Default mocker fixture
            mock_correct_response (function): Mock correct response that sent by APIRequestor
            default_tested_class_data (tuple): Tuple with 7 item that contain:
            - tested_class (class): Class that will be tested
            - class_name (str): String representation for the class
            - method_name (str): Method name that will be tested
            - http_method_name (str): HTTP Method name that will be used in the API Requestor
            - url (str): URL for the request
            - params (tuple): Params with format (args, kwargs)
            - expected_correct_result (dict): Expected Correct Result
        """
        tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result = default_tested_class_data
        mocker.patch.object(_APIRequestor, http_method_name)
        api_requestor_used_method = getattr(_APIRequestor, http_method_name)
        setattr(api_requestor_used_method, "return_value", mock_error_request_response)
        self.base_test_raises_error_on_response_error(
            tested_class_name=class_name,
            tested_method_name=method_name,
            params=params,
        )

    def run_success_return_test_on_global_config(self, mocker, mock_correct_response, default_tested_class_data):
        """Using global config for API key and receive result from API, it should return the correct result

        Args:
            mocker (fixture): Default mocker fixture
            mock_correct_response (function): Mock correct response that sent by APIRequestor
            default_tested_class_data (tuple): Tuple with 7 item that contain:
            - tested_class (class): Class that will be tested
            - class_name (str): String representation for the class
            - method_name (str): Method name that will be tested
            - http_method_name (str): HTTP Method name that will be used in the API Requestor
            - url (str): URL for the request
            - params (tuple): Params with format (args, kwargs)
            - expected_correct_result (dict): Expected Correct Result
        """
        tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result = default_tested_class_data
        args, kwargs = params
        mocker.patch.object(_APIRequestor, http_method_name)
        api_requestor_used_method = getattr(_APIRequestor, http_method_name)
        setattr(api_requestor_used_method, "return_value", mock_correct_response)
        returned_object = getattr(tested_class, method_name)(*args, **kwargs)
        try:
            assert vars(returned_object) == expected_correct_result
        except TypeError:
            for idx, singular_data in enumerate(returned_object):
                assert vars(singular_data) == expected_correct_result[idx]

    def run_raises_error_test_on_global_config(self, mocker, mock_error_request_response, default_tested_class_data):
        """Using global config for API key and receive error from API, it should return XenditError

        Args:
            mocker (fixture): Default mocker fixture
            mock_correct_response (function): Mock correct response that sent by APIRequestor
            default_tested_class_data (tuple): Tuple with 7 item that contain:
            - tested_class (class): Class that will be tested
            - class_name (str): String representation for the class
            - method_name (str): Method name that will be tested
            - http_method_name (str): HTTP Method name that will be used in the API Requestor
            - url (str): URL for the request
            - params (tuple): Params with format (args, kwargs)
            - expected_correct_result (dict): Expected Correct Result
        """
        tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result = default_tested_class_data
        args, kwargs = params
        mocker.patch.object(_APIRequestor, http_method_name)
        api_requestor_used_method = getattr(_APIRequestor, http_method_name)
        setattr(api_requestor_used_method, "return_value", mock_error_request_response)
        with pytest.raises(XenditError):
            returned_object = getattr(tested_class, method_name)(*args, **kwargs)
            print(returned_object)

    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        """It should send correct request to API Requestor

        Args:
            mocker (fixture): Default mocker fixture
            mock_correct_response (function): Mock correct response that sent by APIRequestor
            api_requestor_request_data (tuple): Tuple with 8 items that contain:
            - tested_class (class): Class that will be tested
            - class_name (str): String representation for the class
            - method_name (str): Method name that will be tested
            - http_method_name (str): HTTP Method name that will be used in the API Requestor
            - url (str): URL for the request
            - params (tuple): Params with format (args, kwargs)
            - headers (dict): headers that will be sent
            - body (dict): body that will be sent (if http_method_name == 'get' then it's parameters of the request)
        """
        tested_class, class_name, method_name, http_method_name, url, params, headers, body = api_requestor_request_data
        args, kwargs = params

        mocker.patch.object(_APIRequestor, http_method_name)
        tested_apirequestor_method = getattr(_APIRequestor, http_method_name)
        setattr(tested_apirequestor_method, "return_value", mock_correct_response)

        tested_method = getattr(tested_class, method_name)
        tested_method(*args, **kwargs)
        self.assert_apirequestor_method(tested_apirequestor_method, http_method_name, url, headers, body)

    def assert_apirequestor_method(self, tested_apirequestor_method, http_method_name, url, headers, body):
        """Assert that tested_apirequestor_method is called with the specified parameters.
        If the body is empty, we should give the freedom to not attach the body in the parameters

        Args:
            tested_apirequestor_method (Mock function): Function that will be tested
            http_method_name (str): HTTP Method
            url (str): URL for the request
            headers (dict): Headers for the request
            body (dict): Body/params of the request
        """
        if(http_method_name == "get"):
            if(body != {} and '?' not in url):
                tested_apirequestor_method.assert_called_with(url, headers=headers, params=body)
            else:
                try:
                    tested_apirequestor_method.assert_called_with(url, headers=headers)
                except AssertionError:
                    tested_apirequestor_method.assert_called_with(url, headers=headers, params=body)
        else:
            if(body != {}):
                tested_apirequestor_method.assert_called_with(url, headers=headers, body=body)
            else:
                try:
                    tested_apirequestor_method.assert_called_with(url, headers=headers)
                except AssertionError:
                    tested_apirequestor_method.assert_called_with(url, headers=headers, body=body)
# fmt: on
