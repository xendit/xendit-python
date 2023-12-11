![Xendit Python SDK](images/header.jpg "Xendit Python SDK")

# Xendit Python SDK

The official Xendit Python SDK provides a simple and convenient way to call Xendit's REST API
in applications written in Python.

* Package version: 4.1.0

## Requirements

Python >= 3.10

# Getting Started

## Installation

Install directly from Xendit's Github Repository:

```sh
pip install git+https://github.com/xendit/xendit-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/xendit/xendit-python.git`)

Then import the package:
```python
import xendit
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import xendit
```

## Authorization

The SDK needs to be instantiated using your secret API key obtained from the [Xendit Dashboard](https://dashboard.xendit.co/settings/developers#api-keys).
You can sign up for a free Dashboard account [here](https://dashboard.xendit.co/register).

```python
import xendit
from xendit.apis import BalanceApi
from pprint import pprint

xendit.set_api_key('XENDIT_API_KEY')

client = xendit.ApiClient()

try:
    response = BalanceApi(client).get_balance('CASH')
    pprint(response)
except xendit.XenditSdkException as e:
    print("Exception when calling BalanceApi->get_balance: %s\n" % e)
```

# Documentation

Find detailed API information and examples for each of our product's by clicking the links below,

* [Invoice](docs/InvoiceApi.md)
* [PaymentRequest](docs/PaymentRequestApi.md)
* [PaymentMethod](docs/PaymentMethodApi.md)
* [Refund](docs/RefundApi.md)
* [Balance](docs/BalanceApi.md)
* [Transaction](docs/TransactionApi.md)
* [Customer](docs/CustomerApi.md)
* [Payout](docs/PayoutApi.md)

All URIs are relative to *https://api.xendit.co*.  For more information about our API, please refer to *https://developers.xendit.co/*.

Further Reading

* [Xendit Docs](https://docs.xendit.co/)
* [Xendit API Reference](https://developers.xendit.co/)