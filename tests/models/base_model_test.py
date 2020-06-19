import pytest
from xendit import Xendit, XenditError


class BaseModelTest:
    def base_test_return_class_on_correct_params(
        self, tested_method_name, tested_class_name, params, expected_result
    ):
        xendit = Xendit(api_key="mock_key")
        tested_object = getattr(xendit, tested_class_name)
        tested_method = getattr(tested_object, tested_method_name)
        result_object = vars(tested_method(*params))
        assert result_object == expected_result

    def base_test_raises_error_on_response_error(
        self, tested_method_name, tested_class_name, params
    ):
        xendit = Xendit(api_key="mock_key")
        tested_object = getattr(xendit, tested_class_name)
        tested_method = getattr(tested_object, tested_method_name)
        with pytest.raises(XenditError):
            print(tested_method(*params))
