def customer_response():
    return {
        "id": "9d72e4bc-a178-4aff-9f63-f20b74532bac",
        "reference_id": "merc-1594272368",
        "description": None,
        "given_names": "Adyaksa",
        "middle_name": None,
        "surname": None,
        "mobile_number": None,
        "phone_number": None,
        "email": "t@x.co",
        "nationality": None,
        "addresses": None,
        "date_of_birth": None,
        "employment": None,
        "source_of_wealth": None,
        "metadata": None,
    }


def multi_customer_response():
    return [customer_response(), customer_response()]


def linked_account_response():
    return {
        "id": "lat-afcfde47-18e0-4d68-bf1b-c729a5d8e54a",
        "customer_id": "ed20b5db-df04-41fc-8018-8ea4ac4d1030",
        "channel_code": "DC_BRI",
        "status": "PENDING",
    }


def accessible_accounts_response():
    return [
        {
            "channel_code": "DC_BRI",
            "id": "la-aefbc050-4198-4e30-a925-4bbcf572f20d",
            "properties": {
                "card_expiry": "06/24",
                "card_last_four": "8888",
                "currency": "IDR",
                "description": "",
            },
            "type": "DEBIT_CARD",
        }
    ]


def payment_method_response():
    return {
        "customer_id": "ed20b5db-df04-41fc-8018-8ea4ac4d1030",
        "type": "DEBIT_CARD",
        "properties": {
            "id": "la-fac7e744-ab40-4100-a447-cbbb16f29ded",
            "currency": "IDR",
            "card_expiry": "06/24",
            "description": "",
            "channel_code": "DC_BRI",
            "card_last_four": "8888",
        },
        "status": "ACTIVE",
        "metadata": {},
        "id": "pm-b6116aea-8c23-42d0-a1e6-33227b52fccd",
        "created": "2020-07-13T07:28:57.716Z",
        "updated": "2020-07-13T07:28:57.716Z",
    }


def multi_payment_method_response():
    return [payment_method_response(), payment_method_response()]


def payment_response():
    return {
        "amount": 60000,
        "basket": None,
        "channel_code": "DC_BRI",
        "created": "2020-07-14T09:04:20.031451Z",
        "currency": "IDR",
        "description": "",
        "failure_code": None,
        "id": "ddpy-38ef50a8-00f0-4019-8b28-9bca81f2cbf1",
        "is_otp_required": False,
        "metadata": None,
        "otp_expiration_timestamp": None,
        "otp_mobile_number": None,
        "payment_method_id": "pm-b6116aea-8c23-42d0-a1e6-33227b52fccd",
        "reference_id": "direct-debit-ref-1594717458",
        "status": "PENDING",
        "updated": "2020-07-14T09:04:20.031451Z",
    }


def multi_payment_response():
    return [payment_response(), payment_response()]
