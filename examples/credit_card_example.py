from print_running_function import print_running_function
import time

import xendit


class CreateAuthorization:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            charge = xendit_instance.CreditCard.create_authorization(**kwargs)
            print(charge)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        token_id = input("Please input your token_id: ")
        args = {
            "token_id": token_id,
            "external_id": f"card_preAuth-{int(time.time())}",
            "amount": 75000,
            "card_cvn": "123",
        }
        print_running_function("xendit.CreditCard.create_authorization", args)
        CreateAuthorization.run(xendit_instance, **args)


class ReverseAuthorization:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            reverse_authorization = xendit_instance.CreditCard.reverse_authorization(
                **kwargs
            )
            print(reverse_authorization)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        credit_card_charge_id = input("Please input your credit_card_charge_id: ")
        args = {
            "credit_card_charge_id": credit_card_charge_id,
            "external_id": f"reverse-authorization-{int(time.time())}",
        }
        print_running_function("xendit.CreditCard.reverse_authorizatiton", args)
        ReverseAuthorization.run(xendit_instance, **args)


class CreateCharge:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            charge = xendit_instance.CreditCard.create_charge(**kwargs)
            print(charge)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        token_id = input("Please input your token_id: ")
        args = {
            "token_id": token_id,
            "external_id": f"card_charge-{int(time.time())}",
            "amount": 75000,
            "card_cvn": "123",
        }
        print_running_function("xendit.CreditCard.create_charge", args)
        CreateCharge.run(xendit_instance, **args)


class CaptureCharge:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            charge = xendit_instance.CreditCard.capture_charge(**kwargs)
            print(charge)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        credit_card_charge_id = input("Please input your credit_card_charge_id: ")
        args = {
            "credit_card_charge_id": credit_card_charge_id,
            "amount": 75000,
        }
        print_running_function("xendit.CreditCard.capture_charge", args)
        CaptureCharge.run(xendit_instance, **args)


class GetCharge:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            charge = xendit_instance.CreditCard.get_charge(**kwargs)
            print(charge)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        credit_card_charge_id = input("Please input your credit_card_charge_id: ")
        args = {
            "credit_card_charge_id": credit_card_charge_id,
        }
        print_running_function("xendit.CreditCard.get_charge", args)
        GetCharge.run(xendit_instance, **args)


class CreateRefund:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            refund = xendit_instance.CreditCard.create_refund(**kwargs)
            print(refund)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        credit_card_charge_id = input("Please input your credit_card_charge_id: ")
        args = {
            "credit_card_charge_id": credit_card_charge_id,
            "amount": 10000,
            "external_id": f"card_refund-{int(time.time())}",
        }
        print_running_function("xendit.CreditCard.create_refund", args)
        CreateRefund.run(xendit_instance, **args)


class CreatePromotion:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            credit_card = xendit_instance.CreditCard.create_promotion(**kwargs)
            print(credit_card)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "reference_id": f"BRI_20_JAN-{int(time.time())}",
            "description": "20% discount applied for all BRI cards",
            "discount_amount": 10000,
            "bin_list": ["400000", "460000"],
            "start_time": "2020-01-01T00:00:00.000Z",
            "end_time": "2021-01-01T00:00:00.000Z",
        }
        print_running_function("xendit.CreditCard.create_promotion", args)
        CreatePromotion.run(xendit_instance, **args)


def ask_credit_card_input():
    print("Input the action that you want to use")
    print("0. Exit")
    print("1. Create Authorization")
    print("2. Reverse Authorization")
    print("3. Create Charge")
    print("4. Capture Charge")
    print("5. Get Charge")
    print("6. Create Refund")
    print("7. Create Promotion")
    try:
        return int(input())
    except ValueError:
        print("Invalid input. Please type a number")
        return ask_credit_card_input()


def credit_card_example(xendit_instance):
    credit_card_input = ask_credit_card_input()
    while credit_card_input != 0:
        if credit_card_input == 1:
            print("Running example of Create Authorization")
            CreateAuthorization.example(xendit_instance)
        elif credit_card_input == 2:
            print("Running example of Reverse Authorization")
            ReverseAuthorization.example(xendit_instance)
        elif credit_card_input == 3:
            print("Running example of Create Charge")
            CreateCharge.example(xendit_instance)
        elif credit_card_input == 4:
            print("Running example of Capture Charge")
            CaptureCharge.example(xendit_instance)
        elif credit_card_input == 5:
            print("Running example of Get Charge")
            GetCharge.example(xendit_instance)
        elif credit_card_input == 6:
            print("Running example of Create Refund")
            CreateRefund.example(xendit_instance)
        elif credit_card_input == 7:
            print("Running example of Create Promotion")
            CreatePromotion.example(xendit_instance)
        credit_card_input = ask_credit_card_input()
