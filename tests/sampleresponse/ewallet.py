def ovo_payment_response(x_api_version="2020-02-01"):
    if x_api_version == "2020-02-01":
        return {
            "amount": 80001,
            "business_id": "5ed75086a883856178afc12e",
            "created": "2020-06-30T10:58:08.648Z",
            "ewallet_type": "OVO",
            "external_id": "ovo-ewallet-testing-id-123321131114",
            "phone": "08183123123",
            "status": "PENDING",
        }
    elif x_api_version == "2019-02-04":
        return {
            "amount": 80001,
            "business_id": "5ed75086a883856178afc12e",
            "ewallet_type": "OVO",
            "external_id": "ovo-ewallet-testing-id-123321131114",
            "phone": "08183123123",
            "transaction_date": "2020-07-01T04:40:43.000Z",
            "ewallet_transaction_id": "cea4a665-0c91-408b-93a8-7855d2b7ac45",
        }


def ovo_payment_status_response():
    return {
        "amount": "8888",
        "business_id": "5ed75086a883856178afc12e",
        "ewallet_type": "OVO",
        "external_id": "ovo-ewallet-testing-id-1234",
        "status": "COMPLETED",
        "transaction_date": "2020-06-30T01:32:28.267Z",
    }


def dana_payment_response():
    return {
        "external_id": "dana-ewallet-test-33312",
        "amount": 1001,
        "checkout_url": "https://sandbox.m.dana.id/m/portal/cashier/checkout?bizNo=20200630111212800110166944200487696&timestamp=1593501869722&mid=216620000000261692328&sign=NjoCAHIi7py03bmpNRLztChCD3JyhbHoIjv1zNZhqYRXByYNiCAsXfjNMKcOOEQHQA%2BALYU0estGFaUz60qM4r9LoqVhuEn%2FCqzHzbmHdy54FlBUnwPINBTVIPIGgpLXSEQeUTHFUmU5QcoLelzZgZiPjbZaFdPqTlZtpW1XrovWuad2FslHrpsnscko5yp2A4vpAIIxM3%2BV9c8596B4hmugdEhb4qqJ05XQtOXPI%2Fui8qJG84Pc0ezkjavsMfTbD%2BOjRiLSt4Xowsm3KUe1CadycW3GTx6CTFHeRGaCauyMJR5VxbFsu5dztYpvrr%2FaHiIhk4t2XB%2FbQl1JPfl1NQ%3D%3D",
        "ewallet_type": "DANA",
    }


def dana_payment_status_response():
    return {
        "external_id": "dana-ewallet-test-1234",
        "business_id": "5ed75086a883856178afc12e",
        "amount": "1001.00",
        "expiration_date": "2020-12-20T07:00:00+07:00",
        "checkout_url": "https://sandbox.m.dana.id/m/portal/cashier/checkout?bizNo=20200630111212800110166293400518907&timestamp=1593480789887&mid=216620000000261692328&sign=U4vHxKFRCr4ePrZb8Ym24dfEAJ0v8%2FRXPjYcbBEGgCiRKEFD%2FPhIAF%2FNQLQBiiAXEDEM%2FaRSyL%2FLp1d0kKghxgFuRop4glre6JorCIbi%2FswUfOK7X%2BzEB5mEQZhPbxfEeM7jciHH3Cuk%2BAhZ2TV5M15QxWh5icRN3jeDOBPotVvwwjgSzZXBv6PKrmpdY03hJf%2BkKaGWNiEOUFeaGuBQSIBVQjPraiT3RkLrStwae1C1D8Y%2FNS42NSU7XdtHj41PfKgk89WUSUvqzqJs4Ch20N1ZCoZ4ay5D3Wuv7VzQtA5Agx%2ByuJxdWNUVBZL8dpO8oHcToBQEGtPbeaoD0ftPKw%3D%3D",
        "status": "PENDING",
    }


def linkaja_payment_response():
    return {
        "checkout_url": "https://ewallet-linkaja-dev.xendit.co/checkouts/474f2ce2-f991-4fff-b1c2-c92b61d436a4",
        "transaction_date": "2020-06-30T08:20:50.426Z",
        "amount": 300000,
        "external_id": "linkaja-ewallet-test-1593505247",
        "ewallet_type": "LINKAJA",
    }


def linkaja_payment_status_completed_response():
    return {
        "business_id": "5ed75086a883856178afc12e",
        "external_id": "linkaja-ewallet-test-1234",
        "amount": 300000,
        "status": "COMPLETED",
        "payment_timestamp": "2020-06-30T07:50:10.105Z",
    }


def linkaja_payment_status_expired_response():
    return {
        "business_id": "5ed75086a883856178afc12e",
        "external_id": "linkaja-ewallet-test-123",
        "amount": 300000,
        "status": "EXPIRED",
        "expired_at": "2020-06-30T02:03:36.078Z",
        "checkout_url": "https://ewallet-linkaja-dev.xendit.co/checkouts/ecae96ff-2e06-4a00-9a42-95e44ba56aca",
    }
