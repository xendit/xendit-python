# xendit.apis.PaymentMethodApi

All URIs are relative to *https://api.xendit.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_payment_method**](PaymentMethodApi.md#auth_payment_method) | **POST** /v2/payment_methods/{paymentMethodId}/auth | Validate a payment method&#39;s linking OTP
[**create_payment_method**](PaymentMethodApi.md#create_payment_method) | **POST** /v2/payment_methods | Creates payment method
[**expire_payment_method**](PaymentMethodApi.md#expire_payment_method) | **POST** /v2/payment_methods/{paymentMethodId}/expire | Expires a payment method
[**get_all_payment_channels**](PaymentMethodApi.md#get_all_payment_channels) | **GET** /v2/payment_methods/channels | Get all payment channels
[**get_all_payment_methods**](PaymentMethodApi.md#get_all_payment_methods) | **GET** /v2/payment_methods | Get all payment methods by filters
[**get_payment_method_by_id**](PaymentMethodApi.md#get_payment_method_by_id) | **GET** /v2/payment_methods/{paymentMethodId} | Get payment method by ID
[**get_payments_by_payment_method_id**](PaymentMethodApi.md#get_payments_by_payment_method_id) | **GET** /v2/payment_methods/{paymentMethodId}/payments | Returns payments with matching PaymentMethodID.
[**patch_payment_method**](PaymentMethodApi.md#patch_payment_method) | **PATCH** /v2/payment_methods/{paymentMethodId} | Patch payment methods
[**simulate_payment**](PaymentMethodApi.md#simulate_payment) | **POST** /v2/payment_methods/{paymentMethodId}/payments/simulate | Makes payment with matching PaymentMethodID.


# **auth_payment_method**
> PaymentMethod auth_payment_method(payment_method_id)

Validate a payment method's linking OTP

This endpoint validates a payment method linking OTP

### Example


```python
import time
import xendit
from xendit.apis import PaymentMethodApi
from xendit.payment_method.model.get_all_payment_methods403_response import GetAllPaymentMethods403Response
from xendit.payment_method.model.get_all_payment_methods400_response import GetAllPaymentMethods400Response
from xendit.payment_method.model.get_all_payment_methods404_response import GetAllPaymentMethods404Response
from xendit.payment_method.model.create_payment_method503_response import CreatePaymentMethod503Response
from xendit.payment_method.model.payment_method import PaymentMethod
from xendit.payment_method.model.create_payment_method409_response import CreatePaymentMethod409Response
from xendit.payment_method.model.payment_method_auth_parameters import PaymentMethodAuthParameters
from xendit.payment_method.model.get_all_payment_methods_default_response import GetAllPaymentMethodsDefaultResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = xendit.Configuration(
    api_key = 'XENDIT API KEY'
)


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentMethodApi(api_client)
payment_method_id = "pm-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str | 

# example passing only required values which don't have defaults set
try:
    # Validate a payment method's linking OTP
    api_response = api_instance.auth_payment_method(payment_method_id)
    pprint(api_response)
except xendit.ApiException as e:
    print("Exception when calling PaymentMethodApi->auth_payment_method: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Validate a payment method's linking OTP
    api_response = api_instance.auth_payment_method(payment_method_id, payment_method_auth_parameters=payment_method_auth_parameters)
    pprint(api_response)
except xendit.ApiException as e:
    print("Exception when calling PaymentMethodApi->auth_payment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**|  |
 **payment_method_auth_parameters** | [**PaymentMethodAuthParameters**](PaymentMethodAuthParameters.md)|  | [optional]

### Return type

[**PaymentMethod**](PaymentMethod.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful |  -  |
**400** | Bad request |  -  |
**403** | Forbidden due to permissions |  -  |
**404** | Data not found |  -  |
**409** | Request causes conflict |  -  |
**503** | Service is unavailable due to dependencies |  -  |
**0** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payment_method**
> PaymentMethod create_payment_method()

Creates payment method

This endpoint initiates creation of payment method

### Example


```python
import time
import xendit
from xendit.apis import PaymentMethodApi
from xendit.payment_method.model.get_all_payment_methods403_response import GetAllPaymentMethods403Response
from xendit.payment_method.model.get_all_payment_methods400_response import GetAllPaymentMethods400Response
from xendit.payment_method.model.get_all_payment_methods404_response import GetAllPaymentMethods404Response
from xendit.payment_method.model.create_payment_method503_response import CreatePaymentMethod503Response
from xendit.payment_method.model.payment_method_parameters import PaymentMethodParameters
from xendit.payment_method.model.payment_method import PaymentMethod
from xendit.payment_method.model.create_payment_method409_response import CreatePaymentMethod409Response
from xendit.payment_method.model.get_all_payment_methods_default_response import GetAllPaymentMethodsDefaultResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = xendit.Configuration(
    api_key = 'XENDIT API KEY'
)


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentMethodApi(api_client)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Creates payment method
    api_response = api_instance.create_payment_method(payment_method_parameters=payment_method_parameters)
    pprint(api_response)
except xendit.ApiException as e:
    print("Exception when calling PaymentMethodApi->create_payment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_parameters** | [**PaymentMethodParameters**](PaymentMethodParameters.md)|  | [optional]

### Return type

[**PaymentMethod**](PaymentMethod.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Request successful |  -  |
**400** | Bad request |  -  |
**403** | Forbidden due to permissions |  -  |
**404** | Data not found |  -  |
**409** | Request causes conflict |  -  |
**503** | Service is unavailable due to dependencies |  -  |
**0** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **expire_payment_method**
> PaymentMethod expire_payment_method(payment_method_id)

Expires a payment method

This endpoint expires a payment method and performs unlinking if necessary

### Example


```python
import time
import xendit
from xendit.apis import PaymentMethodApi
from xendit.payment_method.model.get_all_payment_methods403_response import GetAllPaymentMethods403Response
from xendit.payment_method.model.get_all_payment_methods400_response import GetAllPaymentMethods400Response
from xendit.payment_method.model.get_all_payment_methods404_response import GetAllPaymentMethods404Response
from xendit.payment_method.model.create_payment_method503_response import CreatePaymentMethod503Response
from xendit.payment_method.model.payment_method import PaymentMethod
from xendit.payment_method.model.get_all_payment_methods_default_response import GetAllPaymentMethodsDefaultResponse
from xendit.payment_method.model.payment_method_expire_parameters import PaymentMethodExpireParameters
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = xendit.Configuration(
    api_key = 'XENDIT API KEY'
)


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentMethodApi(api_client)
payment_method_id = "pm-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str | 

# example passing only required values which don't have defaults set
try:
    # Expires a payment method
    api_response = api_instance.expire_payment_method(payment_method_id)
    pprint(api_response)
except xendit.ApiException as e:
    print("Exception when calling PaymentMethodApi->expire_payment_method: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Expires a payment method
    api_response = api_instance.expire_payment_method(payment_method_id, payment_method_expire_parameters=payment_method_expire_parameters)
    pprint(api_response)
except xendit.ApiException as e:
    print("Exception when calling PaymentMethodApi->expire_payment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**|  |
 **payment_method_expire_parameters** | [**PaymentMethodExpireParameters**](PaymentMethodExpireParameters.md)|  | [optional]

### Return type

[**PaymentMethod**](PaymentMethod.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful |  -  |
**400** | Bad request |  -  |
**403** | Forbidden due to permissions |  -  |
**404** | Data not found |  -  |
**503** | Service is unavailable due to dependencies |  -  |
**0** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_payment_channels**
> PaymentChannelList get_all_payment_channels()

Get all payment channels

Get all payment channels

### Example


```python
import time
import xendit
from xendit.apis import PaymentMethodApi
from xendit.payment_method.model.get_all_payment_methods403_response import GetAllPaymentMethods403Response
from xendit.payment_method.model.get_all_payment_methods400_response import GetAllPaymentMethods400Response
from xendit.payment_method.model.payment_channel_list import PaymentChannelList
from xendit.payment_method.model.get_all_payment_methods_default_response import GetAllPaymentMethodsDefaultResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = xendit.Configuration(
    api_key = 'XENDIT API KEY'
)


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentMethodApi(api_client)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get all payment channels
    api_response = api_instance.get_all_payment_channels(is_activated=is_activated, type=type)
    pprint(api_response)
except xendit.ApiException as e:
    print("Exception when calling PaymentMethodApi->get_all_payment_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_activated** | **bool**|  | [optional] if omitted the server will use the default value of True
 **type** | **str**|  | [optional]

### Return type

[**PaymentChannelList**](PaymentChannelList.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful |  -  |
**400** | Bad request |  -  |
**403** | Forbidden due to permissions |  -  |
**0** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_payment_methods**
> PaymentMethodList get_all_payment_methods()

Get all payment methods by filters

Get all payment methods by filters

### Example


```python
import time
import xendit
from xendit.apis import PaymentMethodApi
from xendit.payment_method.model.get_all_payment_methods403_response import GetAllPaymentMethods403Response
from xendit.payment_method.model.payment_method_status import PaymentMethodStatus
from xendit.payment_method.model.payment_method_reusability import PaymentMethodReusability
from xendit.payment_method.model.get_all_payment_methods400_response import GetAllPaymentMethods400Response
from xendit.payment_method.model.get_all_payment_methods404_response import GetAllPaymentMethods404Response
from xendit.payment_method.model.get_all_payment_methods_default_response import GetAllPaymentMethodsDefaultResponse
from xendit.payment_method.model.payment_method_list import PaymentMethodList
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = xendit.Configuration(
    api_key = 'XENDIT API KEY'
)


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentMethodApi(api_client)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get all payment methods by filters
    api_response = api_instance.get_all_payment_methods(id=id, type=type, status=status, reusability=reusability, customer_id=customer_id, reference_id=reference_id, after_id=after_id, before_id=before_id, limit=limit)
    pprint(api_response)
except xendit.ApiException as e:
    print("Exception when calling PaymentMethodApi->get_all_payment_methods: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **[str]**|  | [optional]
 **type** | **[str]**|  | [optional]
 **status** | [**[PaymentMethodStatus]**](PaymentMethodStatus.md)|  | [optional]
 **reusability** | **PaymentMethodReusability**|  | [optional]
 **customer_id** | **str**|  | [optional]
 **reference_id** | **str**|  | [optional]
 **after_id** | **str**|  | [optional]
 **before_id** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**PaymentMethodList**](PaymentMethodList.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful |  -  |
**400** | Bad request |  -  |
**403** | Forbidden due to permissions |  -  |
**404** | Data not found |  -  |
**0** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method_by_id**
> PaymentMethod get_payment_method_by_id(payment_method_id)

Get payment method by ID

Get payment method by ID

### Example


```python
import time
import xendit
from xendit.apis import PaymentMethodApi
from xendit.payment_method.model.get_all_payment_methods403_response import GetAllPaymentMethods403Response
from xendit.payment_method.model.get_all_payment_methods400_response import GetAllPaymentMethods400Response
from xendit.payment_method.model.get_all_payment_methods404_response import GetAllPaymentMethods404Response
from xendit.payment_method.model.payment_method import PaymentMethod
from xendit.payment_method.model.get_all_payment_methods_default_response import GetAllPaymentMethodsDefaultResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = xendit.Configuration(
    api_key = 'XENDIT API KEY'
)


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentMethodApi(api_client)
payment_method_id = "pm-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str | 

# example passing only required values which don't have defaults set
try:
    # Get payment method by ID
    api_response = api_instance.get_payment_method_by_id(payment_method_id)
    pprint(api_response)
except xendit.ApiException as e:
    print("Exception when calling PaymentMethodApi->get_payment_method_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**|  |

### Return type

[**PaymentMethod**](PaymentMethod.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful |  -  |
**400** | Bad request |  -  |
**403** | Forbidden due to permissions |  -  |
**404** | Data not found |  -  |
**0** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payments_by_payment_method_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_payments_by_payment_method_id(payment_method_id)

Returns payments with matching PaymentMethodID.

Returns payments with matching PaymentMethodID.

### Example


```python
import time
import xendit
from xendit.apis import PaymentMethodApi
from xendit.payment_method.model.get_all_payment_methods403_response import GetAllPaymentMethods403Response
from xendit.payment_method.model.get_all_payment_methods400_response import GetAllPaymentMethods400Response
from xendit.payment_method.model.get_all_payment_methods404_response import GetAllPaymentMethods404Response
from xendit.payment_method.model.create_payment_method503_response import CreatePaymentMethod503Response
from xendit.payment_method.model.payment_method_type import PaymentMethodType
from xendit.payment_method.model.get_all_payment_methods_default_response import GetAllPaymentMethodsDefaultResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = xendit.Configuration(
    api_key = 'XENDIT API KEY'
)


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentMethodApi(api_client)
payment_method_id = "pm-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str | 

# example passing only required values which don't have defaults set
try:
    # Returns payments with matching PaymentMethodID.
    api_response = api_instance.get_payments_by_payment_method_id(payment_method_id)
    pprint(api_response)
except xendit.ApiException as e:
    print("Exception when calling PaymentMethodApi->get_payments_by_payment_method_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Returns payments with matching PaymentMethodID.
    api_response = api_instance.get_payments_by_payment_method_id(payment_method_id, payment_request_id=payment_request_id, payment_method_id2=payment_method_id2, reference_id=reference_id, payment_method_type=payment_method_type, channel_code=channel_code, status=status, currency=currency, created_gte=created_gte, created_lte=created_lte, updated_gte=updated_gte, updated_lte=updated_lte, limit=limit, after_id=after_id, before_id=before_id)
    pprint(api_response)
except xendit.ApiException as e:
    print("Exception when calling PaymentMethodApi->get_payments_by_payment_method_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**|  |
 **payment_request_id** | **[str]**|  | [optional]
 **payment_method_id2** | **[str]**|  | [optional]
 **reference_id** | **[str]**|  | [optional]
 **payment_method_type** | [**[PaymentMethodType]**](PaymentMethodType.md)|  | [optional]
 **channel_code** | **[str]**|  | [optional]
 **status** | **[str]**|  | [optional]
 **currency** | **[str]**|  | [optional]
 **created_gte** | **datetime**|  | [optional]
 **created_lte** | **datetime**|  | [optional]
 **updated_gte** | **datetime**|  | [optional]
 **updated_lte** | **datetime**|  | [optional]
 **limit** | **int**|  | [optional]
 **after_id** | **str**|  | [optional]
 **before_id** | **str**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful |  -  |
**400** | Bad request |  -  |
**403** | Forbidden due to permissions |  -  |
**404** | Data not found |  -  |
**503** | Service is unavailable due to dependencies |  -  |
**0** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_payment_method**
> PaymentMethod patch_payment_method(payment_method_id)

Patch payment methods

This endpoint is used to toggle the ```status``` of an e-Wallet or a Direct Debit payment method to ```ACTIVE``` or ```INACTIVE```.  This is also used to update the details of an Over-the-Counter or a Virtual Account payment method.

### Example


```python
import time
import xendit
from xendit.apis import PaymentMethodApi
from xendit.payment_method.model.get_all_payment_methods403_response import GetAllPaymentMethods403Response
from xendit.payment_method.model.get_all_payment_methods400_response import GetAllPaymentMethods400Response
from xendit.payment_method.model.get_all_payment_methods404_response import GetAllPaymentMethods404Response
from xendit.payment_method.model.payment_method import PaymentMethod
from xendit.payment_method.model.payment_method_update_parameters import PaymentMethodUpdateParameters
from xendit.payment_method.model.get_all_payment_methods_default_response import GetAllPaymentMethodsDefaultResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = xendit.Configuration(
    api_key = 'XENDIT API KEY'
)


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentMethodApi(api_client)
payment_method_id = "pm-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str | 

# example passing only required values which don't have defaults set
try:
    # Patch payment methods
    api_response = api_instance.patch_payment_method(payment_method_id)
    pprint(api_response)
except xendit.ApiException as e:
    print("Exception when calling PaymentMethodApi->patch_payment_method: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Patch payment methods
    api_response = api_instance.patch_payment_method(payment_method_id, payment_method_update_parameters=payment_method_update_parameters)
    pprint(api_response)
except xendit.ApiException as e:
    print("Exception when calling PaymentMethodApi->patch_payment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**|  |
 **payment_method_update_parameters** | [**PaymentMethodUpdateParameters**](PaymentMethodUpdateParameters.md)|  | [optional]

### Return type

[**PaymentMethod**](PaymentMethod.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful |  -  |
**400** | Bad request |  -  |
**403** | Forbidden due to permissions |  -  |
**404** | Data not found |  -  |
**0** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simulate_payment**
> simulate_payment(payment_method_id)

Makes payment with matching PaymentMethodID.

Makes payment with matching PaymentMethodID.

### Example


```python
import time
import xendit
from xendit.apis import PaymentMethodApi
from xendit.payment_method.model.get_all_payment_methods403_response import GetAllPaymentMethods403Response
from xendit.payment_method.model.get_all_payment_methods400_response import GetAllPaymentMethods400Response
from xendit.payment_method.model.get_all_payment_methods404_response import GetAllPaymentMethods404Response
from xendit.payment_method.model.create_payment_method503_response import CreatePaymentMethod503Response
from xendit.payment_method.model.simulate_payment_request import SimulatePaymentRequest
from xendit.payment_method.model.get_all_payment_methods_default_response import GetAllPaymentMethodsDefaultResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = xendit.Configuration(
    api_key = 'XENDIT API KEY'
)


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentMethodApi(api_client)
payment_method_id = "pm-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str | 

# example passing only required values which don't have defaults set
try:
    # Makes payment with matching PaymentMethodID.
    api_instance.simulate_payment(payment_method_id)
except xendit.ApiException as e:
    print("Exception when calling PaymentMethodApi->simulate_payment: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Makes payment with matching PaymentMethodID.
    api_instance.simulate_payment(payment_method_id, simulate_payment_request=simulate_payment_request)
except xendit.ApiException as e:
    print("Exception when calling PaymentMethodApi->simulate_payment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**|  |
 **simulate_payment_request** | [**SimulatePaymentRequest**](SimulatePaymentRequest.md)|  | [optional]

### Return type

void (empty response body)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful |  -  |
**400** | Bad request |  -  |
**403** | Forbidden due to permissions |  -  |
**404** | Data not found |  -  |
**503** | Service is unavailable due to dependencies |  -  |
**0** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

