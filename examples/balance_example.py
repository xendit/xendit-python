# Hackish method to import from another directory
# Useful while xendit-python isn't released yet to the public
import importlib.machinery

loader = importlib.machinery.SourceFileLoader("xendit", "../xendit/__init__.py")
xendit = loader.load_module("xendit")


def get_balance(xendit_instance, params):
    try:
        print(xendit_instance.Balance.get(params))
    except xendit.XenditError as e:
        print("Error status code:", e.status_code)
        print("Error message:", e)
    except ValueError as e:
        print("Error message:", e)


def balance_example(xendit_instance):
    print("Running xendit.Balance.get(xendit.Balance.AccountType.CASH):")
    get_balance(xendit_instance, xendit.BalanceAccountType.CASH)

    print('Running xendit.Balance.get("cash"):')
    get_balance(xendit_instance, "cash")
