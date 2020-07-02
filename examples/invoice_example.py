from print_running_function import print_running_function

import time

# Hackish method to import from another directory
# Useful while xendit-python isn't released yet to the public
import importlib.machinery

loader = importlib.machinery.SourceFileLoader("xendit", "../xendit/__init__.py")
xendit = loader.load_module("xendit")


class CreateInvoice:
    @staticmethod
    def run(xendit_instance, external_id, amount, payer_email, description, **kwargs):
        try:
            invoice = xendit_instance.Invoice.create(
                external_id=external_id,
                amount=amount,
                payer_email=payer_email,
                description=description,
                **kwargs,
            )
            print(invoice)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "external_id": f"invoice-{int(time.time())}",
            "amount": 20000,
            "payer_email": "customer@domain.com",
            "description": "Invoice Demo #123",
        }
        print_running_function("xendit.Invoice.create", args)
        CreateInvoice.run(xendit_instance, **args)


class GetInvoice:
    pass


class ExpireInvoice:
    pass


class ListAllInvoice:
    pass


def ask_invoice_input():
    print("Input the action that you want to use")
    print("0. Exit")
    print("1. Create Invoice")
    print("2. Get Invoice")
    print("3. Expire Invoice")
    print("4. List All Invoice")
    try:
        return int(input())
    except ValueError:
        print("Invalid input. Please type a number")
        return ask_invoice_input()


def invoice_example(xendit_instance):
    invoice_input = ask_invoice_input()
    while invoice_input != 0:
        if invoice_input == 1:
            print("Running example of Create Invoice")
            CreateInvoice.example(xendit_instance)
        elif invoice_input == 2:
            print("Running example of Get Invoice")
            GetInvoice.example(xendit_instance)
        elif invoice_input == 3:
            print("Running example of Expire Invoice")
            ExpireInvoice.example(xendit_instance)
        elif invoice_input == 4:
            print("Running example of List All Invoice")
            ListAllInvoice.example(xendit_instance)
        invoice_input = ask_invoice_input()
