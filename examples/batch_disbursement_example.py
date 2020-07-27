import time

from print_running_function import print_running_function

# Hackish method to import from another directory
# Useful while xendit-python isn't released yet to the public
import importlib.machinery

loader = importlib.machinery.SourceFileLoader("xendit", "../xendit/__init__.py")
xendit = loader.load_module("xendit")


class CreateBatchDisbursement:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            batch_disbursement = xendit_instance.BatchDisbursement.create(**kwargs)
            print(batch_disbursement)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        batch_disbursement_items = []
        batch_disbursement_items.append(
            {
                "amount": 10000,
                "bank_code": "BCA",
                "bank_account_name": "Adyaksa W",
                "bank_account_number": "12345678",
                "description": "Sample Batch Disbursement",
                "external_id": f"batch-disbursement-item-{int(time.time())}",
            }
        )
        args = {
            "reference": f"batch_disbursement-{int(time.time())}",
            "disbursements": batch_disbursement_items,
        }
        print_running_function("xendit.BatchDisbursement.create", args)
        CreateBatchDisbursement.run(xendit_instance, **args)


def ask_batch_disbursement_input():
    print("Input the action that you want to use")
    print("0. Exit")
    print("1. Create Batch Disbursement")
    try:
        return int(input())
    except ValueError:
        print("Invalid input. Please type a number")
        return ask_batch_disbursement_input()


def batch_disbursement_example(xendit_instance):
    batch_disbursement_input = ask_batch_disbursement_input()
    while batch_disbursement_input != 0:
        if batch_disbursement_input == 1:
            print("Running example of Create Batch Disbursement")
            CreateBatchDisbursement.example(xendit_instance)
        batch_disbursement_input = ask_batch_disbursement_input()
