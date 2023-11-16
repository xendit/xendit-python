# PayoutApi


You can use the APIs below to interface with Xendit's `PayoutApi`.
To start using the API, you need to configure the secret key and initiate the client instance.

```python
import time
import xendit
from xendit.apis import PayoutApi

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')

# Enter a context with an instance of the API client
api_client = xendit.ApiClient()

# Create an instance of the API class
api_instance = PayoutApi(api_client)
```

All URIs are relative to *https://api.xendit.co*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**create_payout**](PayoutApi.md#create_payout-function) | **POST** /v2/payouts | API to send money at scale to bank accounts &amp; eWallets |
| [**get_payout_by_id**](PayoutApi.md#get_payout_by_id-function) | **GET** /v2/payouts/{id} | API to fetch the current status, or details of the payout |
| [**get_payout_channels**](PayoutApi.md#get_payout_channels-function) | **GET** /payouts_channels | API providing the current list of banks and e-wallets we support for payouts for both regions |
| [**get_payouts**](PayoutApi.md#get_payouts-function) | **GET** /v2/payouts | API to retrieve all matching payouts with reference ID |
| [**cancel_payout**](PayoutApi.md#cancel_payout-function) | **POST** /v2/payouts/{id}/cancel | API to cancel requested payouts that have not yet been sent to partner banks and e-wallets. Cancellation is possible if the payout has not been sent out via our partner and when payout status is ACCEPTED. |


# `create_payout()` Function
> GetPayouts200ResponseDataInner create_payout(idempotency_key)

API to send money at scale to bank accounts & eWallets

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `create_payout` |
| Request Parameters  |  [CreatePayoutRequestParams](#request-parameters--CreatePayoutRequestParams)	 |
| Return Type  | [**GetPayouts200ResponseDataInner**](payout/GetPayouts200ResponseDataInner.md) |

### Request Parameters - CreatePayoutRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **idempotency_key** | **str** | ☑️ | |
| **for_user_id** | **str**| |  |
| **create_payout_request** | [**CreatePayoutRequest**](payout/CreatePayoutRequest.md)| |  |

### Usage Example
#### Bank or EWallet Payout

```python
import time
import xendit
from xendit.apis import PayoutApi
from xendit.payout.model.create_payout_request import CreatePayoutRequest
from xendit.payout.model.get_payouts200_response_data_inner import GetPayouts200ResponseDataInner
from xendit.payout.model.error import Error
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PayoutApi(api_client)
idempotency_key = "DISB-1234" # str | A unique key to prevent duplicate requests from pushing through our system. No expiration.
for_user_id = "5f9a3fbd571a1c4068aa40ce" # str | The sub-account user-id that you want to make this transaction for. This header is only used if you have access to xenPlatform. See xenPlatform for more information.
create_payout_request = {
  "reference_id" : "DISB-001",
  "currency" : "PHP",
  "channel_code" : "PH_BDO",
  "channel_properties" : {
    "account_holder_name" : "John Doe",
    "account_number" : "000000"
  },
  "amount" : 90000,
  "description" : "Test Bank Payout",
  "type" : "DIRECT_DISBURSEMENT"
} # CreatePayoutRequest 

# example passing only required values which don't have defaults set
try:
    # API to send money at scale to bank accounts & eWallets
    api_response = api_instance.create_payout(idempotency_key)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PayoutApi->create_payout: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # API to send money at scale to bank accounts & eWallets
    api_response = api_instance.create_payout(idempotency_key, for_user_id=for_user_id, create_payout_request=create_payout_request)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PayoutApi->create_payout: %s\n" % e)
```

# `get_payout_by_id()` Function
> GetPayouts200ResponseDataInner get_payout_by_id(id)

API to fetch the current status, or details of the payout

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `get_payout_by_id` |
| Request Parameters  |  [GetPayoutByIdRequestParams](#request-parameters--GetPayoutByIdRequestParams)	 |
| Return Type  | [**GetPayouts200ResponseDataInner**](payout/GetPayouts200ResponseDataInner.md) |

### Request Parameters - GetPayoutByIdRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **id** | **str** | ☑️ | |
| **for_user_id** | **str**| |  |

### Usage Example
```python
import time
import xendit
from xendit.apis import PayoutApi
from xendit.payout.model.get_payouts200_response_data_inner import GetPayouts200ResponseDataInner
from xendit.payout.model.error import Error
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PayoutApi(api_client)
id = "disb-7baa7335-a0b2-4678-bb8c-318c0167f332" # str | Payout id returned from the response of /v2/payouts
for_user_id = "5f9a3fbd571a1c4068aa40ce" # str | The sub-account user-id that you want to make this transaction for. This header is only used if you have access to xenPlatform. See xenPlatform for more information.

# example passing only required values which don't have defaults set
try:
    # API to fetch the current status, or details of the payout
    api_response = api_instance.get_payout_by_id(id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PayoutApi->get_payout_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # API to fetch the current status, or details of the payout
    api_response = api_instance.get_payout_by_id(id, for_user_id=for_user_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PayoutApi->get_payout_by_id: %s\n" % e)
```

# `get_payout_channels()` Function
> [Channel] get_payout_channels()

API providing the current list of banks and e-wallets we support for payouts for both regions

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `get_payout_channels` |
| Request Parameters  |  [GetPayoutChannelsRequestParams](#request-parameters--GetPayoutChannelsRequestParams)	 |
| Return Type  | [**[Channel]**](payout/Channel.md) |

### Request Parameters - GetPayoutChannelsRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **currency** | **str**| |  |
| **channel_category** | [**[ChannelCategory]**](payout/ChannelCategory.md)| |  |
| **channel_code** | **str**| |  |
| **for_user_id** | **str**| |  |

### Usage Example
```python
import time
import xendit
from xendit.apis import PayoutApi
from xendit.payout.model.error import Error
from xendit.payout.model.channel_category import ChannelCategory
from xendit.payout.model.channel import Channel
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PayoutApi(api_client)
currency = "IDR, PHP" # str | Filter channels by currency from ISO-4217 values
channel_category = [
        ChannelCategory("BANK"),
    ] # [ChannelCategory] | Filter channels by category
channel_code = "ID_MANDIRI, PH_GCASH" # str | Filter channels by channel code, prefixed by ISO-3166 country code
for_user_id = "5f9a3fbd571a1c4068aa40ce" # str | The sub-account user-id that you want to make this transaction for. This header is only used if you have access to xenPlatform. See xenPlatform for more information.

# example passing only required values which don't have defaults set
# and optional values
try:
    # API providing the current list of banks and e-wallets we support for payouts for both regions
    api_response = api_instance.get_payout_channels(currency=currency, channel_category=channel_category, channel_code=channel_code, for_user_id=for_user_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PayoutApi->get_payout_channels: %s\n" % e)
```

# `get_payouts()` Function
> GetPayouts200Response get_payouts(reference_id)

API to retrieve all matching payouts with reference ID

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `get_payouts` |
| Request Parameters  |  [GetPayoutsRequestParams](#request-parameters--GetPayoutsRequestParams)	 |
| Return Type  | [**GetPayouts200Response**](payout/GetPayouts200Response.md) |

### Request Parameters - GetPayoutsRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **reference_id** | **str** | ☑️ | |
| **limit** | **float**| |  |
| **after_id** | **str**| |  |
| **before_id** | **str**| |  |
| **for_user_id** | **str**| |  |

### Usage Example
```python
import time
import xendit
from xendit.apis import PayoutApi
from xendit.payout.model.error import Error
from xendit.payout.model.get_payouts200_response import GetPayouts200Response
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PayoutApi(api_client)
reference_id = "DISB-123" # str | Reference_id provided when creating the payout
limit = 10 # float | Number of records to fetch per API call
after_id = "disb-7baa7335-a0b2-4678-bb8c-318c0167f332" # str | Used to fetch record after this payout unique id
before_id = "disb-7baa7335-a0b2-4678-bb8c-318c0167f332" # str | Used to fetch record before this payout unique id
for_user_id = "5f9a3fbd571a1c4068aa40ce" # str | The sub-account user-id that you want to make this transaction for. This header is only used if you have access to xenPlatform. See xenPlatform for more information.

# example passing only required values which don't have defaults set
try:
    # API to retrieve all matching payouts with reference ID
    api_response = api_instance.get_payouts(reference_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PayoutApi->get_payouts: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # API to retrieve all matching payouts with reference ID
    api_response = api_instance.get_payouts(reference_id, limit=limit, after_id=after_id, before_id=before_id, for_user_id=for_user_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PayoutApi->get_payouts: %s\n" % e)
```

# `cancel_payout()` Function
> GetPayouts200ResponseDataInner cancel_payout(id)

API to cancel requested payouts that have not yet been sent to partner banks and e-wallets. Cancellation is possible if the payout has not been sent out via our partner and when payout status is ACCEPTED.

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `cancel_payout` |
| Request Parameters  |  [CancelPayoutRequestParams](#request-parameters--CancelPayoutRequestParams)	 |
| Return Type  | [**GetPayouts200ResponseDataInner**](payout/GetPayouts200ResponseDataInner.md) |

### Request Parameters - CancelPayoutRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **id** | **str** | ☑️ | |
| **for_user_id** | **str**| |  |

### Usage Example
```python
import time
import xendit
from xendit.apis import PayoutApi
from xendit.payout.model.get_payouts200_response_data_inner import GetPayouts200ResponseDataInner
from xendit.payout.model.error import Error
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PayoutApi(api_client)
id = "disb-7baa7335-a0b2-4678-bb8c-318c0167f332" # str | Payout id returned from the response of /v2/payouts
for_user_id = "5f9a3fbd571a1c4068aa40ce" # str | The sub-account user-id that you want to make this transaction for. This header is only used if you have access to xenPlatform. See xenPlatform for more information.

# example passing only required values which don't have defaults set
try:
    # API to cancel requested payouts that have not yet been sent to partner banks and e-wallets. Cancellation is possible if the payout has not been sent out via our partner and when payout status is ACCEPTED.
    api_response = api_instance.cancel_payout(id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PayoutApi->cancel_payout: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # API to cancel requested payouts that have not yet been sent to partner banks and e-wallets. Cancellation is possible if the payout has not been sent out via our partner and when payout status is ACCEPTED.
    api_response = api_instance.cancel_payout(id, for_user_id=for_user_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PayoutApi->cancel_payout: %s\n" % e)
```

[[Back to README]](../README.md)
