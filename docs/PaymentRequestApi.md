# PaymentRequestApi


You can use the APIs below to interface with Xendit's `PaymentRequestApi`.
To start using the API, you need to configure the secret key and initiate the client instance.

```python
import time
import xendit
from xendit.apis import PaymentRequestApi

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')

# Enter a context with an instance of the API client
api_client = xendit.ApiClient()

# Create an instance of the API class
api_instance = PaymentRequestApi(api_client)
```

All URIs are relative to *https://api.xendit.co*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**create_payment_request**](PaymentRequestApi.md#create_payment_request-function) | **POST** /payment_requests | Create Payment Request |
| [**get_payment_request_by_id**](PaymentRequestApi.md#get_payment_request_by_id-function) | **GET** /payment_requests/{paymentRequestId} | Get payment request by ID |
| [**get_payment_request_captures**](PaymentRequestApi.md#get_payment_request_captures-function) | **GET** /payment_requests/{paymentRequestId}/captures | Get Payment Request Capture |
| [**get_all_payment_requests**](PaymentRequestApi.md#get_all_payment_requests-function) | **GET** /payment_requests | Get all payment requests by filter |
| [**capture_payment_request**](PaymentRequestApi.md#capture_payment_request-function) | **POST** /payment_requests/{paymentRequestId}/captures | Payment Request Capture |
| [**authorize_payment_request**](PaymentRequestApi.md#authorize_payment_request-function) | **POST** /payment_requests/{paymentRequestId}/auth | Payment Request Authorize |
| [**resend_payment_request_auth**](PaymentRequestApi.md#resend_payment_request_auth-function) | **POST** /payment_requests/{paymentRequestId}/auth/resend | Payment Request Resend Auth |


# `create_payment_request()` Function
> PaymentRequest create_payment_request()

Create Payment Request

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `create_payment_request` |
| Request Parameters  |  [CreatePaymentRequestRequestParams](#request-parameters--CreatePaymentRequestRequestParams)	 |
| Return Type  | [**PaymentRequest**](payment_request/PaymentRequest.md) |

### Request Parameters - CreatePaymentRequestRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **idempotency_key** | **str**| |  |
| **for_user_id** | **str**| |  |
| **payment_request_parameters** | [**PaymentRequestParameters**](payment_request/PaymentRequestParameters.md)| |  |

### Usage Example
#### E-Wallet One Time Payment via Redirect URL

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
idempotency_key = "5f9a3fbd571a1c4068aa40ce" # str 
for_user_id = "5f9a3fbd571a1c4068aa40cf" # str 
payment_request_parameters = {
  "reference_id" : "example-ref-1234",
  "amount" : 15000,
  "currency" : "IDR",
  "country" : "ID",
  "payment_method" : {
    "type" : "EWALLET",
    "ewallet" : {
      "channel_code" : "SHOPEEPAY",
      "channel_properties" : {
        "success_return_url" : "https://redirect.me/success"
      }
    },
    "reusability" : "ONE_TIME_USE"
  }
} # PaymentRequestParameters 

# example passing only required values which don't have defaults set
# and optional values
try:
    # Create Payment Request
    api_response = api_instance.create_payment_request(idempotency_key=idempotency_key, for_user_id=for_user_id, payment_request_parameters=payment_request_parameters)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentRequestApi->create_payment_request: %s\n" % e)
```
#### Fixed amount dynamic QR

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
idempotency_key = "5f9a3fbd571a1c4068aa40ce" # str 
for_user_id = "5f9a3fbd571a1c4068aa40cf" # str 
payment_request_parameters = {
  "reference_id" : "example-ref-1234",
  "amount" : 15000,
  "currency" : "IDR",
  "payment_method" : {
    "type" : "QR_CODE",
    "reusability" : "ONE_TIME_USE",
    "qr_code" : {
      "channel_code" : "“QRIS”"
    }
  },
  "metadata" : {
    "sku" : "example-sku-1234"
  }
} # PaymentRequestParameters 

# example passing only required values which don't have defaults set
# and optional values
try:
    # Create Payment Request
    api_response = api_instance.create_payment_request(idempotency_key=idempotency_key, for_user_id=for_user_id, payment_request_parameters=payment_request_parameters)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentRequestApi->create_payment_request: %s\n" % e)
```
#### Fixed amount single use Virtual Account

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
idempotency_key = "5f9a3fbd571a1c4068aa40ce" # str 
for_user_id = "5f9a3fbd571a1c4068aa40cf" # str 
payment_request_parameters = {
  "reference_id" : "example-ref-1234",
  "currency" : "IDR",
  "amount" : 15000,
  "country" : "ID",
  "payment_method" : {
    "type" : "VIRTUAL_ACCOUNT",
    "reusability" : "ONE_TIME_USE",
    "reference_id" : "example-1234",
    "virtual_account" : {
      "channel_code" : "BNI",
      "channel_properties" : {
        "customer_name" : "Ahmad Gunawan",
        "expires_at" : "2023-01-03T17:00:00Z"
      }
    }
  },
  "metadata" : {
    "sku" : "example-sku-1234"
  }
} # PaymentRequestParameters 

# example passing only required values which don't have defaults set
# and optional values
try:
    # Create Payment Request
    api_response = api_instance.create_payment_request(idempotency_key=idempotency_key, for_user_id=for_user_id, payment_request_parameters=payment_request_parameters)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentRequestApi->create_payment_request: %s\n" % e)
```
#### Subsequent PH Direct Debit payments after account linking

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
idempotency_key = "5f9a3fbd571a1c4068aa40ce" # str 
for_user_id = "5f9a3fbd571a1c4068aa40cf" # str 
payment_request_parameters = {
  "reference_id" : "example-ref-1234",
  "amount" : 1500,
  "currency" : "PHP",
  "payment_method_id" : "pm-9685a196-81e9-4c73-8d62-97df5aab2762",
  "metadata" : {
    "sku" : "example-sku-1234"
  }
} # PaymentRequestParameters 

# example passing only required values which don't have defaults set
# and optional values
try:
    # Create Payment Request
    api_response = api_instance.create_payment_request(idempotency_key=idempotency_key, for_user_id=for_user_id, payment_request_parameters=payment_request_parameters)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentRequestApi->create_payment_request: %s\n" % e)
```
#### Subsequent tokenized E-Wallet payments after account linking

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
idempotency_key = "5f9a3fbd571a1c4068aa40ce" # str 
for_user_id = "5f9a3fbd571a1c4068aa40cf" # str 
payment_request_parameters = {
  "reference_id" : "example-ref-1234",
  "amount" : 15000,
  "currency" : "IDR",
  "payment_method_id" : "pm-2b2c6092-2100-4843-a7fc-f5c7edac7efd",
  "metadata" : {
    "sku" : "example-sku-1234"
  }
} # PaymentRequestParameters 

# example passing only required values which don't have defaults set
# and optional values
try:
    # Create Payment Request
    api_response = api_instance.create_payment_request(idempotency_key=idempotency_key, for_user_id=for_user_id, payment_request_parameters=payment_request_parameters)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentRequestApi->create_payment_request: %s\n" % e)
```

# `get_payment_request_by_id()` Function
> PaymentRequest get_payment_request_by_id(payment_request_id)

Get payment request by ID

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `get_payment_request_by_id` |
| Request Parameters  |  [GetPaymentRequestByIdRequestParams](#request-parameters--GetPaymentRequestByIdRequestParams)	 |
| Return Type  | [**PaymentRequest**](payment_request/PaymentRequest.md) |

### Request Parameters - GetPaymentRequestByIdRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **payment_request_id** | **str** | ☑️ | |
| **for_user_id** | **str**| |  |

### Usage Example
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
payment_request_id = "pr-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str 
for_user_id = "5f9a3fbd571a1c4068aa40cf" # str 

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

# `get_payment_request_captures()` Function
> CaptureListResponse get_payment_request_captures(payment_request_id)

Get Payment Request Capture

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `get_payment_request_captures` |
| Request Parameters  |  [GetPaymentRequestCapturesRequestParams](#request-parameters--GetPaymentRequestCapturesRequestParams)	 |
| Return Type  | [**CaptureListResponse**](payment_request/CaptureListResponse.md) |

### Request Parameters - GetPaymentRequestCapturesRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **payment_request_id** | **str** | ☑️ | |
| **for_user_id** | **str**| |  |
| **limit** | **int**| |  |

### Usage Example
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
payment_request_id = "pr-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str 
for_user_id = "5f9a3fbd571a1c4068aa40cf" # str 
limit = 1 # int 

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

# `get_all_payment_requests()` Function
> PaymentRequestListResponse get_all_payment_requests()

Get all payment requests by filter

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `get_all_payment_requests` |
| Request Parameters  |  [GetAllPaymentRequestsRequestParams](#request-parameters--GetAllPaymentRequestsRequestParams)	 |
| Return Type  | [**PaymentRequestListResponse**](payment_request/PaymentRequestListResponse.md) |

### Request Parameters - GetAllPaymentRequestsRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **for_user_id** | **str**| |  |
| **reference_id** | **[str]**| |  |
| **id** | **[str]**| |  |
| **customer_id** | **[str]**| |  |
| **limit** | **int**| |  |
| **before_id** | **str**| |  |
| **after_id** | **str**| |  |

### Usage Example
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
for_user_id = "5f9a3fbd571a1c4068aa40cf" # str 
reference_id = [
        "reference_id_example",
    ] # [str] 
id = [
        "id_example",
    ] # [str] 
customer_id = [
        "customer_id_example",
    ] # [str] 
limit = 1 # int 
before_id = "before_id_example" # str 
after_id = "after_id_example" # str 

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get all payment requests by filter
    api_response = api_instance.get_all_payment_requests(for_user_id=for_user_id, reference_id=reference_id, id=id, customer_id=customer_id, limit=limit, before_id=before_id, after_id=after_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling PaymentRequestApi->get_all_payment_requests: %s\n" % e)
```

# `capture_payment_request()` Function
> Capture capture_payment_request(payment_request_id)

Payment Request Capture

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `capture_payment_request` |
| Request Parameters  |  [CapturePaymentRequestRequestParams](#request-parameters--CapturePaymentRequestRequestParams)	 |
| Return Type  | [**Capture**](payment_request/Capture.md) |

### Request Parameters - CapturePaymentRequestRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **payment_request_id** | **str** | ☑️ | |
| **for_user_id** | **str**| |  |
| **capture_parameters** | [**CaptureParameters**](payment_request/CaptureParameters.md)| |  |

### Usage Example
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
payment_request_id = "pr-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str 
for_user_id = "5f9a3fbd571a1c4068aa40cf" # str 
capture_parameters = CaptureParameters(
        reference_id="reference_id_example",
        capture_amount=3.14,
    ) # CaptureParameters 

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

# `authorize_payment_request()` Function
> PaymentRequest authorize_payment_request(payment_request_id)

Payment Request Authorize

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `authorize_payment_request` |
| Request Parameters  |  [AuthorizePaymentRequestRequestParams](#request-parameters--AuthorizePaymentRequestRequestParams)	 |
| Return Type  | [**PaymentRequest**](payment_request/PaymentRequest.md) |

### Request Parameters - AuthorizePaymentRequestRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **payment_request_id** | **str** | ☑️ | |
| **for_user_id** | **str**| |  |
| **payment_request_auth_parameters** | [**PaymentRequestAuthParameters**](payment_request/PaymentRequestAuthParameters.md)| |  |

### Usage Example
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
payment_request_id = "pr-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str 
for_user_id = "5f9a3fbd571a1c4068aa40cf" # str 
payment_request_auth_parameters = PaymentRequestAuthParameters(
        auth_code="auth_code_example",
    ) # PaymentRequestAuthParameters 

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

# `resend_payment_request_auth()` Function
> PaymentRequest resend_payment_request_auth(payment_request_id)

Payment Request Resend Auth

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `resend_payment_request_auth` |
| Request Parameters  |  [ResendPaymentRequestAuthRequestParams](#request-parameters--ResendPaymentRequestAuthRequestParams)	 |
| Return Type  | [**PaymentRequest**](payment_request/PaymentRequest.md) |

### Request Parameters - ResendPaymentRequestAuthRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **payment_request_id** | **str** | ☑️ | |
| **for_user_id** | **str**| |  |

### Usage Example
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
payment_request_id = "pr-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str 
for_user_id = "5f9a3fbd571a1c4068aa40cf" # str 

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


## Callback Objects
Use the following callback objects provided by Xendit to receive callbacks (also known as webhooks) that Xendit sends you on events, such as successful payments. Note that the example is meant to illustrate the contents of the callback object -- you will not need to instantiate these objects in practice
### PaymentCallback Object
>Callback for successful or failed payments made via the Payments API

Model Documentation: [PaymentCallback](payment_request/PaymentCallback.md)
#### Usage Example
Note that the example is meant to illustrate the contents of the callback object -- you will not need to instantiate these objects in practice
```python
import xendit
from xendit.payment_request.model import PaymentCallback
import json
from pprint import pprint

payment_callback_obj = {
  "event" : "payment.succeeded",
  "data" : {
    "id" : "ddpy-3cd658ae-25b9-4659-aa36-596ae41a809f",
    "amount" : 1000,
    "status" : "SUCCEEDED",
    "country" : "PH",
    "created" : "2022-08-12T13:30:40.9209Z",
    "updated" : "2022-08-12T13:30:58.729373Z",
    "currency" : "PHP",
    "metadata" : {
      "sku" : "ABCDEFGH"
    },
    "customer_id" : "c832697e-a62d-46fa-a383-24930b155e81",
    "reference_id" : "25cfd0f9-baee-44ca-9a12-6debe03f3c22",
    "payment_method" : {
      "id" : "pm-951b1ad9-1fbb-4724-a744-8956ab6ed17f",
      "card" : null,
      "type" : "DIRECT_DEBIT",
      "status" : "ACTIVE",
      "created" : "2022-08-12T13:30:26.579048Z",
      "ewallet" : null,
      "qr_code" : null,
      "updated" : "2022-08-12T13:30:40.221525Z",
      "metadata" : {
        "sku" : "ABCDEFGH"
      },
      "description" : null,
      "reusability" : "MULTIPLE_USE",
      "direct_debit" : {
        "type" : "BANK_ACCOUNT",
        "debit_card" : null,
        "bank_account" : {
          "bank_account_hash" : "b4dfa99c9b60c77f2e3962b73c098945",
          "masked_bank_account_number" : "XXXXXX1234"
        },
        "channel_code" : "BPI",
        "channel_properties" : {
          "failure_return_url" : "https://your-redirect-website.com/failure",
          "success_return_url" : "https://your-redirect-website.com/success"
        }
      },
      "reference_id" : "620b9df4-fe69-4bfd-b9d4-5cba6861db8a",
      "virtual_account" : null,
      "over_the_counter" : null,
      "direct_bank_transfer" : null
    },
    "description" : null,
    "failure_code" : null,
    "payment_detail" : null,
    "channel_properties" : null,
    "payment_request_id" : "pr-5b26cae1-545b-49e9-855e-f85128f3e705"
  },
  "created" : "2022-08-12T13:30:58.986Z",
  "business_id" : "5f27a14a9bf05c73dd040bc8",
  "api_version" : null
}
payment_callback_json = json.dumps(payment_callback_obj)
```

You may then use the callback object in your webhook or callback handler like so,
```python
def SimulatePaymentCallback(payment_callback_json) {
    callback_obj = PaymentCallback(**json.loads(payment_callback_json))
    // do things here with the callback
}
```
[[Back to README]](../README.md)
