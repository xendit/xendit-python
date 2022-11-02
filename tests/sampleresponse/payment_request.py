def payment_request_response():
    return {
        "id": "ewc_93f9be97-67dc-47cf-8225-0bb18cb3dfb1",
        "reference_id": "ec0aeced-f9cc-407c-a7a7-f78653235185",
        "business_id": "1417479e238542429cb891f0",
        "currency": "PHP",
        "amount": 1500,
        "country": "PH",
        "payment_method": {
            "id": "pm-bdd34ca4-e75d-49a1-86fc-d24090c70f81",
            "type": "EWALLET",
            "reference_id": "57a8413b-75d1-4611-8585-5fdc33a02b34",
            "description": None,
            "created": "2022-10-21T02:03:37.569360552Z",
            "updated": "2022-10-21T02:03:37.569360552Z",
            "card": None,
            "ewallet": {
                "channel_code": "PAYMAYA",
                "channel_properties": {
                    "cancel_return_url": "https://redirect.me/nostuff",
                    "failure_return_url": "https://redirect.me/badstuff",
                    "success_return_url": "https://redirect.me/goodstuff"
                },
                "account": {
                    "name": None,
                    "account_details": None,
                    "balance": None,
                    "point_balance": None
                }
            },
            "direct_debit": None,
            "direct_bank_transfer": None,
            "over_the_counter": None,
            "virtual_account": None,
            "qr_code": None,
            "metadata": None,
            "reusability": "ONE_TIME_USE",
            "status": "ACTIVE"
        },
        "description": None,
        "metadata": None,
        "customer_id": None,
        "created": "2022-10-21T02:03:37.583670197Z",
        "updated": "2022-10-21T02:03:37.583670197Z",
        "status": "REQUIRES_ACTION",
        "actions": [
            {
                "action": "AUTH",
                "url": "https://mock-test.co",
                "url_type": "WEB",
                "method": "GET",
                "qr_code": None
            },
            {
                "action": "AUTH",
                "url": "https://mock-test.co",
                "url_type": "MOBILE",
                "method": "GET",
                "qr_code": None
            }
        ],
        "failure_code": None,
        "capture_method": "AUTOMATIC",
        "initiator": None,
        "card_verification_results": None,
        "channel_properties": None,
        "shipping_information": None,
        "items": None
    }
