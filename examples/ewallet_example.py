from print_running_function import print_running_function

import time

# Hackish method to import from another directory
# Useful while xendit-python isn't released yet to the public
import importlib.machinery

loader = importlib.machinery.SourceFileLoader("xendit", "../xendit/__init__.py")
xendit = loader.load_module("xendit")


class CreateOVOPayment:
    @staticmethod
    def run(xendit_instance, external_id, amount, phone, **kwargs):
        try:
            ewallet = xendit_instance.EWallet.create_ovo_payment(
                external_id=external_id, amount=amount, phone=phone,
            )
            print(ewallet)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "external_id": f"ovo-ewallet-testing-id-{int(time.time())}",
            "amount": "80001",
            "phone": "08123123123",
        }
        print_running_function("xendit.EWallet.create_ovo_payment", args)
        CreateOVOPayment.run(xendit_instance, **args)


class CreateDANAPayment:
    @staticmethod
    def run(xendit_instance, external_id, amount, callback_url, redirect_url, **kwargs):
        try:
            ewallet = xendit_instance.EWallet.create_dana_payment(
                external_id=external_id,
                amount=amount,
                callback_url=callback_url,
                redirect_url=redirect_url,
                **kwargs,
            )
            print(ewallet)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "external_id": f"dana-ewallet-test-{int(time.time())}",
            "amount": "1001",
            "callback_url": "https://my-shop.com/callbacks",
            "redirect_url": "https://my-shop.com/home",
        }
        print_running_function("xendit.EWallet.create_dana_payment", args)
        CreateDANAPayment.run(xendit_instance, **args)


class CreateLinkAjaPayment:
    @staticmethod
    def run(
        xendit_instance,
        external_id,
        phone,
        amount,
        items,
        callback_url,
        redirect_url,
        **kwargs,
    ):
        try:
            ewallet = xendit_instance.EWallet.create_linkaja_payment(
                external_id=external_id,
                phone=phone,
                amount=amount,
                items=items,
                callback_url=callback_url,
                redirect_url=redirect_url,
                **kwargs,
            )
            print(ewallet)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        items = []
        item = xendit.EWallet.helper_create_linkaja_item(
            id="123123", name="Phone Case", price=100000, quantity=1
        )
        items.append(item)

        args = {
            "external_id": f"linkaja-ewallet-test-{int(time.time())}",
            "phone": "089911111111",
            "items": {items},
            "amount": 300000,
            "callback_url": "https://my-shop.com/callbacks",
            "redirect_url": "https://xendit.co/",
        }
        print_running_function("xendit.EWallet.create_linkaja_payment", args)
        CreateLinkAjaPayment.run(xendit_instance, **args)


class GetOVOPaymentStatus:
    @staticmethod
    def run(xendit_instance, external_id, ewallet_type, **kwargs):
        try:
            ewallet = xendit_instance.EWallet.get_payment_status(
                external_id=external_id, ewallet_type=ewallet_type, **kwargs,
            )
            print(ewallet)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "ewallet_type": xendit.EWalletType.OVO,
            "external_id": "ovo-ewallet-testing-id-1234",
        }
        print_running_function("xendit.EWallet.get_payment_status", args)
        GetOVOPaymentStatus.run(xendit_instance, **args)


class GetDANAPaymentStatus:
    @staticmethod
    def run(xendit_instance, external_id, ewallet_type, **kwargs):
        try:
            ewallet = xendit_instance.EWallet.get_payment_status(
                external_id=external_id, ewallet_type=ewallet_type, **kwargs,
            )
            print(ewallet)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "ewallet_type": xendit.EWalletType.DANA,
            "external_id": "dana-ewallet-test-1234",
        }
        print_running_function("xendit.EWallet.get_payment_status", args)
        GetDANAPaymentStatus.run(xendit_instance, **args)


class GetLinkAjaPaymentStatus:
    @staticmethod
    def run(xendit_instance, external_id, ewallet_type, **kwargs):
        try:
            ewallet = xendit_instance.EWallet.get_payment_status(
                external_id=external_id, ewallet_type=ewallet_type, **kwargs,
            )
            print(ewallet)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "ewallet_type": xendit.EWalletType.LINKAJA,
            "external_id": "linkaja-ewallet-test-123",
        }
        print_running_function("xendit.EWallet.get_payment_status", args)
        GetLinkAjaPaymentStatus.run(xendit_instance, **args)


