import time

from print_running_function import print_running_function

# Hackish method to import from another directory
# Useful while xendit-python isn't released yet to the public
import importlib.machinery

loader = importlib.machinery.SourceFileLoader("xendit", "../xendit/__init__.py")
xendit = loader.load_module("xendit")


class CreateAccount:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            xenplatform_account = xendit_instance.XenPlatform.create_account(**kwargs)
            print(xenplatform_account)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "account_email": f"test-xenplatform-{int(time.time())}@pythonxendit.co",
            "type": xendit.XenPlatformAccountType.OWNED,
            "business_profile": {"business_name": "python-xendit"},
        }
        print_running_function("xendit.XenPlatform.create_account", args)
        CreateAccount.run(xendit_instance, **args)


class SetCallbackURL:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            xenplatform_callback_url = xendit_instance.XenPlatform.set_callback_url(
                **kwargs
            )
            print(xenplatform_callback_url)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "type": xendit.XenPlatformURLType.INVOICE,
            "url": "https://test-url-invoice.com",
        }
        print_running_function("xendit.XenPlatform.set_callback_url", args)
        SetCallbackURL.run(xendit_instance, **args)


class Transfers:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            xenplatform_transfers = xendit_instance.XenPlatform.transfers(**kwargs)
            print(xenplatform_transfers)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        source_user_id = input("Please input your source_user_id: ")
        destination_user_id = input("Please input your destination_user_id: ")
        args = {
            "reference": "123",
            "amount": 10000,
            "source_user_id": source_user_id,
            "destination_user_id": destination_user_id,
        }
        print_running_function("xendit.XenPlatform.transfers", args)
        Transfers.run(xendit_instance, **args)


def ask_xenplatform_input():
    print("Input the action that you want to use")
    print("0. Exit")
    print("1. Create Account")
    print("2. Set Callback URLs")
    print("3. Transfers")
    try:
        return int(input())
    except ValueError:
        print("Invalid input. Please type a number")
        return ask_xenplatform_input()


def xenplatform_example(xendit_instance):
    xenplatform_input = ask_xenplatform_input()
    while xenplatform_input != 0:
        if xenplatform_input == 1:
            print("Running example of Create Account")
            CreateAccount.example(xendit_instance)
        elif xenplatform_input == 2:
            print("Running example of Set Callback URLs")
            SetCallbackURL.example(xendit_instance)
        elif xenplatform_input == 3:
            print("Running example of Transfers")
            Transfers.example(xendit_instance)
        xenplatform_input = ask_xenplatform_input()
