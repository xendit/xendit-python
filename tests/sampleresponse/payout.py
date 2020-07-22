def payout_response():
    return {
        "id": "a6ee1bf1-ffcd-4bda-a7ab-99c1d5cd0472",
        "external_id": "payout-1595405117",
        "amount": 50000,
        "merchant_name": "Xendit&amp;#x27;s Intern",
        "status": "PENDING",
        "expiration_timestamp": "2020-07-23T08:05:19.815Z",
        "created": "2020-07-22T08:05:18.421Z",
        "email": "test@email.co",
        "payout_url": "https://payout-staging.xendit.co/web/a6ee1bf1-ffcd-4bda-a7ab-99c1d5cd0472",
    }


def void_payout_response():
    return {
        "id": "a6ee1bf1-ffcd-4bda-a7ab-99c1d5cd0472",
        "external_id": "payout-1595405117",
        "amount": 50000,
        "merchant_name": "Xendit&amp;#x27;s Intern",
        "status": "VOIDED",
        "expiration_timestamp": "2020-07-23T08:05:19.815Z",
        "created": "2020-07-22T08:05:18.421Z",
        "email": "test@email.co",
    }
