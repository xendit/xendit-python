from print_running_function import print_running_function

import xendit


class CreateVirtualAccount:
    @staticmethod
    def run(xendit_instance, external_id, bank_code, name, **kwargs):
        try:
            virtual_account = xendit_instance.VirtualAccount.create(
                external_id=external_id, bank_code=bank_code, name=name, **kwargs,
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
        args = {}
        print_running_function("xendit.VirtualAccount.get_banks", args)
        GetVirtualAccountBanks.run(xendit_instance)


class GetVirtualAccount:
    @staticmethod
    def run(xendit_instance, id, **kwargs):
        try:
            virtual_account = xendit_instance.VirtualAccount.get(id=id, **kwargs,)
            print(virtual_account)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "id": "5eec3a3e8dd9ea2fc97d6728",
        }
        print_running_function("xendit.VirtualAccount.get", args)
        GetVirtualAccount.run(xendit_instance, **args)


class UpdateVirtualAccount:
    @staticmethod
    def run(xendit_instance, id, **kwargs):
        try:
            virtual_account = xendit_instance.VirtualAccount.update(id=id, **kwargs,)
            print(virtual_account)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "id": "5eec3a3e8dd9ea2fc97d6728",
            "is_single_use": True,
        }
        print_running_function("xendit.VirtualAccount.update", args)
        UpdateVirtualAccount.run(xendit_instance, **args)


class GetVirtualAccountPayment:
    @staticmethod
    def run(xendit_instance, payment_id, **kwargs):
        try:
            virtual_account = xendit_instance.VirtualAccount.get_payment(
                payment_id=payment_id, **kwargs,
            )
            print(virtual_account)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {"payment_id": "5ef18efca7d10d1b4d61fb52"}
        print_running_function("xendit.VirtualAccount.get_payment", args)
        GetVirtualAccountPayment.run(xendit_instance, **args)


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
