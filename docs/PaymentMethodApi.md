# PaymentMethodApi


You can use the APIs below to interface with Xendit's `PaymentMethodApi`.
To start using the API, you need to configure the secret key and initiate the client instance.

```python
import time
import xendit
from xendit.apis import PaymentMethodApi

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')

# Enter a context with an instance of the API client
api_client = xendit.ApiClient()

# Create an instance of the API class
api_instance = PaymentMethodApi(api_client)
```

All URIs are relative to *https://api.xendit.co*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**create_payment_method**](PaymentMethodApi.md#create_payment_method-function) | **POST** /v2/payment_methods | Creates payment method |
| [**get_payment_method_by_id**](PaymentMethodApi.md#get_payment_method_by_id-function) | **GET** /v2/payment_methods/{paymentMethodId} | Get payment method by ID |
| [**get_payments_by_payment_method_id**](PaymentMethodApi.md#get_payments_by_payment_method_id-function) | **GET** /v2/payment_methods/{paymentMethodId}/payments | Returns payments with matching PaymentMethodID. |
| [**patch_payment_method**](PaymentMethodApi.md#patch_payment_method-function) | **PATCH** /v2/payment_methods/{paymentMethodId} | Patch payment methods |
| [**get_all_payment_methods**](PaymentMethodApi.md#get_all_payment_methods-function) | **GET** /v2/payment_methods | Get all payment methods by filters |
| [**expire_payment_method**](PaymentMethodApi.md#expire_payment_method-function) | **POST** /v2/payment_methods/{paymentMethodId}/expire | Expires a payment method |
| [**auth_payment_method**](PaymentMethodApi.md#auth_payment_method-function) | **POST** /v2/payment_methods/{paymentMethodId}/auth | Validate a payment method&#39;s linking OTP |
| [**simulate_payment**](PaymentMethodApi.md#simulate_payment-function) | **POST** /v2/payment_methods/{paymentMethodId}/payments/simulate | Makes payment with matching PaymentMethodID. |


# `create_payment_method()` Function
> PaymentMethod create_payment_method()

Creates payment method

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `create_payment_method` |
| Request Parameters  |  [CreatePaymentMethodRequestParams](#request-parameters--CreatePaymentMethodRequestParams)	 |
| Return Type  | [**PaymentMethod**](payment_method/PaymentMethod.md) |

### Request Parameters - CreatePaymentMethodRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **for_user_id** | **str**| |  |
| **payment_method_parameters** | [**PaymentMethodParameters**](payment_method/PaymentMethodParameters.md)| |  |

### Usage Example
#### Account linking for E-Wallet

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
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentMethodApi(api_client)
for_user_id = "5f9a3fbd571a1c4068aa40cf" # str 
payment_method_parameters = {
  "type" : "EWALLET",
  "reusability" : "MULTIPLE_USE",
  "customer" : {
    "reference_id" : "customer-123",
    "type" : "INDIVIDUAL",
    "individual_detail" : {
      "given_names" : "John",
      "surname" : "Doe"
    }
  },
  "ewallet" : {
    "channel_code" : "OVO",
    "channel_properties" : {
      "success_return_url" : "https://redirect.me/success",
      "failure_return_url" : "https://redirect.me/failure",
      "cancel_return_url" : "https://redirect.me/cancel"
    }
  },
  "metadata" : {
    "sku" : "example-1234"
  }
} # PaymentMethodParameters 

# example passing only required values which don't have defaults set
# and optional values
try:
    # Creates payment method
    api_response = api_instance.create_payment_method(for_user_id=for_user_id, payment_method_parameters=payment_method_parameters)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentMethodApi->create_payment_method: %s\n" % e)
```
#### Account linking for PH Direct Debit

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
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentMethodApi(api_client)
for_user_id = "5f9a3fbd571a1c4068aa40cf" # str 
payment_method_parameters = {
  "type" : "DIRECT_DEBIT",
  "direct_debit" : {
    "channel_code" : "BPI",
    "channel_properties" : {
      "success_return_url" : "https://redirect.me/success",
      "failure_return_url" : "https://redirect.me/failure"
    }
  },
  "reusability" : "MULTIPLE_USE",
  "customer" : {
    "reference_id" : "customer-123",
    "type" : "INDIVIDUAL",
    "individual_detail" : {
      "given_names" : "John",
      "surname" : "Doe"
    }
  },
  "email" : "testemail@email.com",
  "mobile_number" : 628774494404
} # PaymentMethodParameters 

# example passing only required values which don't have defaults set
# and optional values
try:
    # Creates payment method
    api_response = api_instance.create_payment_method(for_user_id=for_user_id, payment_method_parameters=payment_method_parameters)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentMethodApi->create_payment_method: %s\n" % e)
```

# `get_payment_method_by_id()` Function
> PaymentMethod get_payment_method_by_id(payment_method_id)

Get payment method by ID

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `get_payment_method_by_id` |
| Request Parameters  |  [GetPaymentMethodByIdRequestParams](#request-parameters--GetPaymentMethodByIdRequestParams)	 |
| Return Type  | [**PaymentMethod**](payment_method/PaymentMethod.md) |

### Request Parameters - GetPaymentMethodByIdRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **payment_method_id** | **str** | ☑️ | |
| **for_user_id** | **str**| |  |

### Usage Example
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
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentMethodApi(api_client)
payment_method_id = "pm-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str 
for_user_id = "5f9a3fbd571a1c4068aa40cf" # str 

# example passing only required values which don't have defaults set
try:
    # Get payment method by ID
    api_response = api_instance.get_payment_method_by_id(payment_method_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentMethodApi->get_payment_method_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get payment method by ID
    api_response = api_instance.get_payment_method_by_id(payment_method_id, for_user_id=for_user_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentMethodApi->get_payment_method_by_id: %s\n" % e)
```

# `get_payments_by_payment_method_id()` Function
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_payments_by_payment_method_id(payment_method_id)

Returns payments with matching PaymentMethodID.

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `get_payments_by_payment_method_id` |
| Request Parameters  |  [GetPaymentsByPaymentMethodIdRequestParams](#request-parameters--GetPaymentsByPaymentMethodIdRequestParams)	 |
| Return Type  | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |

### Request Parameters - GetPaymentsByPaymentMethodIdRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **payment_method_id** | **str** | ☑️ | |
| **for_user_id** | **str**| |  |
| **payment_request_id** | **[str]**| |  |
| **payment_method_id2** | **[str]**| |  |
| **reference_id** | **[str]**| |  |
| **payment_method_type** | [**[PaymentMethodType]**](payment_method/PaymentMethodType.md)| |  |
| **channel_code** | **[str]**| |  |
| **status** | **[str]**| |  |
| **currency** | **[str]**| |  |
| **created_gte** | **datetime**| |  |
| **created_lte** | **datetime**| |  |
| **updated_gte** | **datetime**| |  |
| **updated_lte** | **datetime**| |  |
| **limit** | **int**| |  |

### Usage Example
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
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentMethodApi(api_client)
payment_method_id = "pm-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str 
for_user_id = "5f9a3fbd571a1c4068aa40cf" # str 
payment_request_id = [
        "payment_request_id_example",
    ] # [str] 
payment_method_id2 = [
        "payment_method_id_example",
    ] # [str] 
reference_id = [
        "reference_id_example",
    ] # [str] 
payment_method_type = [
        PaymentMethodType("CARD"),
    ] # [PaymentMethodType] 
channel_code = [
        "channel_code_example",
    ] # [str] 
status = [
        "status_example",
    ] # [str] 
currency = [
        "currency_example",
    ] # [str] 
created_gte = dateutil_parser('2016-08-29T09:12:33.001Z') # datetime 
created_lte = dateutil_parser('2016-08-29T09:12:33.001Z') # datetime 
updated_gte = dateutil_parser('2016-08-29T09:12:33.001Z') # datetime 
updated_lte = dateutil_parser('2016-08-29T09:12:33.001Z') # datetime 
limit = 1 # int 

# example passing only required values which don't have defaults set
try:
    # Returns payments with matching PaymentMethodID.
    api_response = api_instance.get_payments_by_payment_method_id(payment_method_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentMethodApi->get_payments_by_payment_method_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Returns payments with matching PaymentMethodID.
    api_response = api_instance.get_payments_by_payment_method_id(payment_method_id, for_user_id=for_user_id, payment_request_id=payment_request_id, payment_method_id2=payment_method_id2, reference_id=reference_id, payment_method_type=payment_method_type, channel_code=channel_code, status=status, currency=currency, created_gte=created_gte, created_lte=created_lte, updated_gte=updated_gte, updated_lte=updated_lte, limit=limit)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentMethodApi->get_payments_by_payment_method_id: %s\n" % e)
```

# `patch_payment_method()` Function
> PaymentMethod patch_payment_method(payment_method_id)

Patch payment methods

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `patch_payment_method` |
| Request Parameters  |  [PatchPaymentMethodRequestParams](#request-parameters--PatchPaymentMethodRequestParams)	 |
| Return Type  | [**PaymentMethod**](payment_method/PaymentMethod.md) |

### Request Parameters - PatchPaymentMethodRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **payment_method_id** | **str** | ☑️ | |
| **for_user_id** | **str**| |  |
| **payment_method_update_parameters** | [**PaymentMethodUpdateParameters**](payment_method/PaymentMethodUpdateParameters.md)| |  |

### Usage Example
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
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentMethodApi(api_client)
payment_method_id = "pm-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str 
for_user_id = "5f9a3fbd571a1c4068aa40cf" # str 
payment_method_update_parameters = PaymentMethodUpdateParameters(
        description="description_example",
        reference_id="reference_id_example",
        reusability=PaymentMethodReusability("MULTIPLE_USE"),
        status=PaymentMethodStatus("ACTIVE"),
        over_the_counter=OverTheCounterUpdateParameters(
            amount=3.14,
            channel_properties=OverTheCounterChannelPropertiesUpdate(
                customer_name="Rika Sutanto",
                expires_at=dateutil_parser('2022-01-01T00:00:00Z'),
            ),
        ),
        virtual_account=VirtualAccountUpdateParameters(
            amount=3.14,
            min_amount=1,
            max_amount=1,
            channel_properties=VirtualAccountChannelPropertiesPatch(
                expires_at=dateutil_parser('2022-01-01T00:00:00Z'),
                suggested_amount=100000,
            ),
            alternative_display_types=[
                "QR_STRING",
            ],
        ),
    ) # PaymentMethodUpdateParameters 

# example passing only required values which don't have defaults set
try:
    # Patch payment methods
    api_response = api_instance.patch_payment_method(payment_method_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentMethodApi->patch_payment_method: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Patch payment methods
    api_response = api_instance.patch_payment_method(payment_method_id, for_user_id=for_user_id, payment_method_update_parameters=payment_method_update_parameters)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentMethodApi->patch_payment_method: %s\n" % e)
```

# `get_all_payment_methods()` Function
> PaymentMethodList get_all_payment_methods()

Get all payment methods by filters

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `get_all_payment_methods` |
| Request Parameters  |  [GetAllPaymentMethodsRequestParams](#request-parameters--GetAllPaymentMethodsRequestParams)	 |
| Return Type  | [**PaymentMethodList**](payment_method/PaymentMethodList.md) |

### Request Parameters - GetAllPaymentMethodsRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **for_user_id** | **str**| |  |
| **id** | **[str]**| |  |
| **type** | **[str]**| |  |
| **status** | [**[PaymentMethodStatus]**](payment_method/PaymentMethodStatus.md)| |  |
| **reusability** | **PaymentMethodReusability**| |  |
| **customer_id** | **str**| |  |
| **reference_id** | **str**| |  |
| **after_id** | **str**| |  |
| **before_id** | **str**| |  |
| **limit** | **int**| |  |

### Usage Example
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
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentMethodApi(api_client)
for_user_id = "5f9a3fbd571a1c4068aa40cf" # str 
id = [
        "id_example",
    ] # [str] 
type = [
        "type_example",
    ] # [str] 
status = [
        PaymentMethodStatus("ACTIVE"),
    ] # [PaymentMethodStatus] 
reusability = PaymentMethodReusability("MULTIPLE_USE") # PaymentMethodReusability 
customer_id = "customer_id_example" # str 
reference_id = "reference_id_example" # str 
after_id = "after_id_example" # str 
before_id = "before_id_example" # str 
limit = 1 # int 

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get all payment methods by filters
    api_response = api_instance.get_all_payment_methods(for_user_id=for_user_id, id=id, type=type, status=status, reusability=reusability, customer_id=customer_id, reference_id=reference_id, after_id=after_id, before_id=before_id, limit=limit)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentMethodApi->get_all_payment_methods: %s\n" % e)
```

# `expire_payment_method()` Function
> PaymentMethod expire_payment_method(payment_method_id)

Expires a payment method

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `expire_payment_method` |
| Request Parameters  |  [ExpirePaymentMethodRequestParams](#request-parameters--ExpirePaymentMethodRequestParams)	 |
| Return Type  | [**PaymentMethod**](payment_method/PaymentMethod.md) |

### Request Parameters - ExpirePaymentMethodRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **payment_method_id** | **str** | ☑️ | |
| **for_user_id** | **str**| |  |
| **payment_method_expire_parameters** | [**PaymentMethodExpireParameters**](payment_method/PaymentMethodExpireParameters.md)| |  |

### Usage Example
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
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentMethodApi(api_client)
payment_method_id = "pm-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str 
for_user_id = "5f9a3fbd571a1c4068aa40cf" # str 
payment_method_expire_parameters = PaymentMethodExpireParameters(
        success_return_url="success_return_url_example",
        failure_return_url="failure_return_url_example",
    ) # PaymentMethodExpireParameters 

# example passing only required values which don't have defaults set
try:
    # Expires a payment method
    api_response = api_instance.expire_payment_method(payment_method_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentMethodApi->expire_payment_method: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Expires a payment method
    api_response = api_instance.expire_payment_method(payment_method_id, for_user_id=for_user_id, payment_method_expire_parameters=payment_method_expire_parameters)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentMethodApi->expire_payment_method: %s\n" % e)
```

# `auth_payment_method()` Function
> PaymentMethod auth_payment_method(payment_method_id)

Validate a payment method's linking OTP

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `auth_payment_method` |
| Request Parameters  |  [AuthPaymentMethodRequestParams](#request-parameters--AuthPaymentMethodRequestParams)	 |
| Return Type  | [**PaymentMethod**](payment_method/PaymentMethod.md) |

### Request Parameters - AuthPaymentMethodRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **payment_method_id** | **str** | ☑️ | |
| **for_user_id** | **str**| |  |
| **payment_method_auth_parameters** | [**PaymentMethodAuthParameters**](payment_method/PaymentMethodAuthParameters.md)| |  |

### Usage Example
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
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentMethodApi(api_client)
payment_method_id = "pm-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str 
for_user_id = "5f9a3fbd571a1c4068aa40cf" # str 
payment_method_auth_parameters = PaymentMethodAuthParameters(
        auth_code="auth_code_example",
    ) # PaymentMethodAuthParameters 

# example passing only required values which don't have defaults set
try:
    # Validate a payment method's linking OTP
    api_response = api_instance.auth_payment_method(payment_method_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentMethodApi->auth_payment_method: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Validate a payment method's linking OTP
    api_response = api_instance.auth_payment_method(payment_method_id, for_user_id=for_user_id, payment_method_auth_parameters=payment_method_auth_parameters)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentMethodApi->auth_payment_method: %s\n" % e)
```

# `simulate_payment()` Function
> simulate_payment(payment_method_id)

Makes payment with matching PaymentMethodID.

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `simulate_payment` |
| Request Parameters  |  [SimulatePaymentRequestParams](#request-parameters--SimulatePaymentRequestParams)	 |
| Return Type  | void (empty response body) |

### Request Parameters - SimulatePaymentRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **payment_method_id** | **str** | ☑️ | |
| **simulate_payment_request** | [**SimulatePaymentRequest**](payment_method/SimulatePaymentRequest.md)| |  |

### Usage Example
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
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = PaymentMethodApi(api_client)
payment_method_id = "pm-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str 
simulate_payment_request = SimulatePaymentRequest(
        amount=3.14,
    ) # SimulatePaymentRequest 

# example passing only required values which don't have defaults set
try:
    # Makes payment with matching PaymentMethodID.
    api_instance.simulate_payment(payment_method_id)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentMethodApi->simulate_payment: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Makes payment with matching PaymentMethodID.
    api_instance.simulate_payment(payment_method_id, simulate_payment_request=simulate_payment_request)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentMethodApi->simulate_payment: %s\n" % e)
```

[[Back to README]](../README.md)
