# xendit.apis.TransactionApi

All URIs are relative to *https://api.xendit.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_transactions**](TransactionApi.md#get_all_transactions) | **GET** /transactions | Get a list of transactions
[**get_transaction_by_id**](TransactionApi.md#get_transaction_by_id) | **GET** /transactions/{id} | Get a transaction based on its id


# **get_all_transactions**
> TransactionsResponse get_all_transactions()

Get a list of transactions

Get a list of all transactions based on filter and search parameters.

### Example


```python
import time
import xendit
from xendit.apis import TransactionApi
from xendit.balance_and_transaction.model.transaction_statuses import TransactionStatuses
from xendit.balance_and_transaction.model.server_error import ServerError
from xendit.balance_and_transaction.model.transaction_types import TransactionTypes
from xendit.balance_and_transaction.model.date_range_filter import DateRangeFilter
from xendit.balance_and_transaction.model.channels_categories import ChannelsCategories
from xendit.balance_and_transaction.model.transactions_response import TransactionsResponse
from xendit.balance_and_transaction.model.validation_error import ValidationError
from xendit.balance_and_transaction.model.currency import Currency
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = xendit.Configuration(
    api_key = 'XENDIT API KEY'
)


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = TransactionApi(api_client)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get a list of transactions
    api_response = api_instance.get_all_transactions(for_user_id=for_user_id, types=types, statuses=statuses, channel_categories=channel_categories, reference_id=reference_id, product_id=product_id, account_identifier=account_identifier, amount=amount, currency=currency, created=created, updated=updated, limit=limit, after_id=after_id, before_id=before_id)
    pprint(api_response)
except xendit.ApiException as e:
    print("Exception when calling TransactionApi->get_all_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **for_user_id** | **str**| The sub-account user-id that you want to make this transaction for. This header is only used if you have access to xenPlatform. See xenPlatform for more information | [optional]
 **types** | [**[TransactionTypes]**](TransactionTypes.md)| Transaction types that will be included in the result. Default is to include all transaction types | [optional]
 **statuses** | [**[TransactionStatuses]**](TransactionStatuses.md)| Status of the transaction. Default is to include all status. | [optional]
 **channel_categories** | [**[ChannelsCategories]**](ChannelsCategories.md)| Payment channels in which the transaction is carried out. Default is to include all channels. | [optional]
 **reference_id** | **str**| To filter the result for transactions with matching reference given (case sensitive) | [optional]
 **product_id** | **str**| To filter the result for transactions with matching product_id (a.k.a payment_id) given (case sensitive) | [optional]
 **account_identifier** | **str**| Account identifier of transaction. The format will be different from each channel. For example, on &#x60;BANK&#x60; channel it will be account number and on &#x60;CARD&#x60; it will be masked card number. | [optional]
 **amount** | **float**| Specific transaction amount to search for | [optional]
 **currency** | **Currency**|  | [optional]
 **created** | **DateRangeFilter**| Filter time of transaction by created date. If not specified will list all dates. | [optional]
 **updated** | **DateRangeFilter**| Filter time of transaction by updated date. If not specified will list all dates. | [optional]
 **limit** | **float**| number of items in the result per page. Another name for \&quot;results_per_page\&quot; | [optional] if omitted the server will use the default value of 10
 **after_id** | **TransactionId**|  | [optional]
 **before_id** | **TransactionId**|  | [optional]

### Return type

[**TransactionsResponse**](TransactionsResponse.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of transaction object |  -  |
**400** | invalid input, object invalid |  -  |
**0** | Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_by_id**
> TransactionResponse get_transaction_by_id(id)

Get a transaction based on its id

Get single specific transaction by transaction id.

### Example


```python
import time
import xendit
from xendit.apis import TransactionApi
from xendit.balance_and_transaction.model.transaction_response import TransactionResponse
from xendit.balance_and_transaction.model.server_error import ServerError
from xendit.balance_and_transaction.model.validation_error import ValidationError
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = xendit.Configuration(
    api_key = 'XENDIT API KEY'
)


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = TransactionApi(api_client)
id = TransactionId("txn_438e4b61-7c4c-4dbb-bbba-94a896bff333") # TransactionId | 

# example passing only required values which don't have defaults set
try:
    # Get a transaction based on its id
    api_response = api_instance.get_transaction_by_id(id)
    pprint(api_response)
except xendit.ApiException as e:
    print("Exception when calling TransactionApi->get_transaction_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get a transaction based on its id
    api_response = api_instance.get_transaction_by_id(id, for_user_id=for_user_id)
    pprint(api_response)
except xendit.ApiException as e:
    print("Exception when calling TransactionApi->get_transaction_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **TransactionId**|  |
 **for_user_id** | **str**| The sub-account user-id that you want to make this transaction for. This header is only used if you have access to xenPlatform. See xenPlatform for more information | [optional]

### Return type

[**TransactionResponse**](TransactionResponse.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | invalid input, object invalid |  -  |
**0** | Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

