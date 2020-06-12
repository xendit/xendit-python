import xendit


def ask_input():
    print("Please output one of the number below")
    print("0. Exit")
    print("1. Balance")
    return input()


def balance_example():
    print('Running Balance example using "CASH" parameter:')
    print(xendit.Balance.get("CASH"))


if __name__ == "__main__":
    xendit.api_key = input("Please paste your SECRET KEY here: ")
    user_choice = int(ask_input())
    while user_choice != 0:
        print(user_choice)
        if user_choice == 1:
            balance_example()
        else:
            print("Wrong input, please output number in range [0,1]")
        ask_input()
