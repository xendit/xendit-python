from xendit.models._base_model import BaseModel

from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params

from xendit.xendit_error import XenditError


class QRCode(BaseModel):
    """QR Codes class (API Reference: QR Codes)

    Static Methods:
      - QRCode.create (API Reference: /Create QR Code)
      - QRCode.get_by_ext_id (API Reference: /Get QR Code by External ID)

    Attributes:
      - id (str)
      - external_id (str)
      - amount (float)
      - qr_string (str)
      - callback_url (str)
      - type (str)
      - status (str)
      - created (str)
      - updated (str)

    """

    id: str
    external_id: str
    amount: float
    qr_string: str
    callback_url: str
    type: str
    status: str
    created: str
    updated: str

    @staticmethod
    def create(
        *,
        external_id,
        type,
        callback_url,
        amount=None,
        for_user_id=None,
        x_idempotency_key=None,
        x_api_version=None,
        **kwargs,
    ):
        """Send POST Request to create QR Codes (API Reference: QR Code/Create QR Code)

        Args:
          - external_id (str)
          - type (str)
          - callback_url (str)
          - amount (int)
          - **for_user_id (str) (XenPlatforms only)
          - **x_idempotency_key (str)
          - **x_api_version (str): API Version that will be used. If not provided will default to the latest

        Returns:
          QRCode

        Raises:
          XenditError

        """
        type = QRCode._parse_qrcode_type(type)
        url = "/qr_codes"
        headers, body = _extract_params(
            locals(),
            func_object=QRCode.create,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return QRCode(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def get_by_ext_id(
        *,
        external_id,
        for_user_id=None,
        x_idempotency_key=None,
        x_api_version=None,
        **kwargs,
    ):
        """Get QR Codes by external_id (API Reference: QR Code/Get QR Code by External ID)

        Args:
          - external_id (str)
          - **for_user_id (str) (XenPlatforms only)
          - **x_api_version (str): API Version that will be used. If not provided will default to the latest

        Returns:
          QRCode

        Raises:
          XenditError

        """
        url = f"/qr_codes/{external_id}"
        headers, _ = _extract_params(
            locals(),
            func_object=QRCode.get_by_ext_id,
            headers_params=["for_user_id", "x_api_version"],
        )
        kwargs["headers"] = headers

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return QRCode(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def _parse_qrcode_type(qrcode_type):
        try:
            return qrcode_type.name
        except AttributeError:
            return qrcode_type
