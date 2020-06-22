import pytest
from xendit import Xendit, XenditError
from xendit._api_requestor import _APIRequestor


# fmt: off
class BaseModelTest:
    def base_test_return_class_on_correct_params(
        self, tested_class_name, tested_method_name, params, expected_result
    ):
        xendit = Xendit(api_key="mock_key")
        tested_object = getattr(xendit, tested_class_name)
        tested_method = getattr(tested_object, tested_method_name)
        returned_object = tested_method(*params)
        try:
            assert vars(returned_object) == expected_result
        except TypeError:
            for idx, singular_data in enumerate(returned_object):
                assert vars(singular_data) == expected_result[idx]

    def base_test_raises_error_on_response_error(
        self, tested_class_name, tested_method_name, params
    ):
        xendit = Xendit(api_key="mock_key")
        tested_object = getattr(xendit, tested_class_name)
        tested_method = getattr(tested_object, tested_method_name)
        with pytest.raises(XenditError):
            print(tested_method(*params))

    def run_success_return_test_on_xendit_instance(self, mocker, mock_correct_response, default_tested_class_data):
        tested_class, class_name, method_name, http_method_name, params, expected_correct_result = default_tested_class_data
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
        tested_class, class_name, method_name, http_method_name, params, expected_correct_result = default_tested_class_data
        mocker.patch.object(_APIRequestor, http_method_name)
        api_requestor_used_method = getattr(_APIRequestor, http_method_name)
        setattr(api_requestor_used_method, "return_value", mock_error_request_response)
        self.base_test_raises_error_on_response_error(
            tested_class_name=class_name,
            tested_method_name=method_name,
            params=params,
        )

    def run_success_return_test_on_global_config(self, mocker, mock_correct_response, default_tested_class_data):
        tested_class, class_name, method_name, http_method_name, params, expected_correct_result = default_tested_class_data
        mocker.patch.object(_APIRequestor, http_method_name)
        api_requestor_used_method = getattr(_APIRequestor, http_method_name)
        setattr(api_requestor_used_method, "return_value", mock_correct_response)
        returned_object = getattr(tested_class, method_name)(*params)
        try:
            assert vars(returned_object) == expected_correct_result
        except TypeError:
            for idx, singular_data in enumerate(returned_object):
                assert vars(singular_data) == expected_correct_result[idx]

    def run_raises_error_test_on_global_config(self, mocker, mock_error_request_response, default_tested_class_data):
        tested_class, class_name, method_name, http_method_name, params, expected_correct_result = default_tested_class_data
        mocker.patch.object(_APIRequestor, http_method_name)
        api_requestor_used_method = getattr(_APIRequestor, http_method_name)
        setattr(api_requestor_used_method, "return_value", mock_error_request_response)
        with pytest.raises(XenditError):
            returned_object = getattr(tested_class, method_name)(*params)
            print(returned_object)
# fmt: on
