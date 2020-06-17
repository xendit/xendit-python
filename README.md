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
    - [Balance Service](#balance-service)
      - [Get Balance](#get-balance)
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
b = x.Balance
b.get()
```

### Balance Service

#### Get Balance

The `account_type` parameter is optional.

```python
from xendit import Balance
Balance.get()

Balance.get(Balance.AccountType)
```

Usage example:

```python
from xendit import Balance
Balance balance = Balance.get(Balance.AccountType.CASH)

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

To create your own HTTP Client, you can do it by implementing interface at `xendit/network/http_client_interface.py`. Our default HTTP Client are wrapper of [requests](https://github.com/psf/requests), which can be found at `xendit/network/xendit_http_client.py`. To attach it to your instance, add it to your xendit parameter.

```python
import xendit

xendit_instance =  xendit.Xendit(api_key='', http_client=YourHTTPClientClass)
```
