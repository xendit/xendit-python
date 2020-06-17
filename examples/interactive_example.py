# Hackish method to import from another directory
# Useful while xendit-python isn't released yet to the public
import importlib.machinery

loader = importlib.machinery.SourceFileLoader("xendit", "../xendit/__init__.py")
xendit = loader.load_module("xendit")


def ask_input():
    print("Please type one of the number below")
    print("0. Exit")
    print("1. Balance")
    try:
        return int(input())
    except ValueError:
        print("Invalid input. Please type a number")
        return ask_input()


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
    get_balance(xendit_instance, xendit.Balance.AccountType.CASH)

    print('Running xendit.Balance.get("cash"):')
    get_balance(xendit_instance, "cash")


if __name__ == "__main__":
    api_key = input("Please paste your SECRET KEY here: ")
    xendit_instance = xendit.Xendit(api_key=api_key)
    user_choice = ask_input()
    while user_choice != 0:
        print()
        if user_choice == 1:
            balance_example(xendit_instance)
        else:
            print("Wrong input, please output number in range [0,1]")
        print()
        user_choice = ask_input()
