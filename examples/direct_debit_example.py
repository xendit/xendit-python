from print_running_function import print_running_function

import time

# Hackish method to import from another directory
# Useful while xendit-python isn't released yet to the public
import importlib.machinery

loader = importlib.machinery.SourceFileLoader("xendit", "../xendit/__init__.py")
xendit = loader.load_module("xendit")


class CreateCustomer:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            customer = xendit_instance.DirectDebit.create_customer(**kwargs)
            print(customer)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "reference_id": f"merc-{int(time.time())}",
            "email": "t@x.co",
            "given_names": "Adyaksa",
        }
        print_running_function("xendit.DirectDebit.create_customer", args)
        CreateCustomer.run(xendit_instance, **args)


class GetCustomerByRefID:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            customer = xendit_instance.DirectDebit.get_customer_by_ref_id(**kwargs)
            print(customer)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        reference_id = input("Please input your reference_id: ")
        args = {
            "reference_id": reference_id,
        }
        print_running_function("xendit.DirectDebit.get_customer_by_ref_id", args)
        GetCustomerByRefID.run(xendit_instance, **args)


class InitializeTokenization:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            customer = xendit_instance.DirectDebit.initialize_tokenization(**kwargs)
            print(customer)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "customer_id": "ed20b5db-df04-41fc-8018-8ea4ac4d1030",
            "channel_code": "DC_BRI",
            "properties": {
                "account_mobile_number": "+62818555988",
                "card_last_four": "8888",
                "card_expiry": "06/24",
                "account_email": "test.email@xendit.co",
            },
        }
        print_running_function("xendit.DirectDebit.initialize_tokenization", args)
        InitializeTokenization.run(xendit_instance, **args)


class ValidateTokenOTP:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            linked_account_token = xendit_instance.DirectDebit.validate_token_otp(
                **kwargs
            )
            print(linked_account_token)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        linked_account_token_id = input("Please input your linked_account_token_id: ")
        args = {
            "linked_account_token_id": linked_account_token_id,
            "otp_code": "333000",
        }
        print_running_function("xendit.DirectDebit.validate_token_otp", args)
        ValidateTokenOTP.run(xendit_instance, **args)


class GetAccessibleAccountsByToken:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            customer = xendit_instance.DirectDebit.get_accessible_accounts_by_token(
                **kwargs
            )
            print(customer)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        linked_account_token_id = input("Please input your linked_account_token_id: ")
        args = {
            "linked_account_token_id": linked_account_token_id,
        }
        print_running_function(
            "xendit.DirectDebit.get_accessible_account_by_token", args
        )
        GetAccessibleAccountsByToken.run(xendit_instance, **args)


class CreatePaymentMethod:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            customer = xendit_instance.DirectDebit.create_payment_method(**kwargs)
            print(customer)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        customer_id = input("Please input your customer_id: ")
        linked_account_token_id = input("Please input your linked_account_token_id: ")
        args = {
            "customer_id": customer_id,
            "type": xendit.DirectDebitPaymentMethodType.DEBIT_CARD,
            "properties": {"id": linked_account_token_id},
        }
        print_running_function("xendit.DirectDebit.create_payment_method", args)
        CreatePaymentMethod.run(xendit_instance, **args)


class GetPaymentMethodsByCustomerID:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            customer = xendit_instance.DirectDebit.get_payment_methods_by_customer_id(
                **kwargs
            )
            print(customer)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        customer_id = input("Please input your customer_id: ")
        args = {
            "customer_id": customer_id,
        }
        print_running_function(
            "xendit.DirectDebit.get_payment_methods_by_customer_id", args
        )
        GetPaymentMethodsByCustomerID.run(xendit_instance, **args)


class CreatePayment:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            payment = xendit_instance.DirectDebit.create_payment(**kwargs)
            print(payment)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        payment_method_id = input("Please input your payment_method_id: ")
        args = {
            "reference_id": f"direct-debit-ref-{int(time.time())}",
            "payment_method_id": payment_method_id,
            "currency": "IDR",
            "amount": "60000",
            "callback_url": "http://webhook.site/",
            "enable_otp": True,
            "idempotency_key": f"idemp_key-{int(time.time())}",
        }
        print_running_function("xendit.DirectDebit.create_payment", args)
        CreatePayment.run(xendit_instance, **args)


