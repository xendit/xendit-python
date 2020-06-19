# Hackish method to import from another directory
# Useful while xendit-python isn't released yet to the public
import importlib.machinery

loader = importlib.machinery.SourceFileLoader("xendit", "../xendit/__init__.py")
xendit = loader.load_module("xendit")


def create_virtual_account(func, external_id, bank_code, name):
    try:
        print(func(external_id, bank_code, name))
    except xendit.XenditError as e:
        print("Error status code:", e.status_code)
        print("Error message:", e)


def create_virtual_account_example(xendit_instance):
    print(
        'Running xendit.VirtualAccount.create("demo_1475459775872", "BNI", "Rika Sutanto"):'
    )
    create_virtual_account(
        xendit_instance.VirtualAccount.create,
        "demo_1475459775872",
        "BNI",
        "Rika Sutanto",
    )

    print(
        'Running xendit.VirtualAccount.create("demo_1475459775872", "CIB", "Rika Sutanto"):'
    )
    create_virtual_account(
        xendit_instance.VirtualAccount.create,
        "demo_1475459775872",
        "CIB",
        "Rika Sutanto",
    )


def virtual_account_example(xendit_instance):
    create_virtual_account_example(xendit_instance)
