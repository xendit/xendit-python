# TransactionApi


You can use the APIs below to interface with Xendit's `TransactionApi`.
To start using the API, you need to configure the secret key and initiate the client instance.

```python
import time
import xendit
from xendit.apis import TransactionApi

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')

# Enter a context with an instance of the API client
api_client = xendit.ApiClient()

# Create an instance of the API class
api_instance = TransactionApi(api_client)
```

All URIs are relative to *https://api.xendit.co*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**get_transaction_by_id**](TransactionApi.md#get_transaction_by_id-function) | **GET** /transactions/{id} | Get a transaction based on its id |
| [**get_all_transactions**](TransactionApi.md#get_all_transactions-function) | **GET** /transactions | Get a list of transactions |


# `get_transaction_by_id()` Function
> TransactionResponse get_transaction_by_id(id)

Get a transaction based on its id

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `get_transaction_by_id` |
| Request Parameters  |  [GetTransactionByIdRequestParams](#request-parameters--GetTransactionByIdRequestParams)	 |
| Return Type  | [**TransactionResponse**](balance_and_transaction/TransactionResponse.md) |

### Request Parameters - GetTransactionByIdRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **id** | **TransactionId** | ☑️ | |
| **for_user_id** | **str**| |  |

### Usage Example
```python
import time
import xendit
from xendit.apis import TransactionApi
from xendit.balance_and_transaction.model.transaction_response import TransactionResponse
from xendit.balance_and_transaction.model.server_error import ServerError
from xendit.balance_and_transaction.model.validation_error import ValidationError
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = TransactionApi(api_client)
id = TransactionId("txn_438e4b61-7c4c-4dbb-bbba-94a896bff333") # TransactionId 
for_user_id = "5dbf20d7c8eb0c0896f811b6" # str | The sub-account user-id that you want to make this transaction for. This header is only used if you have access to xenPlatform. See xenPlatform for more information

# example passing only required values which don't have defaults set
try:
    # Get a transaction based on its id
    api_response = api_instance.get_transaction_by_id(id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling TransactionApi->get_transaction_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get a transaction based on its id
    api_response = api_instance.get_transaction_by_id(id, for_user_id=for_user_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling TransactionApi->get_transaction_by_id: %s\n" % e)
```

# `get_all_transactions()` Function
> TransactionsResponse get_all_transactions()

Get a list of transactions

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `get_all_transactions` |
| Request Parameters  |  [GetAllTransactionsRequestParams](#request-parameters--GetAllTransactionsRequestParams)	 |
| Return Type  | [**TransactionsResponse**](balance_and_transaction/TransactionsResponse.md) |

### Request Parameters - GetAllTransactionsRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **for_user_id** | **str**| |  |
| **types** | [**[TransactionTypes]**](balance_and_transaction/TransactionTypes.md)| |  |
| **statuses** | [**[TransactionStatuses]**](balance_and_transaction/TransactionStatuses.md)| |  |
| **channel_categories** | [**[ChannelsCategories]**](balance_and_transaction/ChannelsCategories.md)| |  |
| **reference_id** | **str**| |  |
| **product_id** | **str**| |  |
| **account_identifier** | **str**| |  |
| **amount** | **float**| |  |
| **currency** | **Currency**| |  |
| **created** | **DateRangeFilter**| |  |
| **updated** | **DateRangeFilter**| |  |
| **limit** | **float**| | 10 |
| **after_id** | **TransactionId**| |  |
| **before_id** | **TransactionId**| |  |

### Usage Example
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
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = TransactionApi(api_client)
for_user_id = "5dbf20d7c8eb0c0896f811b6" # str | The sub-account user-id that you want to make this transaction for. This header is only used if you have access to xenPlatform. See xenPlatform for more information
types = [
        TransactionTypes("["DISBURSEMENT","PAYMENT"]"),
    ] # [TransactionTypes] | Transaction types that will be included in the result. Default is to include all transaction types
statuses = [
        TransactionStatuses("["SUCCESS","PENDING"]"),
    ] # [TransactionStatuses] | Status of the transaction. Default is to include all status.
channel_categories = [
        ChannelsCategories("["BANK","INVOICE"]"),
    ] # [ChannelsCategories] | Payment channels in which the transaction is carried out. Default is to include all channels.
reference_id = "ref23232" # str | To filter the result for transactions with matching reference given (case sensitive)
product_id = "d290f1ee-6c54-4b01-90e6-d701748f0701" # str | To filter the result for transactions with matching product_id (a.k.a payment_id) given (case sensitive)
account_identifier = "123123123" # str | Account identifier of transaction. The format will be different from each channel. For example, on `BANK` channel it will be account number and on `CARD` it will be masked card number.
amount = 100 # float | Specific transaction amount to search for
currency = Currency("IDR") # Currency 
created = DateRangeFilter(
        gte=dateutil_parser('2020-08-29T17:00:00Z'),
        lte=dateutil_parser('2020-08-29T17:00:00Z'),
    ) # DateRangeFilter | Filter time of transaction by created date. If not specified will list all dates.
updated = DateRangeFilter(
        gte=dateutil_parser('2020-08-29T17:00:00Z'),
        lte=dateutil_parser('2020-08-29T17:00:00Z'),
    ) # DateRangeFilter | Filter time of transaction by updated date. If not specified will list all dates.
limit = 10 # float | number of items in the result per page. Another name for \"results_per_page\"
after_id = TransactionId("txn_438e4b61-7c4c-4dbb-bbba-94a896bff333") # TransactionId 
before_id = TransactionId("txn_438e4b61-7c4c-4dbb-bbba-94a896bff333") # TransactionId 

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get a list of transactions
    api_response = api_instance.get_all_transactions(for_user_id=for_user_id, types=types, statuses=statuses, channel_categories=channel_categories, reference_id=reference_id, product_id=product_id, account_identifier=account_identifier, amount=amount, currency=currency, created=created, updated=updated, limit=limit, after_id=after_id, before_id=before_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling TransactionApi->get_all_transactions: %s\n" % e)
```

[[Back to README]](../README.md)