class CreateEWalletCharge:
    @staticmethod
    def run(
        xendit_instance,
        reference_id,
        currency,
        amount,
        checkout_method,
        channel_code=None,
        channel_properties=None,
        customer_id=None,
        basket=None,
        metadata=None,
        **kwargs,
    ):
        try:
            ewallet_charge = xendit_instance.EWallet.create_ewallet_charge(
                reference_id=reference_id,
                currency=currency,
                amount=amount,
                checkout_method=checkout_method,
                channel_code=channel_code,
                channel_properties=channel_properties,
                customer_id=customer_id,
                basket=basket,
                metadata=metadata,
                **kwargs,
            )
            print(ewallet_charge)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        basket = []
        basket_item = xendit.EWallet.helper_create_basket_item(
            reference_id = "basket-product-ref-id",
            name = "product_name",
            category = "mechanics",
            currency = "IDR",
            price = 50000,
            quantity = 5,
            type = "wht",
            sub_category = "evr",
            metadata = {
                "meta": "data"
            }
        )
        basket.append(basket_item)

        args = {
            "reference_id": "test-reference-id",
            "currency": "IDR",
            "amount": 1688,
            "checkout_method": "ONE_TIME_PAYMENT",
            "channel_code": "ID_SHOPEEPAY",
            "channel_properties": {
                "success_redirect_url": "https://yourwebsite.com/order/123",
            },
            "basket": basket,
            "metadata": {
                "meta2": "data2",
            },
        }
        print_running_function("xendit.EWallet.create_ewallet_charge", args)
        CreateEWalletCharge.run(xendit_instance, **args)


class GetEWalletChargeStatus:
    @staticmethod
    def run(xendit_instance, charge_id, **kwargs):
        try:
            ewallet = xendit_instance.EWallet.get_ewallet_charge_status(
                charge_id=charge_id, **kwargs,
            )
            print(ewallet)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "charge_id": "ewc_f3925450-5c54-4777-98c1-fcf22b0d1e1c",
        }
        print_running_function("xendit.EWallet.get_ewallet_charge_status", args)
        GetEWalletChargeStatus.run(xendit_instance, **args)


def ask_ewallet_input():
    print("Input the action that you want to use")
    print("0. Exit")
    print("1. Create OVO Payment")
    print("2. Create DANA Payment")
    print("3. Create LinkAja Payment")
    print("4. Get OVO Payment Status")
    print("5. Get DANA Payment Status")
    print("6. Get LinkAja Payment Status")
    print("7. Create E-Wallet Charge")
    print("8. Get E-Wallet Charge Status")
    try:
        return int(input())
    except ValueError:
        print("Invalid input. Please type a number")
        return ask_ewallet_input()


def ewallet_example(xendit_instance):
    ewallet_input = ask_ewallet_input()
    while ewallet_input != 0:
        if ewallet_input == 1:
            print("Running example of Create OVO Payment")
            CreateOVOPayment.example(xendit_instance)
        elif ewallet_input == 2:
            print("Running example of Create DANA Payment")
            CreateDANAPayment.example(xendit_instance)
        elif ewallet_input == 3:
            print("Running example of Create LinkAja Payment")
            CreateLinkAjaPayment.example(xendit_instance)
        elif ewallet_input == 4:
            print("Running example of Get Payment Status of OVO")
            GetOVOPaymentStatus.example(xendit_instance)
        elif ewallet_input == 5:
            print("Running example of Get Payment Status of DANA")
            GetDANAPaymentStatus.example(xendit_instance)
        elif ewallet_input == 6:
            print("Running example of Get Payment Status of LinkAja")
            GetLinkAjaPaymentStatus.example(xendit_instance)
        elif ewallet_input == 7:
            print("Running example of Create E-Wallet Charge")
            CreateEWalletCharge.example(xendit_instance)
        elif ewallet_input == 8:
            print("Running example of Get E-Wallet Charge Status")
            GetEWalletChargeStatus.example(xendit_instance)
        ewallet_input = ask_ewallet_input()
