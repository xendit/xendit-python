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
            customer = xendit_instance.DirectDebit.get_customer_by_ref_id(**kwargs,)
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


def ask_direct_debit_input():
    print("Input the action that you want to use")
    print("0. Exit")
    print("1. Create Customer")
    print("2. Get Customer by Reference ID")
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
        direct_debit_input = ask_direct_debit_input()
