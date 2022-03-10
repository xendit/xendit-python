from print_running_function import print_running_function

# # Hackish method to import from another directory
# # Useful while xendit-python isn't released yet to the public
# import importlib.machinery

# loader = importlib.machinery.SourceFileLoader("xendit", "../xendit/__init__.py")
# xendit = loader.load_module("xendit")

import xendit


class GetBalance:
    @staticmethod
    def run(xendit_instance, account_type):
        try:
            balance = xendit_instance.Balance.get(account_type=account_type)
            print(balance)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {"account_type": xendit.BalanceAccountType.CASH}
        print_running_function("xendit.Balance.AccountType", args)
        GetBalance.run(xendit_instance, **args)


def ask_balance_input():
    print("Input the action that you want to use")
    print("0. Exit")
    print("1. Get Balance")
    try:
        return int(input())
    except ValueError:
        print("Invalid input. Please type a number")
        return ask_balance_input()


def balance_example(xendit_instance):
    balance_input = ask_balance_input()
    while balance_input != 0:
        if balance_input == 1:
            print("Running example of Get Balance")
            GetBalance.example(xendit_instance)
        balance_input = ask_balance_input()
