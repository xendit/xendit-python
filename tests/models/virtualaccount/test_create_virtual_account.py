import pytest
from ..base_model_test import BaseModelTest
from .sample_response import virtual_account_response
from xendit import XenditError
from xendit.models import VirtualAccount
from xendit._api_requestor import _APIRequestor


class TestCreateVirtualAccount(BaseModelTest):
    @pytest.mark.parametrize(
        "mock_correct_response", [virtual_account_response()], indirect=True
    )
    def test_return_balance_on_correct_params(self, mocker, mock_correct_response):
        mocker.patch.object(_APIRequestor, "post")
        _APIRequestor.post.return_value = mock_correct_response
        super().base_test_return_class_on_correct_params(
            tested_method_name="create",
            tested_class_name="VirtualAccount",
            params=("demo_1475459775872", "BNI", "Rika Sutanto"),
            expected_result=virtual_account_response(),
        )

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response
    ):
        mocker.patch.object(_APIRequestor, "post")
        _APIRequestor.post.return_value = mock_error_request_response
        super().base_test_raises_error_on_response_error(
            tested_method_name="create",
            tested_class_name="VirtualAccount",
            params=("demo_1475459775872", "BNI", "Rika Sutanto"),
        )

    @pytest.mark.parametrize(
        "mock_correct_response", [virtual_account_response()], indirect=True
    )
    def test_return_balance_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response
    ):
        mocker.patch.object(_APIRequestor, "post")
        _APIRequestor.post.return_value = mock_correct_response
        virtual_account = VirtualAccount.create(
            "demo_1475459775872", "BNI", "Rika Sutanto"
        )
        assert vars(virtual_account) == virtual_account_response()

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response
    ):
        mocker.patch.object(_APIRequestor, "post")
        _APIRequestor.post.return_value = mock_error_request_response
        with pytest.raises(XenditError):
            virtual_account = VirtualAccount.create(
                "demo_1475459775872", "BNI", "Rika Sutanto"
            )
            print(virtual_account)
