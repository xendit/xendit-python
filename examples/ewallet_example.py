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
                external_id, amount, phone
            )
            print(ewallet)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        external_id = f"ovo-ewallet-testing-id-{int(time.time())}"
        amount = "8888"
        phone = "08123123123"
        print(
            f'Running xendit.EWallet.create_ovo_payment("{external_id}", "{amount}", "{phone}"):'
        )
        CreateOVOPayment.run(xendit_instance, external_id, amount, phone)


class CreateDANAPayment:
    @staticmethod
    def run(xendit_instance, external_id, amount, callback_url, redirect_url, **kwargs):
        try:
            ewallet = xendit_instance.EWallet.create_dana_payment(
                external_id, amount, callback_url, redirect_url, **kwargs
            )
            print(ewallet)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        external_id = f"dana-ewallet-test-{int(time.time())}"
        amount = "1001"
        callback_url = "https://my-shop.com/callbacks"
        redirect_url = "https://my-shop.com/home"
        print(
            f'Running xendit.EWallet.create_dana_payment("{external_id}", "{amount}", "{callback_url}", "{redirect_url}"):'
        )
        CreateDANAPayment.run(
            xendit_instance, external_id, amount, callback_url, redirect_url
        )


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
                external_id, phone, amount, items, callback_url, redirect_url, **kwargs
            )
            print(ewallet)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        external_id = f"linkaja-ewallet-test-{int(time.time())}"
        phone = "089911111111"
        amount = 300000
        items = []
        items.append(
            xendit.LinkAjaItem(id="123123", name="Phone Case", price=100000, quantity=1)
        )
        callback_url = "https://my-shop.com/callbacks"
        redirect_url = "https://xendit.co/"
        print(
            f'Running xendit.EWallet.create_linkaja_payment("{external_id}", "{phone}", {amount}, {items}, "{callback_url}", "{redirect_url}"):'
        )
        CreateLinkAjaPayment.run(
            xendit_instance,
            external_id,
            phone,
            amount,
            items,
            callback_url,
            redirect_url,
        )


class GetOVOPaymentStatus:
    @staticmethod
    def run(xendit_instance, external_id, ewallet_type, **kwargs):
        try:
            ewallet = xendit_instance.EWallet.get_payment_status(
                external_id, ewallet_type, **kwargs
            )
            print(ewallet)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        ewallet_type = xendit.EWalletType.OVO
        external_id = "ovo-ewallet-testing-id-1234"
        print(
            f"Running xendit.EWallet.get_payment_status('{external_id}', {ewallet_type}):"
        )
        GetOVOPaymentStatus.run(xendit_instance, external_id, ewallet_type)


class GetDANAPaymentStatus:
    @staticmethod
    def run(xendit_instance, external_id, ewallet_type, **kwargs):
        try:
            ewallet = xendit_instance.EWallet.get_payment_status(
                external_id, ewallet_type, **kwargs
            )
            print(ewallet)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        ewallet_type = xendit.EWalletType.DANA
        external_id = "dana-ewallet-test-1234"
        print(
            f"Running xendit.EWallet.get_payment_status('{external_id}', {ewallet_type}):"
        )
        GetDANAPaymentStatus.run(xendit_instance, external_id, ewallet_type)


class GetLinkAjaPaymentStatus:
    @staticmethod
    def run(xendit_instance, external_id, ewallet_type, **kwargs):
        try:
            ewallet = xendit_instance.EWallet.get_payment_status(
                external_id, ewallet_type, **kwargs
            )
            print(ewallet)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        ewallet_type = xendit.EWalletType.LINKAJA
        external_id = "linkaja-ewallet-test-123"
        print(
            f"Running xendit.EWallet.get_payment_status('{external_id}', {ewallet_type}):"
        )
        GetLinkAjaPaymentStatus.run(xendit_instance, external_id, ewallet_type)


def ask_ewallet_input():
    print("Input the action that you want to use")
    print("0. Exit")
    print("1. Create OVO Payment")
    print("2. Create DANA Payment")
    print("3. Create LinkAja Payment")
    print("4. Get OVO Payment Status")
    print("5. Get DANA Payment Status")
    print("6. Get LinkAja Payment Status")
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
        ewallet_input = ask_ewallet_input()
