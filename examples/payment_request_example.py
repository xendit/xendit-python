import xendit

from xendit.models import ewallet, PaymentMethod

from print_running_function import print_running_function


class CreatePaymentRequest:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            payment_request = xendit_instance.PaymentRequest.create(**kwargs)
            print(payment_request)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "amount": 1500,
            "currency": "IDR",
            "payment_method": PaymentMethod.Query(
                type="EWALLET",
                reusability="ONE_TIME_USE",
                ewallet=ewallet.EWallet.Query(
                    channel_code="OVO",
                    channel_properties=ewallet.ChannelProperties.Query(
                        mobile_number="+628123123123"
                    ),
                ),
            ),
        }
        print_running_function("xendit.PaymentRequest.create", args)
        CreatePaymentRequest.run(xendit_instance, **args)


def ask_payment_method_input():
    print("Input the action that you want to use")
    print("0. Exit")
    print("1. Create Payment Request")
    try:
        return int(input())
    except ValueError:
        print("Invalid input. Please type a number")
        return ask_payment_method_input()


def payment_method_example(xendit_instance):
    payment_method_input = ask_payment_method_input()
    while payment_method_input != 0:
        if payment_method_input == 1:
            print("Running example of Create Payment Method")
            CreatePaymentRequest.example(xendit_instance)
        payment_method_input = ask_payment_method_input()
