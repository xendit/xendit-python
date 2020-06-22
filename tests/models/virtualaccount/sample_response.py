def virtual_account_response():
    return {
        "owner_id": "5ed75086a883856178afc12e",
        "external_id": "demo_1475459775872",
        "bank_code": "BNI",
        "merchant_code": "8808",
        "name": "Rika Sutanto",
        "account_number": "8808999938311321",
        "is_single_use": False,
        "status": "PENDING",
        "expiration_date": "2051-06-18T17:00:00.000Z",
        "is_closed": False,
        "id": "5eec6cdc787210324084cff8",
    }


def virtual_account_banks_response():
    return [
        {"name": "Bank Mandiri", "code": "MANDIRI"},
        {"name": "Bank Negara Indonesia", "code": "BNI"},
        {"name": "Bank Rakyat Indonesia", "code": "BRI"},
        {"name": "Bank Permata", "code": "PERMATA"},
        {"name": "Bank Central Asia", "code": "BCA"},
    ]


def virtual_account_payment_response():
    return {
        "id": "598d91b1191029596846047f",
        "payment_id": "1502450097080",
        "callback_virtual_account_id": "598d5f71bf64853820c49a18",
        "external_id": "demo-1502437214715",
        "merchant_code": "77517",
        "account_number": "1000016980",
        "bank_code": "BNI",
        "amount": 5000,
        "sender_name": "JOHN DOE",
        "transaction_timestamp": "2017-08-11T11:14:57.080Z",
    }
