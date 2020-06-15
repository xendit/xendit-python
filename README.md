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
    - [Balance Service](#balance-service)
      - [Get Balance](#get-balance)
  - [Contributing](#contributing)
    - [Tests](#tests)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## API Documentation
Please check [Xendit API Reference](https://xendit.github.io/apireference/).

## Requirements

Python 3.7 or later

## Installation

To use the package, run ```pip install xendit-python```

## Usage

### Balance Service

#### Get Balance

The `account_type` parameter is optional.

```python
Balance.get()

Balance.get(account_type)
```

Usage example:

```python
Balance balance = Balance.get("CASH")
print(balance)
``` 

## Contributing

For any requests, bugs, or comments, please open an [issue](https://github.com/xendit/xendit-python/issues) or [submit a pull request](https://github.com/xendit/xendit-python/pulls).

To start developing on this repository, you need to have Poetry installed for package dependency. After that, you can run ```poetry install``` to install the dependency. To enter the environment, run ```poetry shell```

### Tests

Make sure the the code passes all tests.

Run the test:

```
python -m pytest tests/
```

Run with coverage:

```
python -m pytest tests/ --cov=xendit/
```