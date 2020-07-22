from balance_example import balance_example
from batch_disbursement_example import batch_disbursement_example
from credit_card_example import credit_card_example
from direct_debit_example import direct_debit_example
from disbursement_example import disbursement_example
from ewallet_example import ewallet_example
from invoice_example import invoice_example
from payout_example import payout_example
from qrcode_example import qrcode_example
from recurring_payment_example import recurring_payment_example
from retail_outlet_example import retail_outlet_example
from virtual_account_example import virtual_account_example

# Hackish method to import from another directory
# Useful while xendit-python isn't released yet to the public
import importlib.machinery

loader = importlib.machinery.SourceFileLoader("xendit", "../xendit/__init__.py")
xendit = loader.load_module("xendit")


def ask_input():
    print("Please type one of the number below")
    print("0. Exit")
    print("1. Balance")
    print("3. Credit Card")
    print("4. eWallet")
    print("6. QR Codes")
    print("7. Direct Debit")
    print("8. VirtualAccount")
    print("9. Retail Outlets")
    print("10. Invoice")
    print("11. Recurring Payment")
    print("12. Payout")
    print("13. Disbursement")
    print("14. Batch Disbursement")
    try:
        return int(input())
    except ValueError:
        print("Invalid input. Please type a number")
        return ask_input()


if __name__ == "__main__":
    api_key = input("Please paste your SECRET KEY here: ")
    xendit_instance = xendit.Xendit(api_key=api_key)
    user_choice = ask_input()
    while user_choice != 0:
        print()
        if user_choice == 1:
            balance_example(xendit_instance)
        elif user_choice == 3:
            credit_card_example(xendit_instance)
        elif user_choice == 4:
            ewallet_example(xendit_instance)
        elif user_choice == 6:
            qrcode_example(xendit_instance)
        elif user_choice == 7:
            direct_debit_example(xendit_instance)
        elif user_choice == 8:
            virtual_account_example(xendit_instance)
        elif user_choice == 9:
            retail_outlet_example(xendit_instance)
        elif user_choice == 10:
            invoice_example(xendit_instance)
        elif user_choice == 11:
            recurring_payment_example(xendit_instance)
        elif user_choice == 12:
            payout_example(xendit_instance)
        elif user_choice == 13:
            disbursement_example(xendit_instance)
        elif user_choice == 14:
            batch_disbursement_example(xendit_instance)
        else:
            print("Wrong input, please output number in range [0,1]")
        print()
        user_choice = ask_input()
