def cardless_credit_payment_response():
    return {
        "redirect_url": "https://pay-sandbox.kredivo.com/signIn?tk=26458cdf-660c-4491-a1de-bb6e63312d8a",
        "order_id": "e8ae4066-7980-499f-b92c-eb3a587782c1",
        "external_id": "id-1595923113",
        "cardless_credit_type": "KREDIVO",
    }


def cardless_credit_payment_type_response():
    return {
        "message": "Available payment types are listed.",
        "payments": [
            {
                "raw_monthly_installment": 401000,
                "name": "Bayar dalam 30 hari",
                "amount": 401000,
                "installment_amount": 401000,
                "raw_amount": 401000,
                "rate": 0,
                "down_payment": 0,
                "monthly_installment": 401000,
                "discounted_monthly_installment": 0,
                "tenure": 1,
                "id": "30_days",
            }
        ],
    }
