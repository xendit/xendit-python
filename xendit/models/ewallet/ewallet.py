from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params

from xendit.xendit_error import XenditError

from .ewallet_type import EWalletType
from .ovo import OVOPayment, OVOPaymentStatus
from .dana import DANAPayment, DANAPaymentStatus
from .linkaja import LinkAjaPayment, LinkAjaPaymentStatus, LinkAjaItem
from .ewallet_charge import EWalletCharge
from .ewallet_basket import EWalletBasket


class EWallet:
    """EWallet class (API Reference: eWallets)

    Related Classes:
      - OVOPayment
      - OVOPaymentStatus
      - DANAPayment
      - DANAPaymentStatus
      - LinkAjaPayment
      - LinkAjaPaymentStatus
      - EWalletCharge

    Static Methods:
      - EWallet.create_ovo_payment (API Reference: /Create Payment)
      - EWallet.create_dana_payment (API Reference: /Create Payment)
      - EWallet.create_linkaja_payment (API Reference: /Create Payment)
      - EWallet.get_payment_status (API Reference: /Get Payment Status)
      - EWallet.create_ewallet_charge (API Reference: /Create E-Wallet Charge)
      - EWallet.get_ewallet_charge_status (API Reference: /Get E-Wallet Charge Status)

    Static Methods for Object Creation:
      - CreditCard.helper_create_linkaja_item (For create_linkaja_payment)
      - EWallet.helper_create_basket_item (For ewallet charge)
    """

    @staticmethod
    def helper_create_linkaja_item(*, id, name, price, quantity, **kwargs):
        """Construct Installments Object for Charge

        Args:
          - id (str)
          - name (str)
          - price (int)
          - quantity (int)

        Return:
          - LinkajaItem
        """
        params = locals()
        del params["kwargs"]

        return LinkAjaItem.Query(**params)

    @staticmethod
    def helper_create_basket_item(
        *,
        reference_id: str,
        name: str,
        category: str,
        currency: str,
        price: int,
        quantity: int,
        type: str,
        url: str = None,
        description: str = None,
        sub_category: str = None,
        metadata: dict = None,
        **kwargs,
    ):
        """Construct Installments Object for Charge

        Args:
          - reference_id (str)
          - name (str)
          - category (str)
          - currency (str)
          - price (int)
          - quantity (int)
          - type (str)
          - url (str)
          - description (str)
          - sub_category (str)
          - metadata (dict)

        Return:
          - EWalletBasket
        """
        params = locals()
        del params["kwargs"]

        return EWalletBasket.Query(**params)

    @staticmethod
    def create_ovo_payment(
        *,
        external_id,
        amount,
        phone,
        for_user_id=None,
        x_idempotency_key=None,
        x_api_version=None,
        **kwargs,
    ):
        """Send POST Request to create OVO Payment (API Reference: eWallets/Create Payment)

        Args:
          - external_id (str)
          - amount (int)
          - phone (str)
          - **for_user_id (str) (XenPlatforms only)
          - **x_idempotency_key (str)
          - **x_api_version (str)

        Returns:
          OVOPayment

        Raises:
          XenditError

        """
        url = "/ewallets"
        headers, body = _extract_params(
            locals(),
            func_object=EWallet.create_ovo_payment,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        body["ewallet_type"] = "OVO"
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return OVOPayment(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def create_dana_payment(
        *,
        external_id,
        amount,
        callback_url,
        redirect_url,
        expiration_date=None,
        for_user_id=None,
        x_idempotency_key=None,
        x_api_version=None,
        **kwargs,
    ):
        """Send POST Request to create DANA Payment (API Reference: eWallets/Create Payment)

        Args:
          - external_id (str)
          - amount (int)
          - callback_url (str)
          - redirect_url (str)
          - **expiration_date (str)
          - **for_user_id (str) (XenPlatforms only)
          - **x_idempotency_key (str)
          - **x_api_version (str)

        Returns:
          DANAPayment

        Raises:
          XenditError

        """
        url = "/ewallets"
        headers, body = _extract_params(
            locals(),
            func_object=EWallet.create_dana_payment,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        body["ewallet_type"] = "DANA"
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return DANAPayment(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def create_linkaja_payment(
        *,
        external_id,
        phone,
        amount,
        items,
        callback_url,
        redirect_url,
        for_user_id=None,
        x_idempotency_key=None,
        x_api_version=None,
        **kwargs,
    ):
        """Send POST Request to create LinkAja Payment (API Reference: eWallets/Create Payment)

        Args:
          - external_id (str)
          - phone (str)
          - amount (int)
          - items (LinkAjaItem.Query[])
          - callback_url (str)
          - redirect_url (str)
          - **for_user_id (str) (XenPlatforms only)
          - **x_idempotency_key (str)
          - **x_api_version (str)

        Returns:
          LinkAjaPayment

        Raises:
          XenditError

        """
        url = "/ewallets"
        headers, body = _extract_params(
            locals(),
            func_object=EWallet.create_linkaja_payment,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        body["ewallet_type"] = "LINKAJA"
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return LinkAjaPayment(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def get_payment_status(
        *, external_id, ewallet_type, for_user_id=None, x_api_version=None, **kwargs
    ):
        """Get payment status of given external id (API Reference: eWallets/Get Payment Status)

        Args:
          - external_id (str)
          - ewallet_type (EWalletType)
          - **for_user_id (str) (XenPlatforms only)
          - **x_api_version (str)

        Returns:
          - OVOPaymentStatus (For EWalletType.OVO)
          - DANAPaymentStatus (For EWalletType.DANA)
          - LinkAjaPaymentStatus (For EWalletType.LINKAJA)

        Raises:
          XenditError

        """
        parsed_ewallet_type = EWallet._parse_ewallet_type(ewallet_type)
        url = f"/ewallets?external_id={external_id}&ewallet_type={parsed_ewallet_type}"
        headers, _ = _extract_params(
            locals(),
            func_object=EWallet.create_linkaja_payment,
            headers_params=["for_user_id", "x_api_version"],
        )
        kwargs["headers"] = headers

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            if ewallet_type == EWalletType.OVO:
                return OVOPaymentStatus(**resp.body)
            elif ewallet_type == EWalletType.DANA:
                return DANAPaymentStatus(**resp.body)
            elif ewallet_type == EWalletType.LINKAJA:
                return LinkAjaPaymentStatus(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def _parse_ewallet_type(ewallet_type):
        try:
            return ewallet_type.name
        except AttributeError:
            return ewallet_type

    @staticmethod
    def create_ewallet_charge(
        *,
        reference_id: str,
        currency: str,
        amount: int,
        checkout_method: str,
        channel_code: str = None,
        channel_properties: dict = None,
        customer_id: str = None,
        basket: list = None,
        metadata: dict = None,
        for_user_id: str = None,
        with_fee_rule: str = None,
        **kwargs,
    ):
        """Send POST Request to create EWallet Charge (API Reference: eWallets/Create E-Wallet Charge)

        Args:
          - reference_id (str)
          - currency (str)
          - amount (int)
          - checkout_method (str)
          - channel_code (str)
          - channel_properties (dict)
          - customer_id (str)
          - basket (list)
          - metadata (dict)
          - **for_user_id (str) (XenPlatforms only)
          - **with_fee_rule (str) (XenPlatforms only)

        Returns:
          EWalletCharge

        Raises:
          XenditError

        """
        url = "/ewallets/charges"
        headers, body = _extract_params(
            locals(),
            func_object=EWallet.create_ewallet_charge,
            headers_params=["for_user_id", "with_fee_rule"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return EWalletCharge(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def get_ewallet_charge_status(
        *,
        charge_id: str,
        for_user_id: str = None,
        **kwargs,
    ):
        """Get ewallet charge status of given charge id (API Reference: eWallets/Get E-Wallet Charge Status)

        Args:
          - charge_id (str)
          - **for_user_id (str) (XenPlatforms only)

        Returns:
          - EWalletCharge

        Raises:
          XenditError

        """
        url = f"/ewallets/charges/{charge_id}"
        headers, body = _extract_params(
            locals(),
            func_object=EWallet.get_ewallet_charge_status,
            headers_params=["for_user_id"],
        )
        kwargs["headers"] = headers

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return EWalletCharge(**resp.body)
        else:
            raise XenditError(resp)
