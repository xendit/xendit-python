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
                external_id, bank_code, name, **kwargs
            )
            print(virtual_account)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        print(
            'Running xendit.VirtualAccount.create("demo_1475459775872", "BNI", "Rika Sutanto"):'
        )
        CreateVirtualAccount.run(
            xendit_instance, "demo_1475459775872", "BNI", "Rika Sutanto",
        )

        print(
            'Running xendit.VirtualAccount.create("demo_1475459775872", "CIB", "Rika Sutanto"):'
        )
        CreateVirtualAccount.run(
            xendit_instance, "demo_1475459775872", "CIB", "Rika Sutanto",
        )


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
            virtual_account = xendit_instance.VirtualAccount.get(id, **kwargs)
            print(virtual_account)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        print('Running xendit.VirtualAccount.get("5eec3a3e8dd9ea2fc97d6728"):')
        GetVirtualAccount.run(xendit_instance, "5eec3a3e8dd9ea2fc97d6728")

        print('Running xendit.VirtualAccount.get("random-id"):')
        GetVirtualAccount.run(xendit_instance, "random-id")


def ask_virtual_account_input():
    print("Input the action that you want to use")
    print("0. Exit")
    print("1. Create Virtual Account")
    print("2. Get Virtual Account Banks")
    print("3. Get Virtual Account")
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
        virtual_account_input = ask_virtual_account_input()
