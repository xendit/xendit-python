import pytest
import time

from xendit import QRCodeType

from .base_integration_test import BaseIntegrationTest
from tests.sampleresponse.qrcode import qrcode_response


class TestQRCode(BaseIntegrationTest):
    @pytest.fixture
    def QRCode(self, xendit_instance):
        return xendit_instance.QRCode

    @pytest.fixture
    def qrcode_data(self, QRCode):
        qrcode = QRCode.create(
            external_id=f"qrcode-id-{int(time.time())}",
            type=QRCodeType.DYNAMIC,
            callback_url="https://webhook.site",
            amount="4000",
        )
        return qrcode

    def test_create_qrcode(self, qrcode_data):
        qrcode = qrcode_data

        self.assert_returned_object_has_same_key_as_sample_response(
            qrcode, qrcode_response()
        )

    def test_get_qrcode_by_ext_id(self, QRCode, qrcode_data):
        qrcode = qrcode_data

        qrcode = QRCode.get_by_ext_id(external_id=qrcode.external_id)

        self.assert_returned_object_has_same_key_as_sample_response(
            qrcode, qrcode_response()
        )
