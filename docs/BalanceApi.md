# BalanceApi


You can use the APIs below to interface with Xendit's `BalanceApi`.
To start using the API, you need to configure the secret key and initiate the client instance.

```python
import time
import xendit
from xendit.apis import BalanceApi

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')

# Enter a context with an instance of the API client
api_client = xendit.ApiClient()

# Create an instance of the API class
api_instance = BalanceApi(api_client)
```

All URIs are relative to *https://api.xendit.co*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**get_balance**](BalanceApi.md#get_balance-function) | **GET** /balance | Retrieves balances for a business, default to CASH type |


# `get_balance()` Function
> Balance get_balance()

Retrieves balances for a business, default to CASH type

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `get_balance` |
| Request Parameters  |  [GetBalanceRequestParams](#request-parameters--GetBalanceRequestParams)	 |
| Return Type  | [**Balance**](balance_and_transaction/Balance.md) |

### Request Parameters - GetBalanceRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **account_type** | **str**| | "CASH" |
| **currency** | **str**| |  |
| **for_user_id** | **str**| |  |

### Usage Example
```python
import time
import xendit
from xendit.apis import BalanceApi
from xendit.balance_and_transaction.model.server_error import ServerError
from xendit.balance_and_transaction.model.validation_error import ValidationError
from xendit.balance_and_transaction.model.balance import Balance
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = BalanceApi(api_client)
account_type = "CASH" # str | The selected balance type
currency = "IDR" # str | Currency for filter for customers with multi currency accounts
for_user_id = "5dbf20d7c8eb0c0896f811b6" # str | The sub-account user-id that you want to make this transaction for. This header is only used if you have access to xenPlatform. See xenPlatform for more information

# example passing only required values which don't have defaults set
# and optional values
try:
    # Retrieves balances for a business, default to CASH type
    api_response = api_instance.get_balance(account_type=account_type, currency=currency, for_user_id=for_user_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling BalanceApi->get_balance: %s\n" % e)
```

[[Back to README]](../README.md)
