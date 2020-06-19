# Hackish method to import from another directory
# Useful while xendit-python isn't released yet to the public
import importlib.machinery

loader = importlib.machinery.SourceFileLoader("xendit", "../xendit/__init__.py")
xendit = loader.load_module("xendit")


class GetBalance:
    @staticmethod
    def run(func, account_type):
        try:
            print(func(account_type))
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        print("Running xendit.Balance.get(xendit.Balance.AccountType.CASH):")
        GetBalance.run(xendit_instance.Balance.get, xendit.BalanceAccountType.CASH)

        print('Running xendit.Balance.get("cash"):')
        GetBalance.run(xendit_instance.Balance.get, "cash")


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
            print("Running example of Create Virtual Account")
            GetBalance.example(xendit_instance)
        balance_input = ask_balance_input()
