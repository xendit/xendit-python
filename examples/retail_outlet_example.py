from print_running_function import print_running_function

import xendit


class CreateFixedPaymentCode:
    @staticmethod
    def run(
        xendit_instance,
        external_id,
        retail_outlet_name,
        name,
        expected_amount,
        **kwargs,
    ):
        try:
            retail_outlet = xendit_instance.RetailOutlet.create_fixed_payment_code(
                external_id=external_id,
                retail_outlet_name=retail_outlet_name,
                name=name,
                expected_amount=expected_amount,
            )
            print(retail_outlet)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "external_id": "demo_fixed_payment_code_123",
            "retail_outlet_name": "ALFAMART",
            "name": "Rika Sutanto",
            "expected_amount": 10000,
        }
        print_running_function("xendit.RetailOutlet.create_fixed_payment_code", args)
        CreateFixedPaymentCode.run(xendit_instance, **args)


class UpdateFixedPaymentCode:
    @staticmethod
    def run(xendit_instance, fixed_payment_code_id, **kwargs):
        try:
            retail_outlet = xendit_instance.RetailOutlet.update_fixed_payment_code(
                fixed_payment_code_id=fixed_payment_code_id, **kwargs
            )
            print(retail_outlet)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "fixed_payment_code_id": "5ef2f0f8e7f5c14077275493",
            "name": "Joe Contini",
        }
        print_running_function("xendit.RetailOutlet.update_fixed_payment_code", args)
        UpdateFixedPaymentCode.run(xendit_instance, **args)


class GetFixedPaymentCode:
    @staticmethod
    def run(xendit_instance, fixed_payment_code_id, **kwargs):
        try:
            retail_outlet = xendit_instance.RetailOutlet.get_fixed_payment_code(
                fixed_payment_code_id=fixed_payment_code_id, **kwargs,
            )
            print(retail_outlet)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "fixed_payment_code_id": "5ef2f0f8e7f5c14077275493",
        }
        print_running_function("xendit.RetailOutlet.get_fixed_payment_code", args)
        GetFixedPaymentCode.run(xendit_instance, **args)


def ask_retail_outlet_input():
    print("Input the action that you want to use")
    print("0. Exit")
    print("1. Create Fixed Payment Code")
    print("2. Update Fixed Payment Code")
    print("3. Get Fixed Payment Code")
    try:
        return int(input())
    except ValueError:
        print("Invalid input. Please type a number")
        return ask_retail_outlet_input()


def retail_outlet_example(xendit_instance):
    retail_outlet_input = ask_retail_outlet_input()
    while retail_outlet_input != 0:
        if retail_outlet_input == 1:
            print("Running example of Create Fixed Payment Code")
            CreateFixedPaymentCode.example(xendit_instance)
        elif retail_outlet_input == 2:
            print("Running example of Update Fixed Payment Code")
            UpdateFixedPaymentCode.example(xendit_instance)
        elif retail_outlet_input == 3:
            print("Running example of Get Fixed Payment Code")
            GetFixedPaymentCode.example(xendit_instance)
        retail_outlet_input = ask_retail_outlet_input()
