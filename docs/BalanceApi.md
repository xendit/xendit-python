# xendit.apis.BalanceApi

All URIs are relative to *https://api.xendit.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_balance**](BalanceApi.md#get_balance) | **GET** /balance | Retrieves balances for a business, default to CASH type


# **get_balance**
> Balance get_balance()

Retrieves balances for a business, default to CASH type

Retrieves balance for your business, defaults to CASH type

### Example


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

# example passing only required values which don't have defaults set
# and optional values
try:
    # Retrieves balances for a business, default to CASH type
    api_response = api_instance.get_balance(account_type=account_type, currency=currency, for_user_id=for_user_id)
    pprint(api_response)
except xendit.ApiException as e:
    print("Exception when calling BalanceApi->get_balance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_type** | **str**| The selected balance type | [optional] if omitted the server will use the default value of "CASH"
 **currency** | **str**| Currency for filter for customers with multi currency accounts | [optional]
 **for_user_id** | **str**| The sub-account user-id that you want to make this transaction for. This header is only used if you have access to xenPlatform. See xenPlatform for more information | [optional]

### Return type

[**Balance**](Balance.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**400** | invalid input, object invalid |  -  |
**0** | Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

