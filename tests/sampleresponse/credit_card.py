def reverse_auth_response():
    return {
        "status": "SUCCEEDED",
        "currency": "IDR",
        "credit_card_charge_id": "5f0421fa8cc1e8001973a1d6",
        "business_id": "5ed75086a883856178afc12e",
        "external_id": "card_preAuth-1594106356",
        "amount": 75000,
        "created": "2020-07-07T07:19:48.896Z",
        "id": "5f0422148cc1e8001973a1dc",
    }


def charge_response():
    return {
        "status": "AUTHORIZED",
        "authorized_amount": 75000,
        "capture_amount": 0,
        "currency": "IDR",
        "business_id": "5ed75086a883856178afc12e",
        "merchant_id": "xendit_ctv_agg",
        "merchant_reference_code": "5f0421faa98815a4f4c92a0d",
        "external_id": "card_preAuth-1594106356",
        "eci": "07",
        "charge_type": "MULTIPLE_USE_TOKEN",
        "masked_card_number": "400000XXXXXX0002",
        "card_brand": "VISA",
        "card_type": "CREDIT",
        "descriptor": "XENDIT*XENDIT&AMP;#X27;S INTERN",
        "bank_reconciliation_id": "5941063625146828103011",
        "approval_code": "831000",
        "created": "2020-07-07T07:19:22.921Z",
        "id": "5f0421fa8cc1e8001973a1d6",
        "metadata": {
            "meta": "data"
        },
    }


def refund_response():
    return {
        "status": "REQUESTED",
        "currency": "IDR",
        "credit_card_charge_id": "5f0422aa2bbbe50019a368c2",
        "user_id": "5ed75086a883856178afc12e",
        "amount": 10000,
        "external_id": "card_refund-1594106755",
        "created": "2020-07-07T07:25:56.872Z",
        "updated": "2020-07-07T07:25:57.740Z",
        "id": "5f0423848bb8da600c57c44f",
        "fee_refund_amount": 290,
    }


def promotion_response():
    return {
        "business_id": "5ed75086a883856178afc12e",
        "reference_id": "BRI_20_JAN-1594176600",
        "description": "20% discount applied for all BRI cards",
        "start_time": "2020-01-01T00:00:00.000Z",
        "end_time": "2021-01-01T00:00:00.000Z",
        "type": "CARD_BIN",
        "discount_amount": 10000,
        "bin_list": ["400000", "460000"],
        "currency": "IDR",
        "id": "c65a2ae7-ce75-4a15-bbec-55d076f46bd0",
        "created": "2020-07-08T02:50:02.296Z",
        "status": "ACTIVE",
    }
