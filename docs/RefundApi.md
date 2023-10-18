# xendit.apis.RefundApi

All URIs are relative to *https://api.xendit.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_refund**](RefundApi.md#create_refund) | **POST** /refunds | 
[**get_refund**](RefundApi.md#get_refund) | **GET** /refunds/{refundID} | 
[**get_all_refunds**](RefundApi.md#get_all_refunds) | **GET** /refunds | 
[**cancel_refund**](RefundApi.md#cancel_refund) | **POST** /refunds/{refundID}/cancel | 


# **create_refund**
> Refund create_refund()



### Example


```python
import time
import xendit
from xendit.apis import RefundApi
from xendit.refund.model.create_refund404_response import CreateRefund404Response
from xendit.refund.model.create_refund403_response import CreateRefund403Response
from xendit.refund.model.create_refund503_response import CreateRefund503Response
from xendit.refund.model.refund import Refund
from xendit.refund.model.create_refund400_response import CreateRefund400Response
from xendit.refund.model.create_refund import CreateRefund
from xendit.refund.model.get_all_refunds_default_response import GetAllRefundsDefaultResponse
from xendit.refund.model.create_refund409_response import CreateRefund409Response
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = RefundApi(api_client)

# example passing only required values which don't have defaults set
# and optional values
try:
    api_response = api_instance.create_refund(idempotency_key=idempotency_key, for_user_id=for_user_id, create_refund=create_refund)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling RefundApi->create_refund: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**|  | [optional]
 **for_user_id** | **str**|  | [optional]
 **create_refund** | [**CreateRefund**](CreateRefund.md)|  | [optional]

### Return type

[**Refund**](Refund.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**403** | Forbidden due to permissions |  -  |
**404** | Data not found |  -  |
**409** | Request causes conflict |  -  |
**503** | Service is unavailable due to dependencies |  -  |
**0** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refund**
> Refund get_refund(refund_id)



### Example


```python
import time
import xendit
from xendit.apis import RefundApi
from xendit.refund.model.refund import Refund
from xendit.refund.model.get_all_refunds_default_response import GetAllRefundsDefaultResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = RefundApi(api_client)
refund_id = "rfd-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str | 

# example passing only required values which don't have defaults set
try:
    api_response = api_instance.get_refund(refund_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling RefundApi->get_refund: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    api_response = api_instance.get_refund(refund_id, idempotency_key=idempotency_key, for_user_id=for_user_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling RefundApi->get_refund: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_id** | **str**|  |
 **idempotency_key** | **str**|  | [optional]
 **for_user_id** | **str**|  | [optional]

### Return type

[**Refund**](Refund.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_refunds**
> RefundList get_all_refunds()



### Example


```python
import time
import xendit
from xendit.apis import RefundApi
from xendit.refund.model.refund_list import RefundList
from xendit.refund.model.get_all_refunds_default_response import GetAllRefundsDefaultResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = RefundApi(api_client)

# example passing only required values which don't have defaults set
# and optional values
try:
    api_response = api_instance.get_all_refunds(for_user_id=for_user_id, payment_request_id=payment_request_id, invoice_id=invoice_id, payment_method_type=payment_method_type, channel_code=channel_code, limit=limit, after_id=after_id, before_id=before_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling RefundApi->get_all_refunds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **for_user_id** | **str**|  | [optional]
 **payment_request_id** | **str**|  | [optional]
 **invoice_id** | **str**|  | [optional]
 **payment_method_type** | **str**|  | [optional]
 **channel_code** | **str**|  | [optional]
 **limit** | **float**|  | [optional]
 **after_id** | **str**|  | [optional]
 **before_id** | **str**|  | [optional]

### Return type

[**RefundList**](RefundList.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_refund**
> Refund cancel_refund(refund_id)



### Example


```python
import time
import xendit
from xendit.apis import RefundApi
from xendit.refund.model.create_refund404_response import CreateRefund404Response
from xendit.refund.model.create_refund403_response import CreateRefund403Response
from xendit.refund.model.refund import Refund
from xendit.refund.model.create_refund400_response import CreateRefund400Response
from xendit.refund.model.get_all_refunds_default_response import GetAllRefundsDefaultResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = RefundApi(api_client)
refund_id = "rfd-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str | 

# example passing only required values which don't have defaults set
try:
    api_response = api_instance.cancel_refund(refund_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling RefundApi->cancel_refund: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    api_response = api_instance.cancel_refund(refund_id, idempotency_key=idempotency_key, for_user_id=for_user_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling RefundApi->cancel_refund: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_id** | **str**|  |
 **idempotency_key** | **str**|  | [optional]
 **for_user_id** | **str**|  | [optional]

### Return type

[**Refund**](Refund.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**403** | Forbidden due to permissions |  -  |
**404** | Data not found |  -  |
**0** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

