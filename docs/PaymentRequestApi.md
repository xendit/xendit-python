# xendit.apis.PaymentRequestApi

All URIs are relative to *https://api.xendit.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_request**](PaymentRequestApi.md#create_payment_request) | **POST** /payment_requests | Create Payment Request
[**get_payment_request_by_id**](PaymentRequestApi.md#get_payment_request_by_id) | **GET** /payment_requests/{paymentRequestId} | Get payment request by ID
[**get_payment_request_captures**](PaymentRequestApi.md#get_payment_request_captures) | **GET** /payment_requests/{paymentRequestId}/captures | Get Payment Request Capture
[**get_all_payment_requests**](PaymentRequestApi.md#get_all_payment_requests) | **GET** /payment_requests | Get all payment requests by filter
[**capture_payment_request**](PaymentRequestApi.md#capture_payment_request) | **POST** /payment_requests/{paymentRequestId}/captures | Payment Request Capture
[**authorize_payment_request**](PaymentRequestApi.md#authorize_payment_request) | **POST** /payment_requests/{paymentRequestId}/auth | Payment Request Authorize
[**resend_payment_request_auth**](PaymentRequestApi.md#resend_payment_request_auth) | **POST** /payment_requests/{paymentRequestId}/auth/resend | Payment Request Resend Auth


# **create_payment_request**
> PaymentRequest create_payment_request()

Create Payment Request

Create Payment Request

### Example


```python
import time
import xendit
from xendit.apis import PaymentRequestApi
from xendit.payment_request.model.payment_request_parameters import PaymentRequestParameters
from xendit.payment_request.model.error import Error
from xendit.payment_request.model.payment_request import PaymentRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentRequestApi(api_client)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Create Payment Request
    api_response = api_instance.create_payment_request(idempotency_key=idempotency_key, for_user_id=for_user_id, payment_request_parameters=payment_request_parameters)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentRequestApi->create_payment_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**|  | [optional]
 **for_user_id** | **str**|  | [optional]
 **payment_request_parameters** | [**PaymentRequestParameters**](PaymentRequestParameters.md)|  | [optional]

### Return type

[**PaymentRequest**](PaymentRequest.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful |  -  |
**201** | Request successful |  -  |
**400** | Errors |  -  |
**500** | Errors |  -  |
**0** | Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_request_by_id**
> PaymentRequest get_payment_request_by_id(payment_request_id)

Get payment request by ID

Get payment request by ID

### Example


```python
import time
import xendit
from xendit.apis import PaymentRequestApi
from xendit.payment_request.model.error import Error
from xendit.payment_request.model.payment_request import PaymentRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentRequestApi(api_client)
payment_request_id = "pr-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str | 

# example passing only required values which don't have defaults set
try:
    # Get payment request by ID
    api_response = api_instance.get_payment_request_by_id(payment_request_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentRequestApi->get_payment_request_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get payment request by ID
    api_response = api_instance.get_payment_request_by_id(payment_request_id, for_user_id=for_user_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentRequestApi->get_payment_request_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_request_id** | **str**|  |
 **for_user_id** | **str**|  | [optional]

### Return type

[**PaymentRequest**](PaymentRequest.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful |  -  |
**404** | Errors |  -  |
**500** | Errors |  -  |
**0** | Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_request_captures**
> CaptureListResponse get_payment_request_captures(payment_request_id)

Get Payment Request Capture

Get Payment Request Capture

### Example


```python
import time
import xendit
from xendit.apis import PaymentRequestApi
from xendit.payment_request.model.error import Error
from xendit.payment_request.model.capture_list_response import CaptureListResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentRequestApi(api_client)
payment_request_id = "pr-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str | 

# example passing only required values which don't have defaults set
try:
    # Get Payment Request Capture
    api_response = api_instance.get_payment_request_captures(payment_request_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentRequestApi->get_payment_request_captures: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get Payment Request Capture
    api_response = api_instance.get_payment_request_captures(payment_request_id, for_user_id=for_user_id, limit=limit)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentRequestApi->get_payment_request_captures: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_request_id** | **str**|  |
 **for_user_id** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**CaptureListResponse**](CaptureListResponse.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful |  -  |
**400** | Errors |  -  |
**500** | Errors |  -  |
**0** | Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_payment_requests**
> PaymentRequestListResponse get_all_payment_requests()

Get all payment requests by filter

Get all payment requests by filter

### Example


```python
import time
import xendit
from xendit.apis import PaymentRequestApi
from xendit.payment_request.model.payment_request_list_response import PaymentRequestListResponse
from xendit.payment_request.model.error import Error
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentRequestApi(api_client)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get all payment requests by filter
    api_response = api_instance.get_all_payment_requests(for_user_id=for_user_id, reference_id=reference_id, id=id, customer_id=customer_id, limit=limit, before_id=before_id, after_id=after_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentRequestApi->get_all_payment_requests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **for_user_id** | **str**|  | [optional]
 **reference_id** | **[str]**|  | [optional]
 **id** | **[str]**|  | [optional]
 **customer_id** | **[str]**|  | [optional]
 **limit** | **int**|  | [optional]
 **before_id** | **str**|  | [optional]
 **after_id** | **str**|  | [optional]

### Return type

[**PaymentRequestListResponse**](PaymentRequestListResponse.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful |  -  |
**404** | Errors |  -  |
**500** | Errors |  -  |
**0** | Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **capture_payment_request**
> Capture capture_payment_request(payment_request_id)

Payment Request Capture

Payment Request Capture

### Example


```python
import time
import xendit
from xendit.apis import PaymentRequestApi
from xendit.payment_request.model.capture_parameters import CaptureParameters
from xendit.payment_request.model.error import Error
from xendit.payment_request.model.capture import Capture
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentRequestApi(api_client)
payment_request_id = "pr-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str | 

# example passing only required values which don't have defaults set
try:
    # Payment Request Capture
    api_response = api_instance.capture_payment_request(payment_request_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentRequestApi->capture_payment_request: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Payment Request Capture
    api_response = api_instance.capture_payment_request(payment_request_id, for_user_id=for_user_id, capture_parameters=capture_parameters)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentRequestApi->capture_payment_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_request_id** | **str**|  |
 **for_user_id** | **str**|  | [optional]
 **capture_parameters** | [**CaptureParameters**](CaptureParameters.md)|  | [optional]

### Return type

[**Capture**](Capture.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Capture created |  -  |
**400** | Errors |  -  |
**500** | Errors |  -  |
**0** | Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorize_payment_request**
> PaymentRequest authorize_payment_request(payment_request_id)

Payment Request Authorize

Payment Request Authorize

### Example


```python
import time
import xendit
from xendit.apis import PaymentRequestApi
from xendit.payment_request.model.error import Error
from xendit.payment_request.model.payment_request_auth_parameters import PaymentRequestAuthParameters
from xendit.payment_request.model.payment_request import PaymentRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentRequestApi(api_client)
payment_request_id = "pr-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str | 

# example passing only required values which don't have defaults set
try:
    # Payment Request Authorize
    api_response = api_instance.authorize_payment_request(payment_request_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentRequestApi->authorize_payment_request: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Payment Request Authorize
    api_response = api_instance.authorize_payment_request(payment_request_id, for_user_id=for_user_id, payment_request_auth_parameters=payment_request_auth_parameters)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentRequestApi->authorize_payment_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_request_id** | **str**|  |
 **for_user_id** | **str**|  | [optional]
 **payment_request_auth_parameters** | [**PaymentRequestAuthParameters**](PaymentRequestAuthParameters.md)|  | [optional]

### Return type

[**PaymentRequest**](PaymentRequest.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful |  -  |
**400** | Errors |  -  |
**500** | Errors |  -  |
**0** | Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_payment_request_auth**
> PaymentRequest resend_payment_request_auth(payment_request_id)

Payment Request Resend Auth

Payment Request Resend Auth

### Example


```python
import time
import xendit
from xendit.apis import PaymentRequestApi
from xendit.payment_request.model.error import Error
from xendit.payment_request.model.payment_request import PaymentRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentRequestApi(api_client)
payment_request_id = "pr-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str | 

# example passing only required values which don't have defaults set
try:
    # Payment Request Resend Auth
    api_response = api_instance.resend_payment_request_auth(payment_request_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentRequestApi->resend_payment_request_auth: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Payment Request Resend Auth
    api_response = api_instance.resend_payment_request_auth(payment_request_id, for_user_id=for_user_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentRequestApi->resend_payment_request_auth: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_request_id** | **str**|  |
 **for_user_id** | **str**|  | [optional]

### Return type

[**PaymentRequest**](PaymentRequest.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful |  -  |
**400** | Errors |  -  |
**500** | Errors |  -  |
**0** | Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

