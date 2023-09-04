# xendit.apis.PayoutApi

All URIs are relative to *https://api.xendit.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_payout**](PayoutApi.md#cancel_payout) | **POST** /v2/payouts/{id}/cancel | API to cancel requested payouts that have not yet been sent to partner banks and e-wallets. Cancellation is possible if the payout has not been sent out via our partner and when payout status is ACCEPTED.
[**create_payout**](PayoutApi.md#create_payout) | **POST** /v2/payouts | API to send money at scale to bank accounts &amp; eWallets
[**get_payout_by_id**](PayoutApi.md#get_payout_by_id) | **GET** /v2/payouts/{id} | API to fetch the current status, or details of the payout
[**get_payout_channels**](PayoutApi.md#get_payout_channels) | **GET** /payouts_channels | API providing the current list of banks and e-wallets we support for payouts for both regions
[**get_payouts**](PayoutApi.md#get_payouts) | **GET** /v2/payouts | API to retrieve all matching payouts with reference ID


# **cancel_payout**
> GetPayouts200ResponseDataInner cancel_payout(id)

API to cancel requested payouts that have not yet been sent to partner banks and e-wallets. Cancellation is possible if the payout has not been sent out via our partner and when payout status is ACCEPTED.

### Example


```python
import time
import xendit
from xendit.apis import PayoutApi
from xendit.payout.model.get_payouts200_response_data_inner import GetPayouts200ResponseDataInner
from xendit.payout.model.error import Error
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = xendit.Configuration(
    api_key = 'XENDIT API KEY'
)


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PayoutApi(api_client)
id = "disb-7baa7335-a0b2-4678-bb8c-318c0167f332" # str | Payout id returned from the response of /v2/payouts

# example passing only required values which don't have defaults set
try:
    # API to cancel requested payouts that have not yet been sent to partner banks and e-wallets. Cancellation is possible if the payout has not been sent out via our partner and when payout status is ACCEPTED.
    api_response = api_instance.cancel_payout(id)
    pprint(api_response)
except xendit.ApiException as e:
    print("Exception when calling PayoutApi->cancel_payout: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payout id returned from the response of /v2/payouts |

### Return type

[**GetPayouts200ResponseDataInner**](GetPayouts200ResponseDataInner.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cancelled Successfully |  -  |
**400** | Unable to Cancel |  -  |
**404** | Invalid Payout ID |  -  |
**0** | Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payout**
> GetPayouts200ResponseDataInner create_payout(idempotency_key)

API to send money at scale to bank accounts & eWallets

### Example


```python
import time
import xendit
from xendit.apis import PayoutApi
from xendit.payout.model.create_payout_request import CreatePayoutRequest
from xendit.payout.model.get_payouts200_response_data_inner import GetPayouts200ResponseDataInner
from xendit.payout.model.error import Error
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = xendit.Configuration(
    api_key = 'XENDIT API KEY'
)


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PayoutApi(api_client)
idempotency_key = "DISB-1234" # str | A unique key to prevent duplicate requests from pushing through our system. No expiration.

# example passing only required values which don't have defaults set
try:
    # API to send money at scale to bank accounts & eWallets
    api_response = api_instance.create_payout(idempotency_key)
    pprint(api_response)
except xendit.ApiException as e:
    print("Exception when calling PayoutApi->create_payout: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # API to send money at scale to bank accounts & eWallets
    api_response = api_instance.create_payout(idempotency_key, for_user_id=for_user_id, create_payout_request=create_payout_request)
    pprint(api_response)
except xendit.ApiException as e:
    print("Exception when calling PayoutApi->create_payout: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique key to prevent duplicate requests from pushing through our system. No expiration. |
 **for_user_id** | **str**| The sub-account user-id that you want to make this transaction for. This header is only used if you have access to xenPlatform. See xenPlatform for more information. | [optional]
 **create_payout_request** | [**CreatePayoutRequest**](CreatePayoutRequest.md)|  | [optional]

### Return type

[**GetPayouts200ResponseDataInner**](GetPayouts200ResponseDataInner.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created payout |  -  |
**400** | Error when creating payout, see error_code for more details |  -  |
**401** | Invalid API key |  -  |
**403** | API key in use does not have necessary permissions to perform the request. Please assign proper permissions for the key. |  -  |
**409** | Duplicate Error, payout already exists |  -  |
**0** | Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payout_by_id**
> GetPayouts200ResponseDataInner get_payout_by_id(id)

API to fetch the current status, or details of the payout

### Example


```python
import time
import xendit
from xendit.apis import PayoutApi
from xendit.payout.model.get_payouts200_response_data_inner import GetPayouts200ResponseDataInner
from xendit.payout.model.error import Error
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = xendit.Configuration(
    api_key = 'XENDIT API KEY'
)


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PayoutApi(api_client)
id = "disb-7baa7335-a0b2-4678-bb8c-318c0167f332" # str | Payout id returned from the response of /v2/payouts

# example passing only required values which don't have defaults set
try:
    # API to fetch the current status, or details of the payout
    api_response = api_instance.get_payout_by_id(id)
    pprint(api_response)
except xendit.ApiException as e:
    print("Exception when calling PayoutApi->get_payout_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payout id returned from the response of /v2/payouts |

### Return type

[**GetPayouts200ResponseDataInner**](GetPayouts200ResponseDataInner.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Payout object |  -  |
**401** | Invalid API key |  -  |
**403** | API key in use does not have necessary permissions to perform the request. Please assign proper permissions for the key. |  -  |
**404** | Payout Not Found |  -  |
**0** | Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payout_channels**
> [Channel] get_payout_channels()

API providing the current list of banks and e-wallets we support for payouts for both regions

### Example


```python
import time
import xendit
from xendit.apis import PayoutApi
from xendit.payout.model.error import Error
from xendit.payout.model.channel_category import ChannelCategory
from xendit.payout.model.channel import Channel
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = xendit.Configuration(
    api_key = 'XENDIT API KEY'
)


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PayoutApi(api_client)

# example passing only required values which don't have defaults set
# and optional values
try:
    # API providing the current list of banks and e-wallets we support for payouts for both regions
    api_response = api_instance.get_payout_channels(currency=currency, channel_category=channel_category, channel_code=channel_code)
    pprint(api_response)
except xendit.ApiException as e:
    print("Exception when calling PayoutApi->get_payout_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Filter channels by currency from ISO-4217 values | [optional]
 **channel_category** | [**[ChannelCategory]**](ChannelCategory.md)| Filter channels by category | [optional]
 **channel_code** | **str**| Filter channels by channel code, prefixed by ISO-3166 country code | [optional]

### Return type

[**[Channel]**](Channel.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current list of banks and e-wallets supported for payouts for all regions |  -  |
**0** | Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payouts**
> GetPayouts200Response get_payouts(reference_id)

API to retrieve all matching payouts with reference ID

### Example


```python
import time
import xendit
from xendit.apis import PayoutApi
from xendit.payout.model.error import Error
from xendit.payout.model.get_payouts200_response import GetPayouts200Response
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = xendit.Configuration(
    api_key = 'XENDIT API KEY'
)


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PayoutApi(api_client)
reference_id = "DISB-123" # str | Reference_id provided when creating the payout

# example passing only required values which don't have defaults set
try:
    # API to retrieve all matching payouts with reference ID
    api_response = api_instance.get_payouts(reference_id)
    pprint(api_response)
except xendit.ApiException as e:
    print("Exception when calling PayoutApi->get_payouts: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # API to retrieve all matching payouts with reference ID
    api_response = api_instance.get_payouts(reference_id, limit=limit, after_id=after_id, before_id=before_id)
    pprint(api_response)
except xendit.ApiException as e:
    print("Exception when calling PayoutApi->get_payouts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_id** | **str**| Reference_id provided when creating the payout |
 **limit** | **float**| Number of records to fetch per API call | [optional]
 **after_id** | **str**| Used to fetch record after this payout unique id | [optional]
 **before_id** | **str**| Used to fetch record before this payout unique id | [optional]

### Return type

[**GetPayouts200Response**](GetPayouts200Response.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of Payout objects sorted by created time in desc order. \&quot;data\&quot; will be an empty array and \&quot;has_more&#39; will be equal to false when there are no matching data. |  -  |
**403** | API key in use does not have necessary permissions to perform the request. Please assign proper permissions for the key. |  -  |
**0** | Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

