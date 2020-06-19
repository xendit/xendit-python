# Hackish method to import from another directory
# Useful while xendit-python isn't released yet to the public
import importlib.machinery

loader = importlib.machinery.SourceFileLoader("xendit", "../xendit/__init__.py")
xendit = loader.load_module("xendit")


class CreateVirtualAccount:
    @staticmethod
    def run(func, external_id, bank_code, name):
        try:
            print(func(external_id, bank_code, name))
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        print(
            'Running xendit.VirtualAccount.create("demo_1475459775872", "BNI", "Rika Sutanto"):'
        )
        CreateVirtualAccount.run(
            xendit_instance.VirtualAccount.create,
            "demo_1475459775872",
            "BNI",
            "Rika Sutanto",
        )

        print(
            'Running xendit.VirtualAccount.create("demo_1475459775872", "CIB", "Rika Sutanto"):'
        )
        CreateVirtualAccount.run(
            xendit_instance.VirtualAccount.create,
            "demo_1475459775872",
            "CIB",
            "Rika Sutanto",
        )


class GetVirtualAccountBanks:
    @staticmethod
    def run(func):
        try:
            print(func())
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        print("Running xendit.VirtualAccount.get_banks():")
        GetVirtualAccountBanks.run(xendit_instance.VirtualAccount.get_banks)


def ask_virtual_account_input():
    print("Input the action that you want to use")
    print("0. Exit")
    print("1. Create Virtual Account")
    print("2. Get Virtual Account Banks")
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
        virtual_account_input = ask_virtual_account_input()
