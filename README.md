# Xendit Python Library

This library is the abstraction of Xendit API for access from applications written with Python.

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Xendit Python Library](#xendit-python-library)
  - [Table of Contents](#table-of-contents)
  - [API Documentation](#api-documentation)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
    - [API Key](#api-key)
      - [Global Variable](#global-variable)
      - [Use Xendit Instance](#use-xendit-instance)
    - [Headers](#headers)
    - [Balance Service](#balance-service)
      - [Get Balance](#get-balance)
    - [Credit Card](#credit-card)
      - [Create Authorization](#create-authorization)
      - [Reverse Authorization](#reverse-authorization)
      - [Create Charge](#create-charge)
      - [Capture Charge](#capture-charge)
      - [Get Charge](#get-charge)
      - [Create Refund](#create-refund)
      - [Get Charge Option](#get-charge-option)
      - [Create Promotion](#create-promotion)
      - [Get Promotion](#get-promotion)
      - [Get Promotion Calculation](#get-promotion-calculation)
    - [eWallets](#ewallets)
      - [Create OVO Payment](#create-ovo-payment)
      - [Create DANA Payment](#create-dana-payment)
      - [Create LinkAja Payment](#create-linkaja-payment)
      - [Get Payment Status](#get-payment-status)
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
    - [Disbursement Service](#disbursement-service)
      - [Create Disbursement](#create-disbursement)
      - [Get Disbursement by ID](#get-disbursement-by-id)
      - [Get Disbursement by External ID](#get-disbursement-by-external-id)
      - [Get Available Banks](#get-available-banks)
  - [Contributing](#contributing)
    - [Tests](#tests)
      - [Running the Test](#running-the-test)
      - [Creating Custom HTTP Client](#creating-custom-http-client)

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
from xendit import Balance
Balance balance = Balance.AccountType(
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

### Credit Card

#### Create Authorization

```python
from xendit import CreditCard

charge = CreditCard.create_authorization(
    token_id="5f0338e800406a0019a8cfac",
    external_id="card_preAuth-1594047446",
    amount=75000,
    card_cvn="123",
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
    "merchant_reference_code": "5f0338e8a5f876f0f4cad03f",
    "external_id": "card_preAuth-1594047446",
    "eci": "05",
    "charge_type": "SINGLE_USE_TOKEN",
    "masked_card_number": "400000XXXXXX0002",
    "card_brand": "VISA",
    "card_type": "CREDIT",
    "descriptor": "XENDIT*XENDIT&AMP;#X27;S INTERN",
    "bank_reconciliation_id": "5940474534726103203010",
    "approval_code": "831000",
    "created": "2020-07-06T14:57:33.509Z",
    "id": "5f033bdd00406a0019a8cfc0"
}
```

#### Reverse Authorization

```python
from xendit import CreditCard

reverse_authorization = CreditCard.reverse_authorizatiton(
    credit_card_charge_id="5f033bdd00406a0019a8cfc0",
    external_id="reverse-authorization-1594047638",
)
print(reverse_authorization)
```

Will return

```
{
    "status": "SUCCEEDED",
    "currency": "IDR",
    "credit_card_charge_id": "5f033bdd00406a0019a8cfc0",
    "business_id": "5ed75086a883856178afc12e",
    "external_id": "card_preAuth-1594047446",
    "amount": 75000,
    "created": "2020-07-06T15:00:41.313Z",
    "id": "5f033c9900406a0019a8cfc4"
}
```

#### Create Charge

#### Capture Charge

#### Get Charge

#### Create Refund

#### Get Charge Option

#### Create Promotion

#### Get Promotion

#### Get Promotion Calculation

### eWallets

#### Create OVO Payment

```python
from xendit import EWallet

ovo_payment = EWallet.create_ovo_payment(
    external_id="ovo-ewallet-testing-id-1593663430",
    amount="80001",
    phone="08123123123",
)
print(ovo_payment)
```

Will return

```
{
    "amount": 80001,
    "business_id": "5ed75086a883856178afc12e",
    "external_id": "ovo-ewallet-testing-id-1593663430",
    "ewallet_type": "OVO",
    "phone": "08123123123",
    "created": "2020-07-02T04:17:12.979Z",
    "status": "PENDING"
}
```

#### Create DANA Payment

```python
from xendit import EWallet

dana_payment = EWallet.create_dana_payment(
    external_id="dana-ewallet-test-1593663447",
    amount="1001",
    callback_url="https://my-shop.com/callbacks",
    redirect_url="https://my-shop.com/home",
)
print(dana_payment)
```

Will return

```
{
    "external_id": "dana-ewallet-test-1593663447",
    "amount": 1001,
    "checkout_url": "https://sandbox.m.dana.id/m/portal/cashier/checkout?bizNo=20200702111212800110166820100550620&timestamp=1593663450389&mid=216620000000261692328&sign=XS3FMKj1oZHkTWu0EXk8PBwzjR1VtwSedqbKX%2BgMF6CyZvbA5xhAmMUR%2FlhD4QkBODbbTPcju1YDFnHmSdzmjbqPfGcQGtkCPgLwVOZo1ERPmoUhhGJIbQXkfZ1Z8eA1w1RSqDzdmDB%2B%2FlvHaTbYPiUlvjzs%2BfgkM33YFFEl0BG1kUFz0%2FKb9OoT1QKyoHxw6ge4SWPF3Po6BwNtjqUZe2n43s7y0CvSrcNiNLHT3k2XHSlIdguwCGjNHh2zClgtv9XbSCecnD96nuIuohYARX8Ai%2BaYo%2FEDO1VEch4XditfIXvyBhL0TocxhYxda7yKNNjkZj56Rl9ds8u7Wyv1eQ%3D%3D",
    "ewallet_type": "DANA"
}
```

#### Create LinkAja Payment

```python
from xendit import EWallet, LinkAjaItem

items = []
items.append(LinkAjaItem(id="123123", name="Phone Case", price=100000, quantity=1))
linkaja_payment = EWallet.create_linkaja_payment(
    external_id="linkaja-ewallet-test-1593663498",
    phone="089911111111",
    items=items,
    amount=300000,
    callback_url="https://my-shop.com/callbacks",
    redirect_url="https://xendit.co/",
)
print(linkaja_payment)
```

Will return

```
{
    "checkout_url": "https://ewallet-linkaja-dev.xendit.co/checkouts/c627cf1f-0470-420f-a0f4-3931ef384bf4",
    "transaction_date": "2020-07-02T04:18:21.729Z",
    "amount": 300000,
    "external_id": "linkaja-ewallet-test-1593663498",
    "ewallet_type": "LINKAJA"
}
```

#### Get Payment Status

```python
from xendit import EWallet

ovo_payment_status = EWallet.get_payment_status(
    ewallet_type=EWalletType.OVO,
    external_id="ovo-ewallet-testing-id-1234",
)
print(ovo_payment_status)
```

Will return

```
{
    "amount": "8888",
    "business_id": "5ed75086a883856178afc12e",
    "ewallet_type": "OVO",
    "external_id": "ovo-ewallet-testing-id-1234",
    "status": "COMPLETED",
    "transaction_date": "2020-06-30T01:32:28.267Z"
}
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

virtual_account_payment = VirtualAccount.get(
    payment_id="5ef18efca7d10d1b4d61fb52",
)
print(virtual_account)
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

#### Creating Custom HTTP Client

To create your own HTTP Client, you can do it by implementing interface at `xendit/network/http_client_interface.py`. Our default HTTP Client are wrapper of [requests](https://github.com/psf/requests), which can be found at `xendit/network/_xendit_http_client.py`. To attach it to your instance, add it to your xendit parameter.

```python
import xendit

xendit_instance =  xendit.Xendit(api_key='', http_client=YourHTTPClientClass)
```
