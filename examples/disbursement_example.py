# Hackish method to import from another directory
# Useful while xendit-python isn't released yet to the public
import importlib.machinery

loader = importlib.machinery.SourceFileLoader("xendit", "../xendit/__init__.py")
xendit = loader.load_module("xendit")


class CreateDisbursement:
    @staticmethod
    def run(
        xendit_instance,
        external_id,
        bank_code,
        account_holder_name,
        account_number,
        description,
        amount,
        **kwargs
    ):
        try:
            disbursement = xendit_instance.Disbursement.create(
                external_id,
                bank_code,
                account_holder_name,
                account_number,
                description,
                amount,
                **kwargs
            )
            print(disbursement)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        print(
            'Running xendit.Disbursement.create("demo_1475459775872", "BCA", "Bob Jones", "1231242311", "Reimbursement for shoes", 17000):'
        )
        CreateDisbursement.run(
            xendit_instance,
            external_id="demo_1475459775872",
            bank_code="BCA",
            account_holder_name="Bob Jones",
            account_number="1231242311",
            description="Reimbursement for shoes",
            amount=17000,
        )


class GetDisbursementByID:
    @staticmethod
    def run(xendit_instance, id, **kwargs):
        try:
            disbursement = xendit_instance.Disbursement.get(id, **kwargs)
            print(disbursement)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        print('Running xendit.Disbursement.get("5ef1befeecb16100179e1d05"):')
        GetDisbursementByID.run(xendit_instance, "5ef1befeecb16100179e1d05")


class GetDisbursementByExternalID:
    @staticmethod
    def run(xendit_instance, external_id, **kwargs):
        try:
            disbursement = xendit_instance.Disbursement.get_by_ext_id(
                external_id, **kwargs
            )
            print(disbursement)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        print('Running xendit.Disbursement.get_by_ext_id("demo_1475459775872"):')
        GetDisbursementByExternalID.run(xendit_instance, "demo_1475459775872")


class GetDisbursementBanks:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            disbursement_banks = xendit_instance.Disbursement.get_available_banks(
                **kwargs
            )
            print(disbursement_banks)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        print("Running xendit.Disbursement.get_available_banks():")
        GetDisbursementBanks.run(xendit_instance)


def ask_disbursement_input():
    print("Input the action that you want to use")
    print("0. Exit")
    print("1. Create Disbursement")
    print("2. Get Disbursement by ID")
    print("3. Get Disbursement by External ID")
    print("4. Get Available Banks")
    try:
        return int(input())
    except ValueError:
        print("Invalid input. Please type a number")
        return ask_disbursement_input()


def disbursement_example(xendit_instance):
    disbursement_input = ask_disbursement_input()
    while disbursement_input != 0:
        if disbursement_input == 1:
            print("Running example of Create Disbursement")
            CreateDisbursement.example(xendit_instance)
        elif disbursement_input == 2:
            print("Running example of Get Disbursement by ID")
            GetDisbursementByID.example(xendit_instance)
        elif disbursement_input == 3:
            print("Running example of Get Disbursement by External ID")
            GetDisbursementByExternalID.example(xendit_instance)
        elif disbursement_input == 4:
            print("Running example of Get Available Banks")
            GetDisbursementBanks.example(xendit_instance)
        disbursement_input = ask_disbursement_input()
