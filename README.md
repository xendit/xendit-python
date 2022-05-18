<!-- omit in toc -->
# Xendit Python Library

This library is the abstraction of Xendit API for access from applications written with Python.

<!-- omit in toc -->
## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [API Documentation](#api-documentation)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [API Key](#api-key)
    - [Global Variable](#global-variable)
    - [Use Xendit Instance](#use-xendit-instance)
  - [Headers](#headers)
  - [Object Creation](#object-creation)
  - [Using Custom HTTP Client](#using-custom-http-client)
  - [Balance Service](#balance-service)
    - [Get Balance](#get-balance)
  - [Credit Card Service](#credit-card-service)
    - [Create Authorization](#create-authorization)
    - [Reverse Authorization](#reverse-authorization)
    - [Create Charge](#create-charge)
    - [Capture Charge](#capture-charge)
    - [Get Charge](#get-charge)
    - [Create Refund](#create-refund)
    - [Create Promotion](#create-promotion)
  - [eWallets Service](#ewallets-service)
    - [Create OVO Payment](#create-ovo-payment)
    - [Create DANA Payment](#create-dana-payment)
    - [Create LinkAja Payment](#create-linkaja-payment)
    - [Get Payment Status](#get-payment-status)
  - [Cardless Credit Service](#cardless-credit-service)
    - [Create Payment / Generate Checkout URL](#create-payment--generate-checkout-url)
    - [Calculate Payment Types](#calculate-payment-types)
  - [QR Codes Service](#qr-codes-service)
    - [Create QR Code](#create-qr-code)
    - [Get QR Code by External ID](#get-qr-code-by-external-id)
  - [Direct Debit Service](#direct-debit-service)
    - [Create Customer](#create-customer)
    - [Get Customer by Reference ID](#get-customer-by-reference-id)
    - [Initialize Linked Account Tokenization](#initialize-linked-account-tokenization)
    - [Validate OTP for Linked Account Token](#validate-otp-for-linked-account-token)
    - [Retrieve Accessible Accounts by Linked Account Token](#retrieve-accessible-accounts-by-linked-account-token)
    - [Create Payment Method](#create-payment-method)
    - [Get Payment Methods by Customer ID](#get-payment-methods-by-customer-id)
    - [Create Direct Debit Payment](#create-direct-debit-payment)
    - [Create Recurring Payment with Direct Debit](#create-recurring-payment-with-direct-debit)
    - [Validate OTP for Direct Debit Payment](#validate-otp-for-direct-debit-payment)
    - [Get Direct Debit Payment Status by ID](#get-direct-debit-payment-status-by-id)
    - [Get Direct Debit Payment Status by Reference ID](#get-direct-debit-payment-status-by-reference-id)
  - [Virtual Account Service](#virtual-account-service)
    - [Create Virtual Account](#create-virtual-account)
    - [Get Virtual Account Banks](#get-virtual-account-banks)
    - [Get Virtual Account](#get-virtual-account)
    - [Update Virtual Account](#update-virtual-account)
    - [Get Virtual Account Payment](#get-virtual-account-payment)
  - [Retail Outlet Service](#retail-outlet-service)
    - [Create Fixed Payment Code](#create-fixed-payment-code)
    - [Update Fixed Payment Code](#update-fixed-payment-code)
    - [Get Fixed Payment Code](#get-fixed-payment-code)
  - [Invoice Service](#invoice-service)
    - [Create Invoice](#create-invoice)
    - [Get Invoice](#get-invoice)
    - [Expire Invoice](#expire-invoice)
    - [List All Invoice](#list-all-invoice)
  - [Recurring Payment Service](#recurring-payment-service)
    - [Create Recurring Payment](#create-recurring-payment)
    - [Get Recurring Payment](#get-recurring-payment)
    - [Edit Recurring Payment](#edit-recurring-payment)
    - [Stop Recurring Payment](#stop-recurring-payment)
    - [Pause Recurring Payment](#pause-recurring-payment)
    - [Resume Recurring Payment](#resume-recurring-payment)
  - [Payout Service](#payout-service)
    - [Create Payout](#create-payout)
    - [Get Payout](#get-payout)
    - [Void a Payout](#void-a-payout)
  - [Disbursement Service](#disbursement-service)
    - [Create Disbursement](#create-disbursement)
    - [Get Disbursement by ID](#get-disbursement-by-id)
    - [Get Disbursement by External ID](#get-disbursement-by-external-id)
    - [Get Available Banks](#get-available-banks)
  - [Batch Disbursement Service](#batch-disbursement-service)
    - [Create Batch Disbursement](#create-batch-disbursement)
    - [Get Batch Disbursement Available Banks](#get-batch-disbursement-available-banks)
  - [xenPlatform Service](#xenplatform-service)
    - [Create Account](#create-account)
    - [Set Callback URLs](#set-callback-urls)
    - [Transfers](#transfers)
- [Contributing](#contributing)
  - [Tests](#tests)
    - [Running the Test](#running-the-test)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## API Documentation
Please check [Xendit API Reference](https://xendit.github.io/apireference/).

## Requirements

Python 3.7 or later

## Installation

To use the package, run ```pip install xendit-python```

## Usage

### API Key

To add API Key, you have 2 option: Use global variable or use Xendit instance

#### Global Variable

```python
import xendit
xendit.api_key = "test-key123"

# Then just run each class as static
from xendit import Balance
Balance.get()
```

#### Use Xendit Instance
```python
import xendit
x = xendit.Xendit(api_key="test-key123")

# Then access each class from x attribute
Balance = x.Balance
Balance.get()
```

### Headers

You can add headers by using the following keyword parameters
- X-IDEMPOTENCY-KEY: `x_idempotency_key`

```
VirtualAccount.create(x_idempotency_key="your-idemp-key")
```

- for-user-id: `for_user_id`

```
Balance.get(for_user_id='subaccount-user-id')
```

- X-API-VERSION: `x_api_version`

```
Balance.get(x_api_version='2020-01-01')
```

### Object Creation

If an API need an object as its parameter, you can use either dictionary for that class or a helper method e.g:

```python
items = []
item = {
    id: "123123",
    name: "Phone Case",
    price: 100000,
    quantity: 1
}
items.append(item)
EWallet.create_linkaja_payment(
    external_id="linkaja-ewallet-test-1593663498",
    phone="089911111111",
    items=items,
    amount=300000,
    callback_url="https://my-shop.com/callbacks",
    redirect_url="https://xendit.co/",
)
```

is equivalent with

```python
items = []
item = EWallet.helper_create_linkaja_item(
    id="123123", name="Phone Case", price=100000, quantity=1
)
items.append(item)
EWallet.create_linkaja_payment(
    external_id="linkaja-ewallet-test-1593663498",
    phone="089911111111",
    items=items,
    amount=300000,
    callback_url="https://my-shop.com/callbacks",
    redirect_url="https://xendit.co/",
)
```

### Using Custom HTTP Client

To use your own HTTP Client, you can do it as long as your http client adhere to HTTP client interface at `xendit/network/http_client_interface.py`. For example, [requests](https://github.com/psf/requests) library are compatible with that interface, so we can freely use it in our library. To attach it to your instance, add it to your xendit parameter.

```python
import xendit

xendit_instance =  xendit.Xendit(api_key='', http_client=YourHTTPClientClass)
```

### Balance Service

#### Get Balance

The `account_type` parameter is optional.

```python
from xendit import Balance
Balance.get()

Balance.AccountType(
    account_type=BalanceAccountType.CASH,
)
```

Usage example:

```python
from xendit import Balance, BalanceAccountType
Balance balance = Balance.get(
    account_type=BalanceAccountType.CASH,
)

# To get the JSON view
print(balance)

# To get only the value
print(balance.balance)
``` 

Will return

```
{'balance': 1000000000}
1000000000
```

### Credit Card Service

#### Create Authorization

```python
from xendit import CreditCard

charge = CreditCard.create_authorization(
    token_id="5f0410898bcf7a001a00879d",
    external_id="card_preAuth-1594106356",
    amount=75000,
    card_cvn="123",
    metadata={
        "meta": "data",
    },
)
print(charge)
```

Will return

```
{
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
    }
}
```

#### Reverse Authorization

```python
from xendit import CreditCard

reverse_authorization = CreditCard.reverse_authorizatiton(
    credit_card_charge_id="5f0421fa8cc1e8001973a1d6",
    external_id="reverse-authorization-1594106387",
)
print(reverse_authorization)
```

Will return

```
{
    "status": "SUCCEEDED",
    "currency": "IDR",
    "credit_card_charge_id": "5f0421fa8cc1e8001973a1d6",
    "business_id": "5ed75086a883856178afc12e",
    "external_id": "card_preAuth-1594106356",
    "amount": 75000,
    "created": "2020-07-07T07:19:48.896Z",
    "id": "5f0422148cc1e8001973a1dc"
}
```

#### Create Charge

```python
from xendit import CreditCard

charge = CreditCard.create_charge(
    token_id="5f0410898bcf7a001a00879d",
    external_id="card_charge-1594106478",
    amount=75000,
    card_cvn="123",
    metadata={
        "meta": "data",
    },
)
print(charge)
```

Will return

```
{
    "status": "CAPTURED",
    "authorized_amount": 75000,
    "capture_amount": 75000,
    "currency": "IDR",
    "business_id": "5ed75086a883856178afc12e",
    "merchant_id": "xendit_ctv_agg",
    "merchant_reference_code": "5f0422746fc1d25bd222df2e",
    "external_id": "card_charge-1594106478",
    "eci": "07",
    "charge_type": "MULTIPLE_USE_TOKEN",
    "masked_card_number": "400000XXXXXX0002",
    "card_brand": "VISA",
    "card_type": "CREDIT",
    "descriptor": "XENDIT*XENDIT&AMP;#X27;S INTERN",
    "bank_reconciliation_id": "5941064846646923303008",
    "approval_code": "831000",
    "created": "2020-07-07T07:21:25.027Z",
    "id": "5f0422752bbbe50019a368b5",
    "metadata": {
        "meta": "data"
    }
}
```

#### Capture Charge

```python
from xendit import CreditCard

charge = CreditCard.capture_charge(
    credit_card_charge_id="5f0422aa2bbbe50019a368c2",
    amount=75000,
)
print(charge)
```

Will return

```
{
    "status": "CAPTURED",
    "authorized_amount": 75000,
    "capture_amount": 75000,
    "currency": "IDR",
    "created": "2020-07-07T07:22:18.719Z",
    "business_id": "5ed75086a883856178afc12e",
    "merchant_id": "xendit_ctv_agg",
    "merchant_reference_code": "5f0422aa6fc1d25bd222df32",
    "external_id": "card_preAuth-1594106532",
    "eci": "07",
    "charge_type": "MULTIPLE_USE_TOKEN",
    "masked_card_number": "400000XXXXXX0002",
    "card_brand": "VISA",
    "card_type": "CREDIT",
    "descriptor": "XENDIT*XENDIT&AMP;#X27;S INTERN",
    "bank_reconciliation_id": "5941065383296525603007",
    "approval_code": "831000",
    "mid_label": "CTV_TEST",
    "id": "5f0422aa2bbbe50019a368c2"
}
```

#### Get Charge

```python
from xendit import CreditCard

charge = CreditCard.get_charge(
    credit_card_charge_id="5f0422aa2bbbe50019a368c2",
)
print(charge)
```

Will return

```
{
    "status": "CAPTURED",
    "authorized_amount": 75000,
    "capture_amount": 75000,
    "currency": "IDR",
    "created": "2020-07-07T07:22:18.719Z",
    "business_id": "5ed75086a883856178afc12e",
    "merchant_id": "xendit_ctv_agg",
    "merchant_reference_code": "5f0422aa6fc1d25bd222df32",
    "external_id": "card_preAuth-1594106532",
    "eci": "07",
    "charge_type": "MULTIPLE_USE_TOKEN",
    "masked_card_number": "400000XXXXXX0002",
    "card_brand": "VISA",
    "card_type": "CREDIT",
    "descriptor": "XENDIT*XENDIT&AMP;#X27;S INTERN",
    "bank_reconciliation_id": "5941065383296525603007",
    "approval_code": "831000",
    "mid_label": "CTV_TEST",
    "metadata": {},
    "id": "5f0422aa2bbbe50019a368c2"
}
```

#### Create Refund

```python
from xendit import CreditCard

refund = CreditCard.create_refund(
    credit_card_charge_id="5f0422aa2bbbe50019a368c2",
    amount=10000,
    external_id="card_refund-1594106755",
)
print(refund)
```

Will return

```
{
    "status": "REQUESTED",
    "currency": "IDR",
    "credit_card_charge_id": "5f0422aa2bbbe50019a368c2",
    "user_id": "5ed75086a883856178afc12e",
    "amount": 10000,
    "external_id": "card_refund-1594106755",
    "created": "2020-07-07T07:25:56.872Z",
    "updated": "2020-07-07T07:25:57.740Z",
    "id": "5f0423848bb8da600c57c44f",
    "fee_refund_amount": 290
}
```

#### Create Promotion

```python
from xendit import CreditCard

promotion = CreditCard.create_promotion(
    reference_id="BRI_20_JAN-1594176600",
    description="20% discount applied for all BRI cards",
    discount_amount=10000,
    bin_list=['400000', '460000'],
    start_time="2020-01-01T00:00:00.000Z",
    end_time="2021-01-01T00:00:00.000Z",
)
print(promotion)
```

Will return

```
{
    "business_id": "5ed75086a883856178afc12e",
    "reference_id": "BRI_20_JAN-1594176600",
    "description": "20% discount applied for all BRI cards",
    "start_time": "2020-01-01T00:00:00.000Z",
    "end_time": "2021-01-01T00:00:00.000Z",
    "type": "CARD_BIN",
    "discount_amount": 10000,
    "bin_list": [
        "400000",
        "460000"
    ],
    "currency": "IDR",
    "id": "c65a2ae7-ce75-4a15-bbec-55d076f46bd0",
    "created": "2020-07-08T02:50:02.296Z",
    "status": "ACTIVE"
}
```

### eWallets Service

#### Create E-Wallet Charge
```python
from xendit import EWallet

basket = []
basket_item = EWallet.helper_create_basket_item(
    reference_id = "basket-product-ref-id",
    name = "product_name",
    category = "product_category",
    currency = "IDR",
    price = 50000,
    quantity = 5,
    type = "product_type",
    sub_category = "product_sub_category",
    metadata = {
        "meta": "data"
    }
)
basket.append(basket_item)

ewallet_charge = EWallet.create_ewallet_charge(
    reference_id="basket-product-ref-id",
    currency="IDR",
    amount=10000,
    checkout_method="ONE_TIME_PAYMENT",
    channel_code="ID_SHOPEEPAY",
    channel_properties={
        "success_redirect_url": "https://yourwebsite.com/order/123",
    },
    basket=basket,
)
```

Will return

```json
{
    "id": "ewc_f3925450-5c54-4777-98c1-fcf22b0d1e1c",
    "business_id": "5ed75086a883856178afc12e",
    "reference_id": "basket-product-ref-id",
    "status": "PENDING",
    "currency": "IDR",
    "charge_amount": 10000,
    "capture_amount": 10000,
    "checkout_method": "ONE_TIME_PAYMENT",
    "channel_code": "ID_SHOPEEPAY",
    "channel_properties": {
        "success_redirect_url": "https://yourwebsite.com/order/123",
    },
    "actions": {
        "desktop_web_checkout_url": null,
        "mobile_web_checkout_url": null,
        "mobile_deeplink_checkout_url": "https://ewallet-mock-connector.xendit.co/v1/ewallet_connector/checkouts?token=ZjQyOGIzMGVlNGFjOWJhNTE2YWQ3NGQyN2RiMTIwODg6ZTY2YjA2YjQ1ZjJlZWI0NDA4OGNjODg2NGFlYzQ2N2U5YTI5MjM3ODUzODViYzljNjQyYWYwOGExMjU4MzdmMTc3NDFlMWZmYjcxN2MzOWZiYmMyNjY4N2ViNmMxM2ZkMjg1ZmIzZDM5ZmZiZDYzM2ViNGMyMDRkOWM3ZTUzNWUyMDBlOWUzMzdhZTkwZjllZjQwZjQyMjExOTkyNWQ2MTg2YzgzZTQ3N2JhYWZkNDFhN2U0MWM1ZDMzMGJmMmNhNzhiMjhmMmY5ZDBjZDQ4MjlkODA3MjE5YWQzYTlhNTE0YmM1NjUzYjljMmZlOWU1YjMwM2FmNTZiNmViNGVlZDIxODQzNzdjNDJmYjRmNzBmZDZlZDhlM2MyMGM4YmExY2RmNTVkOTdjZmU3MWYxMWVmMDYzMmQzNGE1ZTFmMzE=",
        "qr_checkout_string": "test-qr-string",
    },
    "is_redirect_required": true,
    "callback_url": "https://yourwebsite.com/order/123",
    "created": "2021-02-09T06:22:35.064408Z",
    "updated": "2021-02-09T06:22:35.064408Z",
    "voided_at": null,
    "capture_now": true,
    "customer_id": null,
    "payment_method_id": null,
    "failure_code": null,
    "basket": [
        {
            "reference_id": "basket-product-ref-id",
            "name": "product_name",
            "category": "product_category",
            "currency": "IDR",
            "price": 50000,
            "quantity": 5,
            "type": "product_type",
            "url": "",
            "description": "",
            "sub_category": "product_sub_category",
            "metadata": {
                "meta": "data"
            }
        }
    ],
    "metadata": null,
}
```

#### Get E-Wallet Charge Status
```python
from xendit import EWallet

ewallet_charge = EWallet.get_ewallet_charge_status(
    charge_id="ewc_f3925450-5c54-4777-98c1-fcf22b0d1e1c",
)
```

Will return

```json
{
    "id": "ewc_f3925450-5c54-4777-98c1-fcf22b0d1e1c",
    "business_id": "5ed75086a883856178afc12e",
    "reference_id": "basket-product-ref-id",
    "status": "PENDING",
    "currency": "IDR",
    "charge_amount": 10000,
    "capture_amount": 10000,
    "checkout_method": "ONE_TIME_PAYMENT",
    "channel_code": "ID_SHOPEEPAY",
    "channel_properties": {
        "success_redirect_url": "https://yourwebsite.com/order/123",
    },
    "actions": {
        "desktop_web_checkout_url": null,
        "mobile_web_checkout_url": null,
        "mobile_deeplink_checkout_url": "https://ewallet-mock-connector.xendit.co/v1/ewallet_connector/checkouts?token=ZjQyOGIzMGVlNGFjOWJhNTE2YWQ3NGQyN2RiMTIwODg6ZTY2YjA2YjQ1ZjJlZWI0NDA4OGNjODg2NGFlYzQ2N2U5YTI5MjM3ODUzODViYzljNjQyYWYwOGExMjU4MzdmMTc3NDFlMWZmYjcxN2MzOWZiYmMyNjY4N2ViNmMxM2ZkMjg1ZmIzZDM5ZmZiZDYzM2ViNGMyMDRkOWM3ZTUzNWUyMDBlOWUzMzdhZTkwZjllZjQwZjQyMjExOTkyNWQ2MTg2YzgzZTQ3N2JhYWZkNDFhN2U0MWM1ZDMzMGJmMmNhNzhiMjhmMmY5ZDBjZDQ4MjlkODA3MjE5YWQzYTlhNTE0YmM1NjUzYjljMmZlOWU1YjMwM2FmNTZiNmViNGVlZDIxODQzNzdjNDJmYjRmNzBmZDZlZDhlM2MyMGM4YmExY2RmNTVkOTdjZmU3MWYxMWVmMDYzMmQzNGE1ZTFmMzE=",
        "qr_checkout_string": "test-qr-string",
    },
    "is_redirect_required": true,
    "callback_url": "https://yourwebsite.com/order/123",
    "created": "2021-02-09T06:22:35.064408Z",
    "updated": "2021-02-09T06:22:35.064408Z",
    "voided_at": null,
    "capture_now": true,
    "customer_id": null,
    "payment_method_id": null,
    "failure_code": null,
    "basket": [
        {
            "reference_id": "basket-product-ref-id",
            "name": "product_name",
            "category": "product_category",
            "currency": "IDR",
            "price": 50000,
            "quantity": 5,
            "type": "product_type",
            "url": "",
            "description": "",
            "sub_category": "product_sub_category",
            "metadata": {
                "meta": "data"
            }
        }
    ],
    "metadata": null,
}
```

### Cardless Credit Service

#### Create Payment / Generate Checkout URL

```python
from xendit import CardlessCredit, CardlessCreditType

cardless_credit_items = []
cardless_credit_items.append(
    CardlessCredit.helper_create_item(
        id="item-123",
        name="Phone Case",
        price=200000,
        type="Smartphone",
        url="http://example.com/phone/phone_case",
        quantity=2,
    )
)
customer_details = CardlessCredit.helper_create_customer_details(
    first_name="customer first name",
    last_name="customer last name",
    email="customer@email.com",
    phone="0812332145",
)
shipping_address = CardlessCredit.helper_create_shipping_address(
    first_name="first name",
    last_name="last name",
    address="Jl Teknologi No. 12",
    city="Jakarta",
    postal_code="12345",
    phone="081513114262",
    country_code="IDN",
)
cardless_credit_payment = CardlessCredit.create_payment(
    cardless_credit_type=CardlessCreditType.KREDIVO,
    external_id="id-1595923113",
    amount=10000,
    payment_type="3_months",
    items=cardless_credit_items,
    customer_details=customer_details,
    shipping_address=shipping_address,
    redirect_url="https://my-shop.com/home",
    callback_url="https://my-shop.com/callback",
)
print(cardless_credit_payment)
```

Will return

```
{
    "redirect_url": "https://pay-sandbox.kredivo.com/signIn?tk=26458cdf-660c-4491-a1de-bb6e63312d8a",
    "order_id": "e8ae4066-7980-499f-b92c-eb3a587782c1",
    "external_id": "id-1595923113",
    "cardless_credit_type": "KREDIVO"
}
```

#### Calculate Payment Types

```python
from xendit import CardlessCredit, CardlessCreditType

cardless_credit_items = []
cardless_credit_items.append(
    CardlessCredit.helper_create_item(
        id="item-123",
        name="Phone Case",
        price=200000,
        type="Smartphone",
        url="http://example.com/phone/phone_case",
        quantity=2,
    )
)
cardless_credit_payment_types = CardlessCredit.calculate_payment_type(
    cardless_credit_type=CardlessCreditType.KREDIVO,
    amount=10000,
    items=cardless_credit_items,
)
print(cardless_credit_payment_types)
```

Will return

```
{
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
            "id": "30_days"
        }
    ]
}
```

### QR Codes Service

#### Create QR Code

```python
from xendit import QRCode, QRCodeType

qrcode = QRCode.create(
    external_id="qrcode-id-1594794038",
    type=QRCodeType.DYNAMIC,
    callback_url="https://webhook.site",
    amount=4000,
)
print(qrcode)
```

Will return

```
{
    "id": "qr_13c31ddd-9d58-449b-9f52-1bf5123a45b5",
    "external_id": "qrcode-id-1594794038",
    "amount": 4000,
    "qr_string": "00020101021226660014ID.LINKAJA.WWW011893600911002411480002152004230411480010303UME51450015ID.OR.GPNQR.WWW02150000000000000000303UME520454995802ID5920Placeholder merchant6007Jakarta610612345662380115wLoc6DRGwAOgSkZ0715wLoc6DRGwAOgSkZ53033605404400063047668",
    "callback_url": "https://webhook.site",
    "type": "DYNAMIC",
    "status": "ACTIVE",
    "created": "2020-07-15T06:20:40.636Z",
    "updated": "2020-07-15T06:20:40.636Z"
}
```

#### Get QR Code by External ID

```python
from xendit import QRCode

qrcode = QRCode.get_by_ext_id(
    external_id="qrcode-id-1594794038",
)
print(qrcode)
```

Will return

```
{
    "id": "qr_13c31ddd-9d58-449b-9f52-1bf5123a45b5",
    "external_id": "qrcode-id-1594794038",
    "amount": 4000,
    "qr_string": "00020101021226660014ID.LINKAJA.WWW011893600911002411480002152004230411480010303UME51450015ID.OR.GPNQR.WWW02150000000000000000303UME520454995802ID5920Placeholder merchant6007Jakarta610612345662380115wLoc6DRGwAOgSkZ0715wLoc6DRGwAOgSkZ53033605404400063047668",
    "callback_url": "https://webhook.site",
    "type": "DYNAMIC",
    "status": "ACTIVE",
    "created": "2020-07-15T06:20:40.636Z",
    "updated": "2020-07-15T06:20:40.636Z"
}
```

### Direct Debit Service

#### Create Customer

```python
from xendit import DirectDebit

customer = DirectDebit.create_customer(
    reference_id="merc-1594279037",
    email="t@x.co",
    given_names="Adyaksa",
)
print(customer)
```

Will return

```
{
    "id": "ed20b5db-df04-41fc-8018-8ea4ac4d1030",
    "reference_id": "merc-1594279037",
    "description": null,
    "given_names": "Adyaksa",
    "middle_name": null,
    "surname": null,
    "mobile_number": null,
    "phone_number": null,
    "email": "t@x.co",
    "nationality": null,
    "addresses": null,
    "date_of_birth": null,
    "employment": null,
    "source_of_wealth": null,
    "metadata": null
}
```

#### Get Customer by Reference ID

```python
from xendit import DirectDebit

customer = DirectDebit.get_customer_by_ref_id(
    reference_id="merc-1594279037",
)
print(customer)
```

Will return

```
[{
    "id": "ed20b5db-df04-41fc-8018-8ea4ac4d1030",
    "reference_id": "merc-1594279037",
    "description": null,
    "given_names": "Adyaksa",
    "middle_name": null,
    "surname": null,
    "mobile_number": null,
    "phone_number": null,
    "email": "t@x.co",
    "nationality": null,
    "addresses": null,
    "date_of_birth": null,
    "employment": null,
    "source_of_wealth": null,
    "metadata": null
}]
```

#### Initialize Linked Account Tokenization

```python
from xendit import DirectDebit

card_linking = DirectDebit.helper_create_card_link(
    account_mobile_number="+62818555988",
    card_last_four="8888",
    card_expiry="06/24",
    account_email="test.email@xendit.co",
)
linked_account = DirectDebit.initialize_tokenization(
    customer_id="ed20b5db-df04-41fc-8018-8ea4ac4d1030",
    channel_code="DC_BRI",
    properties=card_linking,   
)
print(linked_account)
```

Will return

```
{
    "id": "lat-f325b757-0aae-4c24-92c5-3661e299e154",
    "customer_id": "ed20b5db-df04-41fc-8018-8ea4ac4d1030",
    "channel_code": "DC_BRI",
    "authorizer_url": null,
    "status": "PENDING",
    "metadata": null
}
```

#### Validate OTP for Linked Account Token

```python
from xendit import DirectDebit

linked_account = DirectDebit.validate_token_otp(
    linked_account_token_id="lat-f325b757-0aae-4c24-92c5-3661e299e154",
    otp_code="333000",
)
print(linked_account)
```

Will return

```
{
    "id": "lat-f325b757-0aae-4c24-92c5-3661e299e154",
    "customer_id": "ed20b5db-df04-41fc-8018-8ea4ac4d1030",
    "channel_code": "DC_BRI",
    "status": "SUCCESS",
    "metadata": null
}
```

#### Retrieve Accessible Accounts by Linked Account Token

```python
from xendit import DirectDebit

accessible_accounts = DirectDebit.get_accessible_account_by_token(
    linked_account_token_id="lat-f325b757-0aae-4c24-92c5-3661e299e154",
)
print(accessible_accounts)
```

Will return

```
[{
    "channel_code": "DC_BRI",
    "id": "la-08b089e8-7035-4f5f-bdd9-94edd9dc9480",
    "properties": {
        "card_expiry": "06/24",
        "card_last_four": "8888",
        "currency": "IDR",
        "description": ""
    },
    "type": "DEBIT_CARD"
}]
```

#### Create Payment Method

```python
from xendit import DirectDebit, DirectDebitPaymentMethodType

payment_method = DirectDebit.create_payment_method(
    customer_id="ed20b5db-df04-41fc-8018-8ea4ac4d1030",
    type=DirectDebitPaymentMethodType.DEBIT_CARD,
    properties={'id': 'la-fac7e744-ab40-4100-a447-cbbb16f29ded'},
)

print(payment_method)
```

Will return

```
{
    "customer_id": "ed20b5db-df04-41fc-8018-8ea4ac4d1030",
    "type": "DEBIT_CARD",
    "properties": {
        "id": "la-fac7e744-ab40-4100-a447-cbbb16f29ded",
        "currency": "IDR",
        "card_expiry": "06/24",
        "description": "",
        "channel_code": "DC_BRI",
        "card_last_four": "8888"
    },
    "status": "ACTIVE",
    "metadata": {},
    "id": "pm-b6116aea-8c23-42d0-a1e6-33227b52fccd",
    "created": "2020-07-13T07:28:57.716Z",
    "updated": "2020-07-13T07:28:57.716Z"
}
```

#### Get Payment Methods by Customer ID

```python
from xendit import DirectDebit

payment_methods = DirectDebit.get_payment_methods_by_customer_id(
    customer_id="ed20b5db-df04-41fc-8018-8ea4ac4d1030",
)

print(payment_methods)
```

Will return

```
[{
    "id": "pm-b6116aea-8c23-42d0-a1e6-33227b52fccd",
    "customer_id": "ed20b5db-df04-41fc-8018-8ea4ac4d1030",
    "status": "ACTIVE",
    "type": "DEBIT_CARD",
    "properties": {
        "id": "la-fac7e744-ab40-4100-a447-cbbb16f29ded",
        "currency": "IDR",
        "card_expiry": "06/24",
        "description": "",
        "channel_code": "DC_BRI",
        "card_last_four": "8888"
    },
    "metadata": {},
    "created": "2020-07-13T07:28:57.716Z",
    "updated": "2020-07-13T07:28:57.716Z"
}]
```

#### Create Direct Debit Payment

```python
from xendit import DirectDebit

payment = DirectDebit.create_payment(
    reference_id="direct-debit-ref-1594718940",
    payment_method_id="pm-b6116aea-8c23-42d0-a1e6-33227b52fccd",
    currency="IDR",
    amount="60000",
    callback_url="http://webhook.site/",
    enable_otp=True,
    idempotency_key="idemp_key-1594718940",
)

print(payment)
```

Will return

```
{
    "failure_code": null,
    "otp_mobile_number": null,
    "otp_expiration_timestamp": null,
    "id": "ddpy-eaa093b6-b669-401a-ba2e-61ac644b2aff",
    "reference_id": "direct-debit-ref-1594718940",
    "payment_method_id": "pm-b6116aea-8c23-42d0-a1e6-33227b52fccd",
    "channel_code": "DC_BRI",
    "currency": "IDR",
    "amount": 60000,
    "is_otp_required": true,
    "basket": null,
    "description": "",
    "status": "PENDING",
    "metadata": null,
    "created": "2020-07-14T09:29:02.614443Z",
    "updated": "2020-07-14T09:29:02.614443Z"
}
```

#### Create Recurring Payment with Direct Debit

You can use [Create Recurring Payment](#create-recurring-payment) to use this feature.

#### Validate OTP for Direct Debit Payment

```python
from xendit import DirectDebit

payment = DirectDebit.validate_payment_otp(
    direct_debit_id="ddpy-eaa093b6-b669-401a-ba2e-61ac644b2aff",
    otp_code="222000",
)

print(payment)
```

Will return

```
{
    "failure_code": null,
    "otp_mobile_number": null,
    "otp_expiration_timestamp": null,
    "id": "ddpy-eaa093b6-b669-401a-ba2e-61ac644b2aff",
    "reference_id": "direct-debit-ref-1594718940",
    "payment_method_id": "pm-b6116aea-8c23-42d0-a1e6-33227b52fccd",
    "channel_code": "DC_BRI",
    "currency": "IDR",
    "amount": 60000,
    "is_otp_required": true,
    "basket": null,
    "description": "",
    "status": "PENDING",
    "metadata": null,
    "created": "2020-07-14T09:29:02.614443Z",
    "updated": "2020-07-14T09:29:02.614443Z"
}
```

#### Get Direct Debit Payment Status by ID

```python
from xendit import DirectDebit

payment = DirectDebit.get_payment_status(
    direct_debit_id="ddpy-38ef50a8-00f0-4019-8b28-9bca81f2cbf1",
)

print(payment)
```

Will return

```
{
    "failure_code": null,
    "otp_mobile_number": null,
    "otp_expiration_timestamp": null,
    "id": "ddpy-38ef50a8-00f0-4019-8b28-9bca81f2cbf1",
    "reference_id": "direct-debit-ref-1594717458",
    "payment_method_id": "pm-b6116aea-8c23-42d0-a1e6-33227b52fccd",
    "channel_code": "DC_BRI",
    "currency": "IDR",
    "amount": 60000,
    "is_otp_required": false,
    "basket": null,
    "description": "",
    "status": "PENDING",
    "metadata": null,
    "created": "2020-07-14T09:04:20.031451Z",
    "updated": "2020-07-14T09:04:20.031451Z"
}
```

#### Get Direct Debit Payment Status by Reference ID

```python
from xendit import DirectDebit

payments = DirectDebit.get_payment_status_by_ref_id(
    reference_id="direct-debit-ref-1594717458",
)

print(payments)
```

Will return

```
[{
    "amount": 60000,
    "basket": null,
    "channel_code": "DC_BRI",
    "created": "2020-07-14T09:04:20.031451Z",
    "currency": "IDR",
    "description": "",
    "failure_code": null,
    "id": "ddpy-38ef50a8-00f0-4019-8b28-9bca81f2cbf1",
    "is_otp_required": false,
    "metadata": null,
    "otp_expiration_timestamp": null,
    "otp_mobile_number": null,
    "payment_method_id": "pm-b6116aea-8c23-42d0-a1e6-33227b52fccd",
    "reference_id": "direct-debit-ref-1594717458",
    "status": "PENDING",
    "updated": "2020-07-14T09:04:20.031451Z"
}]
```

### Virtual Account Service

#### Create Virtual Account

```python
from xendit import VirtualAccount

virtual_account = VirtualAccount.create(
    external_id="demo_1475459775872",
    bank_code="BNI",
    name="Rika Sutanto",
)
print(virtual_account)
```

Will return

```
{
    "owner_id": "5ed75086a883856178afc12e",
    "external_id": "demo_1475459775872",
    "bank_code": "BNI",
    "merchant_code": "8808",
    "name": "Rika Sutanto",
    "account_number": "8808999956275653",
    "is_single_use": false,
    "status": "PENDING",
    "expiration_date": "2051-06-22T17:00:00.000Z",
    "is_closed": false,
    "id": "5ef174c48dd9ea2fc97d6a1e"
}
```

#### Get Virtual Account Banks
```python
from xendit import VirtualAccount

virtual_account_banks = VirtualAccount.get_banks()
print(virtual_account_banks)
```

Will return

```
[{
    "name": "Bank Mandiri",
    "code": "MANDIRI"
}, {
    "name": "Bank Negara Indonesia",
    "code": "BNI"
}, {
    "name": "Bank Rakyat Indonesia",
    "code": "BRI"
}, {
    "name": "Bank Permata",
    "code": "PERMATA"
}, {
    "name": "Bank Central Asia",
    "code": "BCA"
}]
```
#### Get Virtual Account

```python
from xendit import VirtualAccount

virtual_account = VirtualAccount.get(
    id="5eec3a3e8dd9ea2fc97d6728",
)
print(virtual_account)
```

Will return

```
{
    "owner_id": "5ed75086a883856178afc12e",
    "external_id": "demo_1475459775872",
    "bank_code": "BNI",
    "merchant_code": "8808",
    "name": "Rika Sutanto",
    "account_number": "8808999917965673",
    "is_single_use": true,
    "status": "ACTIVE",
    "expiration_date": "2051-06-18T17:00:00.000Z",
    "is_closed": false,
    "id": "5eec3a3e8dd9ea2fc97d6728"
}
```

#### Update Virtual Account

```python
from xendit import VirtualAccount

virtual_account = VirtualAccount.update(
    id="5eec3a3e8dd9ea2fc97d6728",
    is_single_use=True,
)
print(virtual_account)
```

Will return

```
{
    "owner_id": "5ed75086a883856178afc12e",
    "external_id": "demo_1475459775872",
    "bank_code": "BNI",
    "merchant_code": "8808",
    "name": "Rika Sutanto",
    "account_number": "8808999917965673",
    "is_single_use": true,
    "status": "PENDING",
    "expiration_date": "2051-06-18T17:00:00.000Z",
    "is_closed": false,
    "id": "5eec3a3e8dd9ea2fc97d6728"
}
```

#### Get Virtual Account Payment

```python
from xendit import VirtualAccount

virtual_account_payment = VirtualAccount.get_payment(
    payment_id="5ef18efca7d10d1b4d61fb52",
)
print(virtual_account_payment)
```

Will return

```
{
    "id": "5ef18efcf9ce3b5f8e188ee4",
    "payment_id": "5ef18efca7d10d1b4d61fb52",
    "callback_virtual_account_id": "5ef18ece8dd9ea2fc97d6a84",
    "external_id": "VA_fixed-1592889038",
    "merchant_code": "88608",
    "account_number": "9999317837",
    "bank_code": "MANDIRI",
    "amount": 50000,
    "transaction_timestamp": "2020-06-23T05:11:24.000Z"
}
```

### Retail Outlet Service

#### Create Fixed Payment Code

```python
from xendit import RetailOutlet

retail_outlet = RetailOutlet.create_fixed_payment_code(
    external_id="demo_fixed_payment_code_123",
    retail_outlet_name="ALFAMART",
    name="Rika Sutanto",
    expected_amount=10000,
)
print(retail_outlet)
```

Will return

```
{
    "owner_id": "5ed75086a883856178afc12e",
    "external_id": "demo_fixed_payment_code_123",
    "retail_outlet_name": "ALFAMART",
    "prefix": "TEST",
    "name": "Rika Sutanto",
    "payment_code": "TEST56147",
    "expected_amount": 10000,
    "is_single_use": False,
    "expiration_date": "2051-06-23T17:00:00.000Z",
    "id": "5ef2f0f8e7f5c14077275493",
}
```

#### Update Fixed Payment Code

```python
from xendit import RetailOutlet

retail_outlet = RetailOutlet.update_fixed_payment_code(
    fixed_payment_code_id="5ef2f0f8e7f5c14077275493",
    name="Joe Contini",
)
print(retail_outlet)
```

Will return

```
{
    "owner_id": "5ed75086a883856178afc12e",
    "external_id": "demo_fixed_payment_code_123",
    "retail_outlet_name": "ALFAMART",
    "prefix": "TEST",
    "name": "Joe Contini",
    "payment_code": "TEST56147",
    "expected_amount": 10000,
    "is_single_use": False,
    "expiration_date": "2051-06-23T17:00:00.000Z",
    "id": "5ef2f0f8e7f5c14077275493",
}
```

#### Get Fixed Payment Code

```python
from xendit import RetailOutlet

retail_outlet = RetailOutlet.get_fixed_payment_code(
    fixed_payment_code_id="5ef2f0f8e7f5c14077275493",
)
print(retail_outlet)
```

Will return

```
{
    "owner_id": "5ed75086a883856178afc12e",
    "external_id": "demo_fixed_payment_code_123",
    "retail_outlet_name": "ALFAMART",
    "prefix": "TEST",
    "name": "Rika Sutanto",
    "payment_code": "TEST56147",
    "expected_amount": 10000,
    "is_single_use": False,
    "expiration_date": "2051-06-23T17:00:00.000Z",
    "id": "5ef2f0f8e7f5c14077275493",
}
```

### Invoice Service

#### Create Invoice

```python
from xendit import Invoice

invoice = Invoice.create(
    external_id="invoice-1593684000",
    amount=20000,
    payer_email="customer@domain.com",
    description="Invoice Demo #123",
)
print(invoice)
```

Will return

```
{
    "id": "5efdb0210425db620ec35fb3",
    "external_id": "invoice-1593684000",
    "user_id": "5ed75086a883856178afc12e",
    "status": "PENDING",
    "merchant_name": "Xendit&amp;#x27;s Intern",
    "merchant_profile_picture_url": "https://xnd-companies.s3.amazonaws.com/prod/1591169469152_279.png",
    "amount": 20000,
    "payer_email": "customer@domain.com",
    "description": "Invoice Demo #123",
    "expiry_date": "2020-07-03T10:00:01.148Z",
    "invoice_url": "https://invoice-staging.xendit.co/web/invoices/5efdb0210425db620ec35fb3",
    "available_banks": [
        {
            "bank_code": "MANDIRI",
            "collection_type": "POOL",
            "bank_account_number": "8860846854335",
            "transfer_amount": 20000,
            "bank_branch": "Virtual Account",
            "account_holder_name": "XENDIT&AMP;#X27;S INTERN",
            "identity_amount": 0
        },
        {
            "bank_code": "BRI",
            "collection_type": "POOL",
            "bank_account_number": "2621554807492",
            "transfer_amount": 20000,
            "bank_branch": "Virtual Account",
            "account_holder_name": "XENDIT&AMP;#X27;S INTERN",
            "identity_amount": 0
        },
        {
            "bank_code": "BNI",
            "collection_type": "POOL",
            "bank_account_number": "880854597383",
            "transfer_amount": 20000,
            "bank_branch": "Virtual Account",
            "account_holder_name": "XENDIT&AMP;#X27;S INTERN",
            "identity_amount": 0
        },
        {
            "bank_code": "PERMATA",
            "collection_type": "POOL",
            "bank_account_number": "821456659745",
            "transfer_amount": 20000,
            "bank_branch": "Virtual Account",
            "account_holder_name": "XENDIT&AMP;#X27;S INTERN",
            "identity_amount": 0
        },
        {
            "bank_code": "BCA",
            "collection_type": "POOL",
            "bank_account_number": "1076619844859",
            "transfer_amount": 20000,
            "bank_branch": "Virtual Account",
            "account_holder_name": "XENDIT&AMP;#X27;S INTERN",
            "identity_amount": 0
        }
    ],
    "available_retail_outlets": [
        {
            "retail_outlet_name": "ALFAMART",
            "payment_code": "TEST34956",
            "transfer_amount": 20000
        }
    ],
    "available_ewallets": [],
    "should_exclude_credit_card": false,
    "should_send_email": false,
    "created": "2020-07-02T10:00:01.285Z",
    "updated": "2020-07-02T10:00:01.285Z",
    "currency": "IDR"
}
```

#### Get Invoice

```python
from xendit import Invoice

invoice = Invoice.get(
    invoice_id="5efda8a20425db620ec35f43",
)
print(invoice)
```

Will return

```
{
    "id": "5efda8a20425db620ec35f43",
    "external_id": "invoice-1593682080",
    "user_id": "5ed75086a883856178afc12e",
    "status": "EXPIRED",
    "merchant_name": "Xendit&amp;#x27;s Intern",
    "merchant_profile_picture_url": "https://xnd-companies.s3.amazonaws.com/prod/1591169469152_279.png",
    "amount": 20000,
    "payer_email": "customer@domain.com",
    "description": "Invoice Demo #123",
    "expiry_date": "2020-07-02T09:55:47.794Z",
    "invoice_url": "https://invoice-staging.xendit.co/web/invoices/5efda8a20425db620ec35f43",
    "available_banks": [
        {
            "bank_code": "MANDIRI",
            "collection_type": "POOL",
            "bank_account_number": "8860846853111",
            "transfer_amount": 20000,
            "bank_branch": "Virtual Account",
            "account_holder_name": "XENDIT&AMP;#X27;S INTERN",
            "identity_amount": 0
        },
        {
            "bank_code": "BRI",
            "collection_type": "POOL",
            "bank_account_number": "2621554806292",
            "transfer_amount": 20000,
            "bank_branch": "Virtual Account",
            "account_holder_name": "XENDIT&AMP;#X27;S INTERN",
            "identity_amount": 0
        }
    ],
    "available_retail_outlets": [
        {
            "retail_outlet_name": "ALFAMART",
            "payment_code": "TEST34950",
            "transfer_amount": 20000
        }
    ],
    "available_ewallets": [],
    "should_exclude_credit_card": false,
    "should_send_email": false,
    "created": "2020-07-02T09:28:02.191Z",
    "updated": "2020-07-02T09:55:47.794Z",
    "currency": "IDR"
}
```

#### Expire Invoice

```python
from xendit import Invoice

invoice = Invoice.expire(
    invoice_id="5efda8a20425db620ec35f43",
)
print(invoice)
```

Will return

```
{
    "id": "5efda8a20425db620ec35f43",
    "external_id": "invoice-1593682080",
    "user_id": "5ed75086a883856178afc12e",
    "status": "EXPIRED",
    "merchant_name": "Xendit&amp;#x27;s Intern",
    "merchant_profile_picture_url": "https://xnd-companies.s3.amazonaws.com/prod/1591169469152_279.png",
    "amount": 20000,
    "payer_email": "customer@domain.com",
    "description": "Invoice Demo #123",
    "expiry_date": "2020-07-02T09:55:47.794Z",
    "invoice_url": "https://invoice-staging.xendit.co/web/invoices/5efda8a20425db620ec35f43",
    "available_banks": [
        {
            "bank_code": "MANDIRI",
            "collection_type": "POOL",
            "bank_account_number": "8860846853111",
            "transfer_amount": 20000,
            "bank_branch": "Virtual Account",
            "account_holder_name": "XENDIT&AMP;#X27;S INTERN",
            "identity_amount": 0
        },
        {
            "bank_code": "BRI",
            "collection_type": "POOL",
            "bank_account_number": "2621554806292",
            "transfer_amount": 20000,
            "bank_branch": "Virtual Account",
            "account_holder_name": "XENDIT&AMP;#X27;S INTERN",
            "identity_amount": 0
        }
    "available_retail_outlets": [
        {
            "retail_outlet_name": "ALFAMART",
            "payment_code": "TEST34950",
            "transfer_amount": 20000
        }
    ],
    "available_ewallets": [],
    "should_exclude_credit_card": false,
    "should_send_email": false,
    "created": "2020-07-02T09:28:02.191Z",
    "updated": "2020-07-02T09:55:47.794Z",
    "currency": "IDR"
}
```

#### List All Invoice

```python
from xendit import Invoice

invoices = Invoice.list_all(
    limit=3,
)
print(invoices)
```

Will return

```
[
    ...
    {
        "id": "5efda8a20425db620ec35f43",
        "external_id": "invoice-1593682080",
        "user_id": "5ed75086a883856178afc12e",
        "status": "EXPIRED",
        "merchant_name": "Xendit&amp;#x27;s Intern",
        "merchant_profile_picture_url": "https://xnd-companies.s3.amazonaws.com/prod/1591169469152_279.png",
        "amount": 20000,
        "payer_email": "customer@domain.com",
        "description": "Invoice Demo #123",
        "expiry_date": "2020-07-02T09:55:47.794Z",
        "invoice_url": "https://invoice-staging.xendit.co/web/invoices/5efda8a20425db620ec35f43",
        "available_banks": [
            {
                "bank_code": "MANDIRI",
                "collection_type": "POOL",
                "bank_account_number": "8860846853111",
                "transfer_amount": 20000,
                "bank_branch": "Virtual Account",
                "account_holder_name": "XENDIT&AMP;#X27;S INTERN",
                "identity_amount": 0
            },
            {
                "bank_code": "BRI",
                "collection_type": "POOL",
                "bank_account_number": "2621554806292",
                "transfer_amount": 20000,
                "bank_branch": "Virtual Account",
                "account_holder_name": "XENDIT&AMP;#X27;S INTERN",
                "identity_amount": 0
            }
        "available_retail_outlets": [
            {
                "retail_outlet_name": "ALFAMART",
                "payment_code": "TEST34950",
                "transfer_amount": 20000
            }
        ],
        "available_ewallets": [],
        "should_exclude_credit_card": false,
        "should_send_email": false,
        "created": "2020-07-02T09:28:02.191Z",
        "updated": "2020-07-02T09:55:47.794Z",
        "currency": "IDR"
    }
    ...
]
```

### Recurring Payment Service

#### Create Recurring Payment

```python
from xendit import RecurringPayment

recurring_payment = RecurringPayment.create(
    external_id="recurring_12345",
    payer_email="test@x.co",
    description="Test Curring Payment",
    amount=100000,
    interval="MONTH",
    interval_count=1,
)
print(recurring_payment)
```

Will return

```
{
    "status": "ACTIVE",
    "should_send_email": false,
    "missed_payment_action": "IGNORE",
    "recurrence_progress": 1,
    "recharge": true,
    "user_id": "5ed75086a883856178afc12e",
    "external_id": "recurring_12345",
    "payer_email": "test@x.co",
    "description": "Test Curring Payment",
    "amount": 100000,
    "interval": "MONTH",
    "interval_count": 1,
    "start_date": "2020-07-08T08:22:55.815Z",
    "currency": "IDR",
    "created": "2020-07-08T08:22:55.817Z",
    "updated": "2020-07-08T08:22:55.994Z",
    "id": "5f05825ff9f52d3ed204c687",
    "last_created_invoice_url": "https://invoice-staging.xendit.co/web/invoices/5f05825ff9f52d3ed204c688"
}
```

#### Get Recurring Payment

```python
from xendit import RecurringPayment

recurring_payment = RecurringPayment.get(
    id="5f05825ff9f52d3ed204c687",
)
print(recurring_payment)
```

Will return

```
{
    "status": "ACTIVE",
    "should_send_email": false,
    "missed_payment_action": "IGNORE",
    "recurrence_progress": 1,
    "recharge": true,
    "user_id": "5ed75086a883856178afc12e",
    "external_id": "recurring_12345",
    "payer_email": "test@x.co",
    "description": "Test Curring Payment",
    "amount": 100000,
    "interval": "MONTH",
    "interval_count": 1,
    "start_date": "2020-07-08T08:22:55.815Z",
    "currency": "IDR",
    "created": "2020-07-08T08:22:55.817Z",
    "updated": "2020-07-08T08:22:55.994Z",
    "id": "5f05825ff9f52d3ed204c687",
    "last_created_invoice_url": "https://invoice-staging.xendit.co/web/invoices/5f05825ff9f52d3ed204c688"
}
```

#### Edit Recurring Payment

```python
from xendit import RecurringPayment

recurring_payment = RecurringPayment.edit(
    id="5f05825ff9f52d3ed204c687",
    interval_count=2,
)
print(recurring_payment)
```

Will return

```
{
    "status": "ACTIVE",
    "should_send_email": false,
    "missed_payment_action": "IGNORE",
    "recurrence_progress": 1,
    "recharge": true,
    "user_id": "5ed75086a883856178afc12e",
    "external_id": "recurring_12345",
    "payer_email": "test@x.co",
    "description": "Test Curring Payment",
    "amount": 100000,
    "interval": "MONTH",
    "interval_count": 2,
    "start_date": "2020-07-08T08:22:55.815Z",
    "currency": "IDR",
    "created": "2020-07-08T08:22:55.817Z",
    "updated": "2020-07-08T08:24:58.295Z",
    "id": "5f05825ff9f52d3ed204c687"
}
```

#### Stop Recurring Payment

```python
from xendit import RecurringPayment

recurring_payment = RecurringPayment.stop(
    id="5f05825ff9f52d3ed204c687",
)
print(recurring_payment)
```

Will return

```
{
    "status": "STOPPED",
    "should_send_email": false,
    "missed_payment_action": "IGNORE",
    "recurrence_progress": 1,
    "recharge": true,
    "user_id": "5ed75086a883856178afc12e",
    "external_id": "recurring_12345",
    "payer_email": "test@x.co",
    "description": "Test Curring Payment",
    "amount": 100000,
    "interval": "MONTH",
    "interval_count": 2,
    "start_date": "2020-07-08T08:22:55.815Z",
    "currency": "IDR",
    "created": "2020-07-08T08:22:55.817Z",
    "updated": "2020-07-08T08:26:32.464Z",
    "id": "5f05825ff9f52d3ed204c687"
}
```

#### Pause Recurring Payment

```python
from xendit import RecurringPayment

recurring_payment = RecurringPayment.pause(
    id="5f05825ff9f52d3ed204c687",
)
print(recurring_payment)
```

Will return

```
{
    "status": "PAUSED",
    "should_send_email": false,
    "missed_payment_action": "IGNORE",
    "recurrence_progress": 1,
    "recharge": true,
    "user_id": "5ed75086a883856178afc12e",
    "external_id": "recurring_12345",
    "payer_email": "test@x.co",
    "description": "Test Curring Payment",
    "amount": 100000,
    "interval": "MONTH",
    "interval_count": 2,
    "start_date": "2020-07-08T08:22:55.815Z",
    "currency": "IDR",
    "created": "2020-07-08T08:22:55.817Z",
    "updated": "2020-07-08T08:25:44.580Z",
    "id": "5f05825ff9f52d3ed204c687"
}
```

#### Resume Recurring Payment

```python
from xendit import RecurringPayment

recurring_payment = RecurringPayment.resume(
    id="5f05825ff9f52d3ed204c687",
)
print(recurring_payment)
```

Will return

```
{
    "status": "ACTIVE",
    "should_send_email": false,
    "missed_payment_action": "IGNORE",
    "recurrence_progress": 1,
    "recharge": true,
    "user_id": "5ed75086a883856178afc12e",
    "external_id": "recurring_12345",
    "payer_email": "test@x.co",
    "description": "Test Curring Payment",
    "amount": 100000,
    "interval": "MONTH",
    "interval_count": 2,
    "start_date": "2020-07-08T08:22:55.815Z",
    "currency": "IDR",
    "created": "2020-07-08T08:22:55.817Z",
    "updated": "2020-07-08T08:26:03.082Z",
    "id": "5f05825ff9f52d3ed204c687"
}
```

### Payout Service

#### Create Payout

```python
from xendit import Payout

payout = Payout.create(
    external_id="payout-1595405117",
    amount=50000,
    email="test@email.co",
)
print(payout)
```

Will return

```
{
    "id": "a6ee1bf1-ffcd-4bda-a7ab-99c1d5cd0472",
    "external_id": "payout-1595405117",
    "amount": 50000,
    "merchant_name": "Xendit&amp;#x27;s Intern",
    "status": "PENDING",
    "expiration_timestamp": "2020-07-23T08:05:19.815Z",
    "created": "2020-07-22T08:05:18.421Z",
    "email": "test@email.co",
    "payout_url": "https://payout-staging.xendit.co/web/a6ee1bf1-ffcd-4bda-a7ab-99c1d5cd0472"
}
```

#### Get Payout

```python
from xendit import Payout

payout = Payout.get(
    id="a6ee1bf1-ffcd-4bda-a7ab-99c1d5cd0472",
)
print(payout)
```

Will return

```
{
    "id": "a6ee1bf1-ffcd-4bda-a7ab-99c1d5cd0472",
    "external_id": "payout-1595405117",
    "amount": 50000,
    "merchant_name": "Xendit&amp;#x27;s Intern",
    "status": "PENDING",
    "expiration_timestamp": "2020-07-23T08:05:19.815Z",
    "created": "2020-07-22T08:05:18.421Z",
    "email": "test@email.co",
    "payout_url": "https://payout-staging.xendit.co/web/a6ee1bf1-ffcd-4bda-a7ab-99c1d5cd0472"
}
```

#### Void a Payout

```python
from xendit import Payout

payout = Payout.void(
    id="a6ee1bf1-ffcd-4bda-a7ab-99c1d5cd0472",
)
print(payout)
```

Will return

```
{
    "id": "a6ee1bf1-ffcd-4bda-a7ab-99c1d5cd0472",
    "external_id": "payout-1595405117",
    "amount": 50000,
    "merchant_name": "Xendit&amp;#x27;s Intern",
    "status": "VOIDED",
    "expiration_timestamp": "2020-07-23T08:05:19.815Z",
    "created": "2020-07-22T08:05:18.421Z",
    "email": "test@email.co"
}
```

### Disbursement Service

#### Create Disbursement

```python
from xendit import Disbursement

disbursement = Disbursement.create(
    external_id="demo_1475459775872",
    bank_code="BCA",
    account_holder_name="Bob Jones",
    account_number="1231242311",
    description="Reimbursement for shoes",
    amount=17000,
)
print(disbursement)
```

Will return

```
{
    "user_id": "5ed75086a883856178afc12e",
    "external_id": "demo_1475459775872",
    "amount": 17000,
    "bank_code": "BCA",
    "account_holder_name": "Bob Jones",
    "disbursement_description": "Reimbursement for shoes",
    "status": "PENDING",
    "id": "5ef1c4f40c2e150017ce3b96",
}
```

#### Get Disbursement by ID

```python
from xendit import Disbursement

disbursement = Disbursement.get(
    id="5ef1befeecb16100179e1d05",
)
print(disbursement)
```

Will return

```
{
    "user_id": "5ed75086a883856178afc12e",
    "external_id": "demo_1475459775872",
    "amount": 17000,
    "bank_code": "BCA",
    "account_holder_name": "Bob Jones",
    "disbursement_description": "Disbursement from Postman",
    "status": "PENDING",
    "id": "5ef1befeecb16100179e1d05"
}
```

#### Get Disbursement by External ID

```python
from xendit import Disbursement

disbursement_list = Disbursement.get_by_ext_id(
    external_id="demo_1475459775872",
)
print(disbursement_list)

```

Will return

```
[
    {
        "user_id": "5ed75086a883856178afc12e",
        "external_id": "demo_1475459775872",
        "amount": 17000,
        "bank_code": "BCA",
        "account_holder_name": "Bob Jones",
        "disbursement_description": "Reimbursement for shoes",
        "status": "PENDING",
        "id": "5ef1c4f40c2e150017ce3b96",
    },
    {
        "user_id": "5ed75086a883856178afc12e",
        "external_id": "demo_1475459775872",
        "amount": 17000,
        "bank_code": "BCA",
        "account_holder_name": "Bob Jones",
        "disbursement_description": "Disbursement from Postman",
        "status": "PENDING",
        "id": "5ef1befeecb16100179e1d05",
    },
    ...
]
```
#### Get Available Banks

```python
from xendit import Disbursement

disbursement_banks = Disbursement.get_available_banks()
print(disbursement_banks)
```

Will return

```
[
    ...
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
    }
]
```

### Batch Disbursement Service

#### Create Batch Disbursement

```python
from xendit import BatchDisbursement

batch_disbursement_items = []
batch_disbursement_items.append(
    BatchDisbursement.helper_create_batch_item(
        amount=10000,
        bank_code="BCA",
        bank_account_name="Adyaksa W",
        bank_account_number="12345678",
        description="Sample Batch Disbursement",
        external_id=f"batch-disbursement-item-12345"
    )
)
batch_disbursement = BatchDisbursement.create(
    reference="batch_disbursement-1595326225",
    disbursements=batch_disbursement_items,
)
print(batch_disbursement)
```

Will return

```
{
    "status": "UPLOADING",
    "reference": "batch_disbursement-1595326225",
    "total_uploaded_amount": 10000,
    "total_uploaded_count": 1,
    "created": "2020-07-21T10:10:35.782Z",
    "id": "5f16bf1bfc70de0017b858bf"
}
```

#### Get Batch Disbursement Available Banks

You can use [Get Available Banks](#get-available-banks) to use this feature.

### xenPlatform Service

#### Create Account

```python
from xendit import XenPlatform, XenPlatformAccountType

xenplatform_account = XenPlatform.create_account(
    account_email="test-xenplatform@pythonxendit.co",
    type=XenPlatformAccountType.OWNED,
    business_profile={'business_name': 'python-xendit'},
)
print(xenplatform_account)
```

Will return

```
{
    "account_email": "test-xenplatform@pythonxendit.co",
    "user_id": "5f2132ed172cd67992c402d6",
    "created": "2020-07-29T08:27:25.346Z",
    "status": "SUCCESSFUL",
    "type": "OWNED"
}
```

#### Set Callback URLs

```python
from xendit import XenPlatform, XenPlatformURLType

xenplatform_callback_url = XenPlatform.set_callback_url(
    type=XenPlatformURLType.INVOICE,
    url="https://test-url-invoice.com",
)
print(xenplatform_callback_url)
```

Will return

```
{
    "status": "SUCCESSFUL",
    "user_id": "5e6b30d967627b957de8c123",
    "url": "https://test-url-invoice.com",
    "environment": "TEST",
    "callback_token": "66a6680348e1c33ed2b9053a8eb9291b9e2230ff4f4d3057c9f4ac26405d2123"
}
```

#### Transfers

```python
from xendit import XenPlatform

xenplatform_transfers = XenPlatform.transfers(
    reference="transfer001",
    amount=10000,
    source_user_id="54afeb170a2b18519b1b8768",
    destination_user_id="5cafeb170a2b1851246b8768",
)
print(xenplatform_transfers)
```

Will return

```
{
    "created": "2020-01-01T08:51:44.484Z",
    "transfer_id": "60b9d810-d9a3-456c-abbf-2786ec7a9651",
    "reference": "transfer001",
    "source_user_id": "54afeb170a2b18519b1b8768",
    "destination_user_id": "5cafeb170a2b1851246b8768",
    "status": "SUCCESSFUL",
    "amount": 10000
}
```

## Contributing

For any requests, bugs, or comments, please open an [issue](https://github.com/xendit/xendit-python/issues) or [submit a pull request](https://github.com/xendit/xendit-python/pulls).

To start developing on this repository, you need to have Poetry installed for package dependency. After that, you can run ```poetry install``` to install the dependency. To enter the environment, run ```poetry shell```

### Tests

#### Running the Test

Make sure the the code passes all tests.

Run the test:

```
python -m pytest tests/
```

Run with coverage:

```
python -m pytest tests/ --cov=xendit/
```