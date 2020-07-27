import time

from print_running_function import print_running_function

# Hackish method to import from another directory
# Useful while xendit-python isn't released yet to the public
import importlib.machinery

loader = importlib.machinery.SourceFileLoader("xendit", "../xendit/__init__.py")
xendit = loader.load_module("xendit")


class CreateCardlessCreditPayment:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            cardless_credit_payment = xendit_instance.CardlessCredit.create_payment(
                **kwargs
            )
            print(cardless_credit_payment)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        cardless_credit_items = []
        cardless_credit_items.append(
            {
                "id": "item-123",
                "name": "Phone Case",
                "price": 200000,
                "type": "Smartphone",
                "url": "http://example.com/phone/phone_case",
                "quantity": 2,
            }
        )
        customer_details = {
            "first_name": "customer first name",
            "last_name": "customer last name",
            "email": "customer@email.com",
            "phone": "0812332145",
        }
        shipping_address = {
            "first_name": "first name",
            "last_name": "last name",
            "address": "Jl Teknologi No. 12",
            "city": "Jakarta",
            "postal_code": "12345",
            "phone": "081513114262",
            "country_code": "IDN",
        }
        args = {
            "cardless_credit_type": xendit.CardlessCreditType.KREDIVO,
            "external_id": f"id-{int(time.time())}",
            "amount": 10000,
            "payment_type": "3_months",
            "items": cardless_credit_items,
            "customer_details": customer_details,
            "shipping_address": shipping_address,
            "redirect_url": "https://my-shop.com/home",
            "callback_url": "https://my-shop.com/callback",
        }
        print_running_function("xendit.CardlessCredit.create_payment", args)
        CreateCardlessCreditPayment.run(xendit_instance, **args)


class CalculatePaymentType:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            cardless_credit_payment_types = xendit_instance.CardlessCredit.calculate_payment_type(
                **kwargs
            )
            print(cardless_credit_payment_types)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        cardless_credit_items = []
        cardless_credit_items.append(
            {
                "id": "item-123",
                "name": "Phone Case",
                "price": 200000,
                "type": "Smartphone",
                "url": "http://example.com/phone/phone_case",
                "quantity": 2,
            }
        )
        args = {
            "cardless_credit_type": xendit.CardlessCreditType.KREDIVO,
            "amount": 10000,
            "items": cardless_credit_items,
        }
        print_running_function("xendit.CardlessCredit.calculate_payment_type", args)
        CalculatePaymentType.run(xendit_instance, **args)


def ask_cardless_credit_input():
    print("Input the action that you want to use")
    print("0. Exit")
    print("1. Create Payment / Generate Checkout URL")
    print("2. Calculate Payment Types")
    try:
        return int(input())
    except ValueError:
        print("Invalid input. Please type a number")
        return ask_cardless_credit_input()


def cardless_credit_example(xendit_instance):
    cardless_credit_input = ask_cardless_credit_input()
    while cardless_credit_input != 0:
        if cardless_credit_input == 1:
            print("Running example of Create Payment / Generate Checkout URL")
            CreateCardlessCreditPayment.example(xendit_instance)
        elif cardless_credit_input == 2:
            print("Running example of Calculate Payment Types")
            CalculatePaymentType.example(xendit_instance)
        cardless_credit_input = ask_cardless_credit_input()
