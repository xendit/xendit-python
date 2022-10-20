import xendit

from xendit.models.paymentmethod import ewallet

from print_running_function import print_running_function


class CreatePaymentMethod:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            payment_method = xendit_instance.PaymentMethod.create(**kwargs)
            print(payment_method)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "type": "EWALLET",
            "reusability": "ONE_TIME_USE",
            "ewallet": ewallet.EWallet.Query(
                channel_code="PAYMAYA",
                channel_properties=ewallet.ChannelProperties.Query(
                    success_return_url="https://mock-test.co",
                    failure_return_url="https://mock-test.co",
                    cancel_return_url="https://mock-test.co",
                )
            )
        }
        print_running_function("xendit.PaymentMethod.create", args)
        CreatePaymentMethod.run(xendit_instance, **args)

class GetPaymentMethod:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            payment_method = xendit_instance.PaymentMethod.create(**kwargs)
            print(payment_method)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "type": "EWALLET",
            "reusability": "ONE_TIME_USE",
            "ewallet": ewallet.EWallet.Query(
                channel_code="PAYMAYA",
                channel_properties=ewallet.ChannelProperties.Query(
                    success_return_url="https://mock-test.co",
                    failure_return_url="https://mock-test.co",
                    cancel_return_url="https://mock-test.co",
                )
            )
        }
        print_running_function("xendit.PaymentMethod.create", args)
        CreatePaymentMethod.run(xendit_instance, **args)

def ask_payment_method_input():
    print("Input the action that you want to use")
    print("0. Exit")
    print("1. Create Payment Method")
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
            CreatePaymentMethod.example(xendit_instance)
        payment_method_input = ask_payment_method_input()
