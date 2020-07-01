from print_running_function import print_running_function

# Hackish method to import from another directory
# Useful while xendit-python isn't released yet to the public
import importlib.machinery

loader = importlib.machinery.SourceFileLoader("xendit", "../xendit/__init__.py")
xendit = loader.load_module("xendit")


class CreateVirtualAccount:
    @staticmethod
    def run(xendit_instance, external_id, bank_code, name, **kwargs):
        try:
            virtual_account = xendit_instance.VirtualAccount.create(
                external_id=external_id, bank_code=bank_code, name=name, **kwargs
            )
            print(virtual_account)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args_1 = {
            "external_id": "demo_1475459775872",
            "bank_code": "BNI",
            "name": "Rika Sutanto",
        }
        print_running_function("xendit.VirtualAccount.create", args_1)
        CreateVirtualAccount.run(xendit_instance, **args_1)

        args_2 = {
            "external_id": "demo_1475459775872",
            "bank_code": "CIB",
            "name": "Rika Sutanto",
        }
        print_running_function("xendit.VirtualAccount.create", args_2)
        CreateVirtualAccount.run(xendit_instance, **args_2)


class GetVirtualAccountBanks:
    @staticmethod
    def run(xendit_instance):
        try:
            virtual_account_banks = xendit_instance.VirtualAccount.get_banks()
            print(virtual_account_banks)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        print("Running xendit.VirtualAccount.get_banks():")
        GetVirtualAccountBanks.run(xendit_instance)


class GetVirtualAccount:
    @staticmethod
    def run(xendit_instance, id, **kwargs):
        try:
            virtual_account = xendit_instance.VirtualAccount.get(id=id, **kwargs)
            print(virtual_account)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        print('Running xendit.VirtualAccount.get(id="5eec3a3e8dd9ea2fc97d6728"):')
        GetVirtualAccount.run(xendit_instance, "5eec3a3e8dd9ea2fc97d6728")

        print('Running xendit.VirtualAccount.get(id="random-id"):')
        GetVirtualAccount.run(xendit_instance, "random-id")


class UpdateVirtualAccount:
    @staticmethod
    def run(xendit_instance, id, **kwargs):
        try:
            virtual_account = xendit_instance.VirtualAccount.update(id=id, **kwargs)
            print(virtual_account)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        print(
            'Running xendit.VirtualAccount.update(id="5eec3a3e8dd9ea2fc97d6728", is_single_use=True):'
        )
        UpdateVirtualAccount.run(
            xendit_instance, "5eec3a3e8dd9ea2fc97d6728", is_single_use=True
        )

        print('Running xendit.VirtualAccount.update("random-id"):')
        UpdateVirtualAccount.run(xendit_instance, "random-id")


class GetVirtualAccountPayment:
    @staticmethod
    def run(xendit_instance, payment_id, **kwargs):
        try:
            virtual_account = xendit_instance.VirtualAccount.get_payment(
                payment_id=payment_id, **kwargs
            )
            print(virtual_account)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        print(
            'Running xendit.VirtualAccount.get_payment(payment_id="5ef18efca7d10d1b4d61fb52"):'
        )
        GetVirtualAccountPayment.run(xendit_instance, "5ef18efca7d10d1b4d61fb52")

        print('Running xendit.VirtualAccount.get_payment(payment_id="random-id"):')
        GetVirtualAccountPayment.run(xendit_instance, "random-id")


def ask_virtual_account_input():
    print("Input the action that you want to use")
    print("0. Exit")
    print("1. Create Virtual Account")
    print("2. Get Virtual Account Banks")
    print("3. Get Virtual Account")
    print("4. Update Virtual Account")
    print("5. Get Virtual Account Payment")
    try:
        return int(input())
    except ValueError:
        print("Invalid input. Please type a number")
        return ask_virtual_account_input()


def virtual_account_example(xendit_instance):
    virtual_account_input = ask_virtual_account_input()
    while virtual_account_input != 0:
        if virtual_account_input == 1:
            print("Running example of Create Virtual Account")
            CreateVirtualAccount.example(xendit_instance)
        elif virtual_account_input == 2:
            print("Running example of Get Virtual Account Banks")
            GetVirtualAccountBanks.example(xendit_instance)
        elif virtual_account_input == 3:
            print("Running example of Get Virtual Account")
            GetVirtualAccount.example(xendit_instance)
        elif virtual_account_input == 4:
            print("Running example of Update Virtual Account")
            UpdateVirtualAccount.example(xendit_instance)
        elif virtual_account_input == 5:
            print("Running example of Get Virtual Account Payment")
            GetVirtualAccountPayment.example(xendit_instance)
        virtual_account_input = ask_virtual_account_input()
