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
    return {}
