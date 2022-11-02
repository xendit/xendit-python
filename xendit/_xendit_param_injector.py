from inspect import signature



from .models import Balance
from .models import BatchDisbursement
from .models import CardlessCredit
from .models import CreditCard
from .models import DirectDebit
from .models import Disbursement
from .models import EWallet
from .models import Invoice
from .models import PaymentMethod
from .models import PaymentRequest
from .models import Payout
from .models import QRCode
from .models import RecurringPayment
from .models import Refund
from .models import RetailOutlet
from .models import VirtualAccount
from .models import XenPlatform


class _XenditParamInjector:
    """Builder class to inject parameters (api_key, base_url, http_client) to feature class"""

    def __init__(self, params):
        self.params = params

    def instantiate_balance(self) -> Balance:
        return self.instantiate(Balance)

    def instantiate_batch_disbursement(self) -> BatchDisbursement:
        return self.instantiate(BatchDisbursement)

    def instantiate_cardless_credit(self) -> CardlessCredit:
        return self.instantiate(CardlessCredit)

    def instantiate_credit_card(self) -> CreditCard:
        return self.instantiate(CreditCard)

    def instantiate_direct_debit(self) -> DirectDebit:
        return self.instantiate(DirectDebit)

    def instantiate_disbursement(self) -> Disbursement:
        return self.instantiate(Disbursement)

    def instantiate_ewallet(self) -> EWallet:
        return self.instantiate(EWallet)

    def instantiate_invoice(self) -> Invoice:
        return self.instantiate(Invoice)

    def instantiate_payment_method(self) -> PaymentMethod:
        return self.instantiate(PaymentMethod)
    
    def instantiate_payment_request(self) -> PaymentRequest:
        return self.instantiate(PaymentRequest)

    def instantiate_payout(self) -> Payout:
        return self.instantiate(Payout)

    def instantiate_qrcode(self) -> QRCode:
        return self.instantiate(QRCode)

    def instantiate_recurring_payment(self) -> RecurringPayment:
        return self.instantiate(RecurringPayment)

    def instantiate_refund(self) -> Refund:
        return self.instantiate(Refund)

    def instantiate_retail_outlet(self) -> RetailOutlet:
        return self.instantiate(RetailOutlet)

    def instantiate_virtual_account(self) -> VirtualAccount:
        return self.instantiate(VirtualAccount)

    def instantiate_xenplatform(self) -> XenPlatform:
        return self.instantiate(XenPlatform)

    def instantiate(self, injected_class):
        """Inject every static method in `injected_class` with provided parameters.

        Args:
          - injected_class (class): Class that will be injected

        Return:
          injected_class
        """
        params = self.params

        injected_class = type(
            injected_class.__name__,
            injected_class.__bases__,
            dict(injected_class.__dict__),
        )
        for keys, value in vars(injected_class).items():
            if type(value) == staticmethod and not keys.startswith("_"):
                _XenditParamInjector._inject_function(
                    injected_class, params, keys, value
                )
        return injected_class

    @staticmethod
    def _inject_function(injected_class, params, func_name, func_value):
        """Inject `func_name` function with params"""
        api_key, base_url, http_client = params
        attr = func_value.__func__

        def inject_func_with_api_key(*args, **kwargs):
            kwargs["api_key"] = api_key
            kwargs["base_url"] = base_url
            kwargs["http_client"] = http_client
            result = attr(*args, **kwargs)
            return result

        inject_func_with_api_key.__signature__ = signature(attr)
        setattr(injected_class, func_name, staticmethod(inject_func_with_api_key))
