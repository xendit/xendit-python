import xendit
from xendit import XenditError


def ask_input():
    print("Please type one of the number below")
    print("0. Exit")
    print("1. Balance")
    try:
        return int(input())
    except ValueError:
        print("Invalid input. Please type a number")
        return ask_input()


def get_balance(params):
    try:
        print(xendit.Balance.get(params))
    except XenditError as e:
        print("Error status code:", e.status_code)
        print("Error message:", e)


def balance_example():
    print('Running Balance example using "CASH" parameter:')
    get_balance("CASH")

    print('Running Balance example using "money" parameter:')
    get_balance("money")


if __name__ == "__main__":
    xendit.api_key = input("Please paste your SECRET KEY here: ")
    user_choice = ask_input()
    while user_choice != 0:
        print()
        if user_choice == 1:
            balance_example()
        else:
            print("Wrong input, please output number in range [0,1]")
        print()
        user_choice = ask_input()
