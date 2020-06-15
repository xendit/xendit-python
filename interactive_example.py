import xendit


def ask_input():
    print("Please type one of the number below")
    print("0. Exit")
    print("1. Balance")
    try:
        return int(input())
    except ValueError:
        print("Invalid input. Please type a number")
        return ask_input()


def balance_example():
    print('Running Balance example using "CASH" parameter:')
    print(xendit.Balance.get("CASH"))


if __name__ == "__main__":
    xendit.api_key = input("Please paste your SECRET KEY here: ")
    user_choice = ask_input()
    while user_choice != 0:
        if user_choice == 1:
            balance_example()
        else:
            print("Wrong input, please output number in range [0,1]")
        user_choice = ask_input()
