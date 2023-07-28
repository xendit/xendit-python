import time

from print_running_function import print_running_function

import xendit


class CreateQRCode:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            qrcode = xendit_instance.QRCode.create(**kwargs)
            print(qrcode)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        args = {
            "external_id": f"qrcode-id-{int(time.time())}",
            "type": xendit.QRCodeType.DYNAMIC,
            "callback_url": "https://webhook.site",
            "amount": 4000,
        }
        print_running_function("xendit.QRCode.create", args)
        CreateQRCode.run(xendit_instance, **args)


class GetQRCodeByExtID:
    @staticmethod
    def run(xendit_instance, **kwargs):
        try:
            qrcode = xendit_instance.QRCode.get_by_ext_id(**kwargs,)
            print(qrcode)
        except xendit.XenditError as e:
            print("Error status code:", e.status_code)
            print("Error message:", e)

    @staticmethod
    def example(xendit_instance):
        external_id = input("Please input your external_id: ")
        args = {
            "external_id": external_id,
        }
        print_running_function("xendit.QRCode.get_by_ext_id", args)
        GetQRCodeByExtID.run(xendit_instance, **args)


def ask_qrcode_input():
    print("Input the action that you want to use")
    print("0. Exit")
    print("1. Create QR Code")
    print("2. Get QR Code by External ID")
    try:
        return int(input())
    except ValueError:
        print("Invalid input. Please type a number")
        return ask_qrcode_input()


def qrcode_example(xendit_instance):
    qrcode_input = ask_qrcode_input()
    while qrcode_input != 0:
        if qrcode_input == 1:
            print("Running example of Create QR Code")
            CreateQRCode.example(xendit_instance)
        elif qrcode_input == 2:
            print("Running example of Get QR Code by External ID")
            GetQRCodeByExtID.example(xendit_instance)
        qrcode_input = ask_qrcode_input()
