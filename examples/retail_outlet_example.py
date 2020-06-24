# Hackish method to import from another directory
# Useful while xendit-python isn't released yet to the public
import importlib.machinery

loader = importlib.machinery.SourceFileLoader("xendit", "../xendit/__init__.py")
xendit = loader.load_module("xendit")


class CreateFixedPaymentCode:
    @staticmethod
    def run(
        xendit_instance,
        external_id,
        retail_outlet_name,
        name,
        expected_amount,
        **kwargs
    ):
        try:
            retail_outlet = xendit_instance.RetailOutlet.create_fixed_payment_code(
                external_id, retail_outlet_name, name, expected_amount,
            )
            print(retail_outlet)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        print(
            'Running xendit.RetailOutlet.create_fixed_payment_code("demo_fixed_payment_code_123", "ALFAMART", "Rika Sutanto", 10000):'
        )
        CreateFixedPaymentCode.run(
            xendit_instance,
            "demo_fixed_payment_code_123",
            "ALFAMART",
            "Rika Sutanto",
            10000,
        )


class UpdateFixedPaymentCode:
    @staticmethod
    def run(xendit_instance, fixed_payment_code_id, **kwargs):
        try:
            retail_outlet = xendit_instance.RetailOutlet.update_fixed_payment_code(
                fixed_payment_code_id, **kwargs
            )
            print(retail_outlet)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        print(
            'Running xendit.RetailOutlet.update_fixed_payment_code("5ef2f0f8e7f5c14077275493", name="Joe Contini"):'
        )
        UpdateFixedPaymentCode.run(
            xendit_instance, "5ef2f0f8e7f5c14077275493", name="Joe Contini"
        )


class GetFixedPaymentCode:
    @staticmethod
    def run(xendit_instance, fixed_payment_code_id, **kwargs):
        try:
            retail_outlet = xendit_instance.RetailOutlet.get_fixed_payment_code(
                fixed_payment_code_id, **kwargs
            )
            print(retail_outlet)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        print(
            'Running xendit.RetailOutlet.get_fixed_payment_code("5ef2f0f8e7f5c14077275493"):'
        )
        GetFixedPaymentCode.run(xendit_instance, "5ef2f0f8e7f5c14077275493")


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
