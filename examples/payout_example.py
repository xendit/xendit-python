import time

from print_running_function import print_running_function

import xendit


class CreatePayout:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            payout = xendit_instance.Payout.create(**kwargs)
            print(payout)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "external_id": f"payout-{int(time.time())}",
            "amount": 50000,
            "email": "test@email.co",
        }
        print_running_function("xendit.Payout.create", args)
        CreatePayout.run(xendit_instance, **args)


class GetPayout:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            payout = xendit_instance.Payout.get(**kwargs)
            print(payout)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        id = input("Please input your id: ")
        args = {
            "id": id,
        }
        print_running_function("xendit.Payout.get", args)
        GetPayout.run(xendit_instance, **args)


class VoidPayout:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            payout = xendit_instance.Payout.void(**kwargs)
            print(payout)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        id = input("Please input your id: ")
        args = {
            "id": id,
        }
        print_running_function("xendit.Payout.void", args)
        VoidPayout.run(xendit_instance, **args)


def ask_payout_input():
    print("Input the action that you want to use")
    print("0. Exit")
    print("1. Create Payout")
    print("2. Get Payout")
    print("3. Void a Payout")
    try:
        return int(input())
    except ValueError:
        print("Invalid input. Please type a number")
        return ask_payout_input()


def payout_example(xendit_instance):
    payout_input = ask_payout_input()
    while payout_input != 0:
        if payout_input == 1:
            print("Running example of Create Payout")
            CreatePayout.example(xendit_instance)
        elif payout_input == 2:
            print("Running example of Get Payout")
            GetPayout.example(xendit_instance)
        elif payout_input == 3:
            print("Running example of Void a Payout")
            VoidPayout.example(xendit_instance)
        payout_input = ask_payout_input()
