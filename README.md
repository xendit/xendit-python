![Xendit Python SDK](docs/header.jpg "Xendit Pyton SDK")

# Xendit Python SDK

The official Xendit Python SDK provides a simple and convenient way to call Xendit's REST API
in applications written in Python.

* Package version: 3.0.0-beta.2

## Requirements.

Python >=3.6

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
from xendit.apis import BalancesApi
from pprint import pprint

xendit.set_api_key('XENDIT_API_KEY')

client = xendit.ApiClient()

try:
    response = BalancesApi(client).get_balance('CASH')
    pprint(response)
except xendit.ApiException as e:
    print("Exception when calling BalancesApi->get_balance: %s\n" % e)
```

# Documentation

Find detailed API infomration and examples for each of our product's by clicking the links below,

* [Balance](docs/BalanceApi.md)
* [Invoice](docs/InvoiceApi.md)
* [PaymentMethod](docs/PaymentMethodApi.md)
* [PaymentRequest](docs/PaymentRequestApi.md)
* [Payout](docs/PayoutApi.md)
* [Refund](docs/RefundApi.md)
* [Transaction](docs/TransactionApi.md)

All URIs are relative to *https://api.xendit.co*.  For more information about our API, please refer to *https://developers.xendit.co/*.

Further Reading

* [Xendit Docs](https://docs.xendit.co/)
* [Xendit API Reference](https://developers.xendit.co/)