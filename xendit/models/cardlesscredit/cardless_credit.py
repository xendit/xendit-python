from xendit.models._base_model import BaseModel
from xendit.xendit_error import XenditError
from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params

from .payment import (
    CardlessCreditCustomerDetails,
    CardlessCreditPayment,
    CardlessCreditPaymentTypeCalculation,
    CardlessCreditShippingAddress,
)
from .cardless_credit_item import CardlessCreditItem


class CardlessCredit(BaseModel):
    """CardlessCredit class (API Reference: CardlessCredit)

    Static Methods:
      - CardlessCredit.create_payment (API Reference: /Create Payment or Generate Checkout URL)
      - CardlessCredit.calculate_payment_type (API Reference: /Get Payment Status)

    Static Methods for Object Creation:
      - CardlessCredit.helper_create_item (For CardlessCreditItem in create_payment)
      - CardlessCredit.helper_create_customer_details (For CardlessCreditCustomerDetails in create_payment)
      - CardlessCredit.helper_create_shipping_address (For CardlessCreditShippingAdress in create_payment)
    """

    @staticmethod
    def helper_create_item(*, id, name, price, type, url, quantity, **kwargs):
        """Construct Cardless Credit Item Object

        Args:
          - id (str)
          - name (str)
          - price (int)
          - type (str)
          - url (str)
          - quantity (str)

        Return:
          - CardlessCreditItem
        """
        params = locals()
        del params["kwargs"]

        return CardlessCreditItem.Query(**params)

    def helper_create_customer_details(
        *, first_name, last_name, email, phone, **kwargs
    ):
        """Construct Cardless Credit Customer Details Object

        Args:
          - first_name (str)
          - last_name (str)
          - email (str)
          - phone (str)

        Return:
          - CardlessCreditCustomerDetails
        """
        params = locals()
        del params["kwargs"]

        return CardlessCreditCustomerDetails.Query(**params)

    def helper_create_shipping_address(
        *,
        first_name,
        last_name,
        address,
        city,
        postal_code,
        phone,
        country_code,
        **kwargs,
    ):
        """Construct Cardless Credit Customer Details Object

        Args:
          - first_name (str)
          - last_name (str)
          - address (str)
          - city (str)
          - postal_code (str)
          - phone (str)
          - country_code (str)

        Return:
          - CardlessCreditShippingAdress
        """
        params = locals()
        del params["kwargs"]

        return CardlessCreditShippingAddress.Query(**params)

    @staticmethod
    def create_payment(
        *,
        cardless_credit_type,
        external_id,
        amount,
        payment_type,
        items,
        customer_details,
        shipping_address,
        redirect_url,
        callback_url,
        x_idempotency_key=None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Create a cardless credit payment (API Reference: Cardless Credit/Create Payment or Generate Checkout URL)

        Args:
          - cardless_credit_type (CardlessCreditType)
          - external_id (str)
          - amount (int)
          - payment_type (str)
          - items (CardlessCreditItem[])
          - customer_details (CardlessCreditCustomerDetails)
          - shipping_address (CardlessCreditShippingAddress)
          - redirect_url (str)
          - callback_url (str)
          - **for_user_id (str) (XenPlatform only)
          - **x_idempotency_key (str)
          - **x_api_version (str)

        Returns
          CardlessCredit

        Raises
          XenditError

        """
        cardless_credit_type = CardlessCredit._parse_cardless_credit_type(
            cardless_credit_type
        )
        url = "/cardless-credit"
        headers, body = _extract_params(
            locals(),
            func_object=CardlessCredit.create_payment,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return CardlessCreditPayment(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def calculate_payment_type(
        *,
        cardless_credit_type,
        amount,
        items,
        x_idempotency_key=None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Calculate Payment Types feature helps merchants to get an accurate value of the installment offered to end customers by the cardless credit provider
        (API Reference: Cardless Credit/Calculate Payment Types)

        Args:
          - cardless_credit_type (str)
          - amount (int)
          - items (CardlessCreditItem[])
          - **for_user_id (str) (XenPlatform only)
          - **x_idempotency_key (str)
          - **x_api_version (str)

        Returns
          CardlessCreditPaymentType

        Raises
          XenditError

        """
        cardless_credit_type = CardlessCredit._parse_cardless_credit_type(
            cardless_credit_type
        )
        url = "/cardless-credit/payment-types"
        headers, body = _extract_params(
            locals(),
            func_object=CardlessCredit.calculate_payment_type,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return CardlessCreditPaymentTypeCalculation(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def _parse_cardless_credit_type(cardless_credit_type):
        try:
            return cardless_credit_type.name
        except AttributeError:
            return cardless_credit_type
