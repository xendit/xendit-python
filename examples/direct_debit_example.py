from print_running_function import print_running_function

import time

# Hackish method to import from another directory
# Useful while xendit-python isn't released yet to the public
import importlib.machinery

loader = importlib.machinery.SourceFileLoader("xendit", "../xendit/__init__.py")
xendit = loader.load_module("xendit")


class CreateCustomer:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            customer = xendit_instance.DirectDebit.create_customer(**kwargs)
            print(customer)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "reference_id": f"merc-{int(time.time())}",
            "email": "t@x.co",
            "given_names": "Adyaksa",
        }
        print_running_function("xendit.DirectDebit.create_customer", args)
        CreateCustomer.run(xendit_instance, **args)


class GetCustomerByRefID:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            customer = xendit_instance.DirectDebit.get_customer_by_ref_id(**kwargs)
            print(customer)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        reference_id = input("Please input your reference_id: ")
        args = {
            "reference_id": reference_id,
        }
        print_running_function("xendit.DirectDebit.get_customer_by_ref_id", args)
        GetCustomerByRefID.run(xendit_instance, **args)


class InitializeTokenization:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            customer = xendit_instance.DirectDebit.initialize_tokenization(**kwargs)
            print(customer)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "customer_id": "ed20b5db-df04-41fc-8018-8ea4ac4d1030",
            "channel_code": "DC_BRI",
            "properties": {
                "account_mobile_number": "+62818555988",
                "card_last_four": "8888",
                "card_expiry": "06/24",
                "account_email": "test.email@xendit.co",
            },
        }
        print_running_function("xendit.DirectDebit.initialize_tokenization", args)
        InitializeTokenization.run(xendit_instance, **args)


class ValidateTokenOTP:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            linked_account_token = xendit_instance.DirectDebit.validate_token_otp(
                **kwargs
            )
            print(linked_account_token)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        linked_account_token_id = input("Please input your linked_account_token_id: ")
        args = {
            "linked_account_token_id": linked_account_token_id,
            "otp_code": "333000",
        }
        print_running_function("xendit.DirectDebit.validate_token_otp", args)
        ValidateTokenOTP.run(xendit_instance, **args)


class GetAccessibleAccountsByToken:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            customer = xendit_instance.DirectDebit.get_accessible_accounts_by_token(
                **kwargs
            )
            print(customer)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        linked_account_token_id = input("Please input your linked_account_token_id: ")
        args = {
            "linked_account_token_id": linked_account_token_id,
        }
        print_running_function(
            "xendit.DirectDebit.get_accessible_account_by_token", args
        )
        GetAccessibleAccountsByToken.run(xendit_instance, **args)


def ask_direct_debit_input():
    print("Input the action that you want to use")
    print("0. Exit")
    print("1. Create Customer")
    print("2. Get Customer by Reference ID")
    print("3. Initialize Linked Account Tokenization")
    print("4. Validate OTP for Linked Account Token")
    print("5. Retrieve Accessible Accounts by Linked Account Token")
    try:
        return int(input())
    except ValueError:
        print("Invalid input. Please type a number")
        return ask_direct_debit_input()


def direct_debit_example(xendit_instance):
    direct_debit_input = ask_direct_debit_input()
    while direct_debit_input != 0:
        if direct_debit_input == 1:
            print("Running example of Create Customer")
            CreateCustomer.example(xendit_instance)
        elif direct_debit_input == 2:
            print("Running example of Get Customer by Reference ID")
            GetCustomerByRefID.example(xendit_instance)
        elif direct_debit_input == 3:
            print("Running example of Initialize Linked Account Tokenization")
            InitializeTokenization.example(xendit_instance)
        elif direct_debit_input == 4:
            print("Running example of Validate OTP for Linked Account Token")
            ValidateTokenOTP.example(xendit_instance)
        elif direct_debit_input == 5:
            print(
                "Running example of Retrieve Accessible Accounts by Linked Account Token"
            )
            GetAccessibleAccountsByToken.example(xendit_instance)
        direct_debit_input = ask_direct_debit_input()