class ValidatePaymentOTP:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            payment = xendit_instance.DirectDebit.validate_payment_otp(**kwargs)
            print(payment)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        direct_debit_id = input("Please input your direct_debit_id: ")
        args = {
            "direct_debit_id": direct_debit_id,
            "otp_code": "222000",
        }
        print_running_function("xendit.DirectDebit.validate_payment_otp", args)
        ValidatePaymentOTP.run(xendit_instance, **args)


class GetPaymentStatus:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            payment = xendit_instance.DirectDebit.get_payment_status(**kwargs)
            print(payment)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        direct_debit_id = input("Please input your direct_debit_id: ")
        args = {
            "direct_debit_id": direct_debit_id,
        }
        print_running_function("xendit.DirectDebit.get_payment_status", args)
        GetPaymentStatus.run(xendit_instance, **args)


class GetPaymentStatusByRefID:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            payment = xendit_instance.DirectDebit.get_payment_status_by_ref_id(**kwargs)
            print(payment)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        reference_id = input("Please input your reference_id: ")
        args = {
            "reference_id": reference_id,
        }
        print_running_function("xendit.DirectDebit.get_payment_status_by_ref_id", args)
        GetPaymentStatusByRefID.run(xendit_instance, **args)


def ask_direct_debit_input():
    print("Input the action that you want to use")
    print("0. Exit")
    print("1. Create Customer")
    print("2. Get Customer by Reference ID")
    print("3. Initialize Linked Account Tokenization")
    print("4. Validate OTP for Linked Account Token")
    print("5. Retrieve Accessible Accounts by Linked Account Token")
    print("6. Create Payment Method")
    print("7. Get Payment Methods by Customer ID")
    print("8. Create Direct Debit Payment")
    print("9. Validate OTP for Direct Debit Payment")
    print("10. Get Direct Debit Payment Status by ID")
    print("11. Get Direct Debit Payment Status by Reference ID")
    try:
        return int(input())
    except ValueError:
        print("Invalid input. Please type a number")
        return ask_direct_debit_input()


def direct_debit_example(xendit_instance):
    direct_debit_input = ask_direct_debit_input()
    while direct_debit_input != 0:
        if direct_debit_input == 1:
            print("Running example of Create Customer")
            CreateCustomer.example(xendit_instance)
        elif direct_debit_input == 2:
            print("Running example of Get Customer by Reference ID")
            GetCustomerByRefID.example(xendit_instance)
        elif direct_debit_input == 3:
            print("Running example of Initialize Linked Account Tokenization")
            InitializeTokenization.example(xendit_instance)
        elif direct_debit_input == 4:
            print("Running example of Validate OTP for Linked Account Token")
            ValidateTokenOTP.example(xendit_instance)
        elif direct_debit_input == 5:
            print(
                "Running example of Retrieve Accessible Accounts by Linked Account Token"
            )
            GetAccessibleAccountsByToken.example(xendit_instance)
        elif direct_debit_input == 6:
            print("Running example of Create Payment Method")
            CreatePaymentMethod.example(xendit_instance)
        elif direct_debit_input == 7:
            print("Running example of Get Payment Methods by Customer ID")
            GetPaymentMethodsByCustomerID.example(xendit_instance)
        elif direct_debit_input == 8:
            print("Running example of Create Direct Debit Payment")
            CreatePayment.example(xendit_instance)
        elif direct_debit_input == 9:
            print("Running example of Validate OTP for Direct Debit Payment")
            ValidatePaymentOTP.example(xendit_instance)
        elif direct_debit_input == 10:
            print("Running example of Get Direct Debit Payment Status by ID")
            GetPaymentStatus.example(xendit_instance)
        elif direct_debit_input == 11:
            print("Running example of Get Direct Debit Payment Status by Reference ID")
            GetPaymentStatusByRefID.example(xendit_instance)
        direct_debit_input = ask_direct_debit_input()
