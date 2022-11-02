def payment_method_list_response():
    return {
        "has_more": True,
        "data": [{
            "id": "pm-1c229762-c21a-433d-8da5-f02240387e34",
            "type": "EWALLET",
            "country": "PH",
            "business_id": "5ed75086a883856178afc12e",
            "customer_id": None,
            "reference_id": "0724a49f-388f-41d9-9662-7aefad85a02b",
            "reusability": "ONE_TIME_USE",
            "status": "ACTIVE",
            "actions": [],
            "description": None,
            "created": "2022-10-18T01:31:45.843043772Z",
            "updated": "2022-10-18T01:31:45.843043772Z",
            "metadata": {},
            "billing_information": None,
            "failure_code": None,
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
            "direct_bank_transfer": None,
            "direct_debit": None,
            "card": None,
            "over_the_counter": None,
            "qr_code": None,
            "virtual_account": None
        }]
    }

def payment_method_response():
    return {
        "id": "pm-1c229762-c21a-433d-8da5-f02240387e34",
        "type": "EWALLET",
        "country": "PH",
        "business_id": "5ed75086a883856178afc12e",
        "customer_id": None,
        "reference_id": "0724a49f-388f-41d9-9662-7aefad85a02b",
        "reusability": "ONE_TIME_USE",
        "status": "ACTIVE",
        "actions": [],
        "description": None,
        "created": "2022-10-18T01:31:45.843043772Z",
        "updated": "2022-10-18T01:31:45.843043772Z",
        "metadata": {},
        "billing_information": None,
        "failure_code": None,
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
        "direct_bank_transfer": None,
        "direct_debit": None,
        "card": None,
        "over_the_counter": None,
        "qr_code": None,
        "virtual_account": None
    }