# xendit.apis.CustomerApi

All URIs are relative to *https://api.xendit.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer**](CustomerApi.md#create_customer) | **POST** /customers | Create Customer
[**get_customer**](CustomerApi.md#get_customer) | **GET** /customers/{id} | Get Customer By ID
[**get_customer_by_reference_id**](CustomerApi.md#get_customer_by_reference_id) | **GET** /customers | GET customers by reference id
[**update_customer**](CustomerApi.md#update_customer) | **PATCH** /customers/{id} | Update End Customer Resource


# **create_customer**
> Customer create_customer()

Create Customer

Function to create a customer that you may use in your Invoice or Payment Requests. For detail explanations, see this link: https://developers.xendit.co/api-reference/#create-customer

### Example


```python
import time
import xendit
from xendit.apis import CustomerApi
from xendit.customer.model.customer import Customer
from xendit.customer.model.customer_request import CustomerRequest
from xendit.customer.model.create_customer400_response import CreateCustomer400Response
from xendit.customer.model.error import Error
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = CustomerApi(api_client)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Create Customer
    api_response = api_instance.create_customer(idempotency_key=idempotency_key, for_user_id=for_user_id, customer_request=customer_request)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling CustomerApi->create_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique key to prevent processing duplicate requests. | [optional]
 **for_user_id** | **str**| The sub-account user-id that you want to make this transaction for. | [optional]
 **customer_request** | [**CustomerRequest**](CustomerRequest.md)| Request object for end customer object | [optional]

### Return type

[**Customer**](Customer.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created End Customer |  -  |
**400** | Various errors |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer**
> Customer get_customer(id)

Get Customer By ID

Retrieves a single customer object For detail explanations, see this link: https://developers.xendit.co/api-reference/#get-customer

### Example


```python
import time
import xendit
from xendit.apis import CustomerApi
from xendit.customer.model.customer import Customer
from xendit.customer.model.get_customer_by_reference_id400_response import GetCustomerByReferenceID400Response
from xendit.customer.model.error import Error
from xendit.customer.model.response_data_not_found import ResponseDataNotFound
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = CustomerApi(api_client)
id = "d290f1ee-6c54-4b01-90e6-d701748f0851" # str | End customer resource id

# example passing only required values which don't have defaults set
try:
    # Get Customer By ID
    api_response = api_instance.get_customer(id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling CustomerApi->get_customer: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get Customer By ID
    api_response = api_instance.get_customer(id, for_user_id=for_user_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling CustomerApi->get_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| End customer resource id |
 **for_user_id** | **str**| The sub-account user-id that you want to make this transaction for. | [optional]

### Return type

[**Customer**](Customer.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | End Customer Resource |  -  |
**400** | Various errors |  -  |
**404** | Customer not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_by_reference_id**
> GetCustomerByReferenceID200Response get_customer_by_reference_id(reference_id)

GET customers by reference id

Retrieves an array with a customer object that matches the provided reference_id - the identifier provided by you For detail explanations, see this link: https://developers.xendit.co/api-reference/#get-customer-by-reference-id

### Example


```python
import time
import xendit
from xendit.apis import CustomerApi
from xendit.customer.model.get_customer_by_reference_id400_response import GetCustomerByReferenceID400Response
from xendit.customer.model.error import Error
from xendit.customer.model.get_customer_by_reference_id200_response import GetCustomerByReferenceID200Response
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = CustomerApi(api_client)
reference_id = "reference_id_example" # str | Merchant's reference of end customer

# example passing only required values which don't have defaults set
try:
    # GET customers by reference id
    api_response = api_instance.get_customer_by_reference_id(reference_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling CustomerApi->get_customer_by_reference_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # GET customers by reference id
    api_response = api_instance.get_customer_by_reference_id(reference_id, for_user_id=for_user_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling CustomerApi->get_customer_by_reference_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_id** | **str**| Merchant&#39;s reference of end customer |
 **for_user_id** | **str**| The sub-account user-id that you want to make this transaction for. | [optional]

### Return type

[**GetCustomerByReferenceID200Response**](GetCustomerByReferenceID200Response.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | End Customers |  -  |
**400** | Various errors |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer**
> Customer update_customer(id)

Update End Customer Resource

Function to update an existing customer. For a detailed explanation For detail explanations, see this link: https://developers.xendit.co/api-reference/#update-customer

### Example


```python
import time
import xendit
from xendit.apis import CustomerApi
from xendit.customer.model.customer import Customer
from xendit.customer.model.update_customer400_response import UpdateCustomer400Response
from xendit.customer.model.error import Error
from xendit.customer.model.patch_customer import PatchCustomer
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = CustomerApi(api_client)
id = "d290f1ee-6c54-4b01-90e6-d701748f0851" # str | End customer resource id

# example passing only required values which don't have defaults set
try:
    # Update End Customer Resource
    api_response = api_instance.update_customer(id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling CustomerApi->update_customer: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Update End Customer Resource
    api_response = api_instance.update_customer(id, for_user_id=for_user_id, patch_customer=patch_customer)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling CustomerApi->update_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| End customer resource id |
 **for_user_id** | **str**| The sub-account user-id that you want to make this transaction for. | [optional]
 **patch_customer** | [**PatchCustomer**](PatchCustomer.md)| Update Request for end customer object | [optional]

### Return type

[**Customer**](Customer.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated End Customer |  -  |
**400** | Various errors |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

