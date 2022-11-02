import requests

from ._xendit_param_injector import _XenditParamInjector

from .network import HTTPClientInterface


class Xendit:
    """Xendit instance. Initialize this with your API Key."""

    def __init__(
        self,
        api_key,
        base_url="https://api.xendit.co/",
        http_client: HTTPClientInterface = requests,
    ):
        injected_params = (api_key, base_url, http_client)
        param_injector = _XenditParamInjector(injected_params)

        self.Balance = param_injector.instantiate_balance()
        self.BatchDisbursement = param_injector.instantiate_batch_disbursement()
        self.CardlessCredit = param_injector.instantiate_cardless_credit()
        self.CreditCard = param_injector.instantiate_credit_card()
        self.DirectDebit = param_injector.instantiate_direct_debit()
        self.Disbursement = param_injector.instantiate_disbursement()
        self.EWallet = param_injector.instantiate_ewallet()
        self.Invoice = param_injector.instantiate_invoice()
        self.PaymentMethod = param_injector.instantiate_payment_method()
        self.PaymentRequest = param_injector.instantiate_payment_request()
        self.Refund = param_injector.instantiate_refund()
        self.Payout = param_injector.instantiate_payout()
        self.QRCode = param_injector.instantiate_qrcode()
        self.RecurringPayment = param_injector.instantiate_recurring_payment()
        self.RetailOutlet = param_injector.instantiate_retail_outlet()
        self.VirtualAccount = param_injector.instantiate_virtual_account()
        self.XenPlatform = param_injector.instantiate_xenplatform()