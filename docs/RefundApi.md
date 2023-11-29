# RefundApi


You can use the APIs below to interface with Xendit's `RefundApi`.
To start using the API, you need to configure the secret key and initiate the client instance.

```python
import time
import xendit
from xendit.apis import RefundApi

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')

# Enter a context with an instance of the API client
api_client = xendit.ApiClient()

# Create an instance of the API class
api_instance = RefundApi(api_client)
```

All URIs are relative to *https://api.xendit.co*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**create_refund**](RefundApi.md#create_refund-function) | **POST** /refunds |  |
| [**get_refund**](RefundApi.md#get_refund-function) | **GET** /refunds/{refundID} |  |
| [**get_all_refunds**](RefundApi.md#get_all_refunds-function) | **GET** /refunds |  |
| [**cancel_refund**](RefundApi.md#cancel_refund-function) | **POST** /refunds/{refundID}/cancel |  |


# `create_refund()` Function
> Refund create_refund()



| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `create_refund` |
| Request Parameters  |  [CreateRefundRequestParams](#request-parameters--CreateRefundRequestParams)	 |
| Return Type  | [**Refund**](refund/Refund.md) |

### Request Parameters - CreateRefundRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **idempotency_key** | **str**| |  |
| **for_user_id** | **str**| |  |
| **create_refund** | [**CreateRefund**](refund/CreateRefund.md)| |  |

### Usage Example
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
idempotency_key = "9797b5a6-54ad-4511-80a4-ec451346808b" # str 
for_user_id = "5f9a3fbd571a1c4068aa40ce" # str 
create_refund = CreateRefund(
        payment_request_id="pr-3ece8615-41b7-4983-a3f0-a037430b6036",
        invoice_id="7a2c81d4f9e052a870bf37d2",
        reference_id="order-1234",
        amount=1500,
        currency="PHP",
        reason="CANCELLATION",
        metadata={},
    ) # CreateRefund 

# example passing only required values which don't have defaults set
# and optional values
try:
    api_response = api_instance.create_refund(idempotency_key=idempotency_key, for_user_id=for_user_id, create_refund=create_refund)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling RefundApi->create_refund: %s\n" % e)
```

# `get_refund()` Function
> Refund get_refund(refund_id)



| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `get_refund` |
| Request Parameters  |  [GetRefundRequestParams](#request-parameters--GetRefundRequestParams)	 |
| Return Type  | [**Refund**](refund/Refund.md) |

### Request Parameters - GetRefundRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **refund_id** | **str** | ☑️ | |
| **idempotency_key** | **str**| |  |
| **for_user_id** | **str**| |  |

### Usage Example
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
refund_id = "rfd-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str 
idempotency_key = "9797b5a6-54ad-4511-80a4-ec451346808b" # str 
for_user_id = "5f9a3fbd571a1c4068aa40ce" # str 

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

# `get_all_refunds()` Function
> RefundList get_all_refunds()



| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `get_all_refunds` |
| Request Parameters  |  [GetAllRefundsRequestParams](#request-parameters--GetAllRefundsRequestParams)	 |
| Return Type  | [**RefundList**](refund/RefundList.md) |

### Request Parameters - GetAllRefundsRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **for_user_id** | **str**| |  |
| **payment_request_id** | **str**| |  |
| **invoice_id** | **str**| |  |
| **payment_method_type** | **str**| |  |
| **channel_code** | **str**| |  |
| **limit** | **float**| |  |
| **after_id** | **str**| |  |
| **before_id** | **str**| |  |

### Usage Example
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
for_user_id = "5f9a3fbd571a1c4068aa40ce" # str 
payment_request_id = "payment_request_id_example" # str 
invoice_id = "invoice_id_example" # str 
payment_method_type = "payment_method_type_example" # str 
channel_code = "channel_code_example" # str 
limit = 3.14 # float 
after_id = "after_id_example" # str 
before_id = "before_id_example" # str 

# example passing only required values which don't have defaults set
# and optional values
try:
    api_response = api_instance.get_all_refunds(for_user_id=for_user_id, payment_request_id=payment_request_id, invoice_id=invoice_id, payment_method_type=payment_method_type, channel_code=channel_code, limit=limit, after_id=after_id, before_id=before_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling RefundApi->get_all_refunds: %s\n" % e)
```

# `cancel_refund()` Function
> Refund cancel_refund(refund_id)



| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `cancel_refund` |
| Request Parameters  |  [CancelRefundRequestParams](#request-parameters--CancelRefundRequestParams)	 |
| Return Type  | [**Refund**](refund/Refund.md) |

### Request Parameters - CancelRefundRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **refund_id** | **str** | ☑️ | |
| **idempotency_key** | **str**| |  |
| **for_user_id** | **str**| |  |

### Usage Example
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
refund_id = "rfd-1fdaf346-dd2e-4b6c-b938-124c7167a822" # str 
idempotency_key = "9797b5a6-54ad-4511-80a4-ec451346808b" # str 
for_user_id = "5f9a3fbd571a1c4068aa40ce" # str 

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


## Callback Objects
Use the following callback objects provided by Xendit to receive callbacks (also known as webhooks) that Xendit sends you on events, such as successful payments. Note that the example is meant to illustrate the contents of the callback object -- you will not need to instantiate these objects in practice
### RefundCallback Object
>Callback for successful or failed Refunds made via the Payments API

Model Documentation: [RefundCallback](/RefundCallback.md)
#### Usage Example
Note that the example is meant to illustrate the contents of the callback object -- you will not need to instantiate these objects in practice
```python
import xendit
from xendit.refund.model import RefundCallback
import json
from pprint import pprint

refund_callback_obj = {
  "event" : "refund.succeeded",
  "business_id" : "5f27a14a9bf05c73dd040bc8",
  "created" : "2020-08-29T09:12:33.001Z",
  "data" : {
    "id" : "rfd-6f4a377d-a201-437f-9119-f8b00cbbe857",
    "payment_id" : "ddpy-3cd658ae-25b9-4659-aa36-596ae41a809f",
    "invoice_id" : null,
    "amount" : 10000,
    "payment_method_type" : "DIRECT_DEBIT",
    "channel_code" : "BPI",
    "currency" : "PHP",
    "status" : "SUCCEEDED",
    "reason" : "CANCELLATION",
    "reference_id" : "b2756a1e-e6cd-4352-9a68-0483aa2b6a2",
    "failure_code" : null,
    "refund_fee_amount" : null,
    "created" : "2020-08-30T09:12:33.001Z",
    "updated" : "2020-08-30T09:12:33.001Z",
    "metadata" : null
  }
}
refund_callback_json = json.dumps(refund_callback_obj)
```

You may then use the callback object in your webhook or callback handler like so,
```python
def SimulateRefundCallback(refund_callback_json) {
    callback_obj = RefundCallback(**json.loads(refund_callback_json))
    // do things here with the callback
}
```
[[Back to README]](../README.md)
