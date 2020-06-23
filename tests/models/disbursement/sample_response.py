def disbursement_response():
    return {
        "user_id": "5ed75086a883856178afc12e",
        "external_id": "demo_1475459775872",
        "amount": 17000,
        "bank_code": "BCA",
        "account_holder_name": "Bob Jones",
        "disbursement_description": "Reimbursement for shoes",
        "status": "PENDING",
        "id": "5ef1c4f40c2e150017ce3b96",
    }


def disbursement_banks_response():
    return [
        {
            "name": "Mandiri Taspen Pos (formerly Bank Sinar Harapan Bali)",
            "code": "MANDIRI_TASPEN",
            "can_disburse": True,
            "can_name_validate": True,
        },
        {
            "name": "Bank QNB Indonesia (formerly Bank QNB Kesawan)",
            "code": "QNB_INDONESIA",
            "can_disburse": True,
            "can_name_validate": True,
        },
    ]
