from print_running_function import print_running_function

# Hackish method to import from another directory
# Useful while xendit-python isn't released yet to the public
import importlib.machinery

loader = importlib.machinery.SourceFileLoader("xendit", "../xendit/__init__.py")
xendit = loader.load_module("xendit")


class CreateRecurringPayment:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            recurring_payment = xendit_instance.RecurringPayment.create(**kwargs)
            print(recurring_payment)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "external_id": "recurring_12345",
            "payer_email": "test@x.co",
            "description": "Test Curring Payment",
            "amount": 100000,
            "interval": "MONTH",
            "interval_count": 1,
        }
        print_running_function("xendit.RecurringPayment.create", args)
        CreateRecurringPayment.run(xendit_instance, **args)


class GetRecurringPayment:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            recurring_payment = xendit_instance.RecurringPayment.get(**kwargs)
            print(recurring_payment)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        id = input("Please input your id: ")
        args = {
            "id": id,
        }
        print_running_function("xendit.RecurringPayment.get", args)
        GetRecurringPayment.run(xendit_instance, **args)


class EditRecurringPayment:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            recurring_payment = xendit_instance.RecurringPayment.edit(**kwargs)
            print(recurring_payment)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        id = input("Please input your id: ")
        args = {
            "id": id,
            "interval_count": 2,
        }
        print_running_function("xendit.RecurringPayment.edit", args)
        EditRecurringPayment.run(xendit_instance, **args)


class StopRecurringPayment:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            recurring_payment = xendit_instance.RecurringPayment.stop(**kwargs)
            print(recurring_payment)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        id = input("Please input your id: ")
        args = {
            "id": id,
        }
        print_running_function("xendit.RecurringPayment.stop", args)
        StopRecurringPayment.run(xendit_instance, **args)


class PauseRecurringPayment:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            recurring_payment = xendit_instance.RecurringPayment.pause(**kwargs)
            print(recurring_payment)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        id = input("Please input your id: ")
        args = {
            "id": id,
        }
        print_running_function("xendit.RecurringPayment.pause", args)
        PauseRecurringPayment.run(xendit_instance, **args)


class ResumeRecurringPayment:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            recurring_payment = xendit_instance.RecurringPayment.resume(**kwargs)
            print(recurring_payment)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        id = input("Please input your id: ")
        args = {
            "id": id,
        }
        print_running_function("xendit.RecurringPayment.resume", args)
        ResumeRecurringPayment.run(xendit_instance, **args)


def ask_recurring_payment_input():
    print("Input the action that you want to use")
    print("0. Exit")
    print("1. Create Recurring Payment")
    print("2. Get Recurring Payment")
    print("3. Edit Recurring Payment")
    print("4. Stop Recurring Payment")
    print("5. Pause Recurring Payment")
    print("6. Resume Recurring Payment")
    try:
        return int(input())
    except ValueError:
        print("Invalid input. Please type a number")
        return ask_recurring_payment_input()


def recurring_payment_example(xendit_instance):
    recurring_payment_input = ask_recurring_payment_input()
    while recurring_payment_input != 0:
        if recurring_payment_input == 1:
            print("Running example of Create Recurring Payment")
            CreateRecurringPayment.example(xendit_instance)
        elif recurring_payment_input == 2:
            print("Running example of Get Recurring Payment")
            GetRecurringPayment.example(xendit_instance)
        elif recurring_payment_input == 3:
            print("Running example of Edit Recurring Payment")
            EditRecurringPayment.example(xendit_instance)
        elif recurring_payment_input == 4:
            print("Running example of Stop Recurring Payment")
            StopRecurringPayment.example(xendit_instance)
        elif recurring_payment_input == 5:
            print("Running example of Pause Recurring Payment")
            PauseRecurringPayment.example(xendit_instance)
        elif recurring_payment_input == 6:
            print("Running example of Resume Recurring Payment")
            ResumeRecurringPayment.example(xendit_instance)
        recurring_payment_input = ask_recurring_payment_input()
