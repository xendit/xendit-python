# InvoiceApi


You can use the APIs below to interface with Xendit's `InvoiceApi`.
To start using the API, you need to configure the secret key and initiate the client instance.

```python
import time
import xendit
from xendit.apis import InvoiceApi

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'
# Enter a context with an instance of the API client
api_client = xendit.ApiClient()

# Create an instance of the API class
api_instance = InvoiceApi(api_client)
```

All URIs are relative to *https://api.xendit.co*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**create_invoice**](InvoiceApi.md#create_invoice-function) | **POST** /v2/invoices/ | Create an invoice |
| [**get_invoice_by_id**](InvoiceApi.md#get_invoice_by_id-function) | **GET** /v2/invoices/{invoice_id} | Get invoice by invoice id |
| [**get_invoices**](InvoiceApi.md#get_invoices-function) | **GET** /v2/invoices | Get all Invoices |
| [**expire_invoice**](InvoiceApi.md#expire_invoice-function) | **POST** /invoices/{invoice_id}/expire! | Manually expire an invoice |


# `create_invoice()` Function
> Invoice create_invoice(create_invoice_request)

Create an invoice

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `create_invoice` |
| Request Parameters  |  [CreateInvoiceRequestParams](#request-parameters--CreateInvoiceRequestParams)	 |
| Return Type  | [**Invoice**](invoice/Invoice.md) |

### Request Parameters - CreateInvoiceRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **create_invoice_request** | [**CreateInvoiceRequest**](invoice/CreateInvoiceRequest.md) | ☑️ | |
| **for_user_id** | **str**| |  |

### Usage Example
#### Create Invoice Request

```python
import time
import xendit
from xendit.apis import InvoiceApi
from xendit.invoice.model.invoice_not_found_error import InvoiceNotFoundError
from xendit.invoice.model.invoice import Invoice
from xendit.invoice.model.bad_request_error import BadRequestError
from xendit.invoice.model.unauthorized_error import UnauthorizedError
from xendit.invoice.model.forbidden_error import ForbiddenError
from xendit.invoice.model.create_invoice_request import CreateInvoiceRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = InvoiceApi(api_client)
create_invoice_request = CreateInvoiceRequest(
        external_id="external_id_example",
        amount=3.14,
        payer_email="payer_email_example",
        description="description_example",
        invoice_duration="invoice_duration_example",
        callback_virtual_account_id="callback_virtual_account_id_example",
        should_send_email=True,
        customer=CustomerObject(
            id="id_example",
            phone_number="phone_number_example",
            given_names="given_names_example",
            surname="surname_example",
            email="email_example",
            mobile_number="mobile_number_example",
            customer_id="customer_id_example",
            addresses=[
                AddressObject(
                    country="country_example",
                    street_line1="street_line1_example",
                    street_line2="street_line2_example",
                    city="city_example",
                    province="province_example",
                    state="state_example",
                    postal_code="postal_code_example",
                ),
            ],
        ),
        customer_notification_preference=NotificationPreference(
            invoice_created=[
                NotificationChannel("email"),
            ],
            invoice_reminder=[
                NotificationChannel("email"),
            ],
            invoice_expired=[
                NotificationChannel("email"),
            ],
            invoice_paid=[
                NotificationChannel("email"),
            ],
        ),
        success_redirect_url="success_redirect_url_example",
        failure_redirect_url="failure_redirect_url_example",
        payment_methods=[
            "payment_methods_example",
        ],
        mid_label="mid_label_example",
        should_authenticate_credit_card=True,
        currency="currency_example",
        reminder_time=3.14,
        local="local_example",
        reminder_time_unit="reminder_time_unit_example",
        items=[
            InvoiceItem(
                name="name_example",
                price=3.14,
                quantity=0,
                reference_id="reference_id_example",
                url="url_example",
                category="category_example",
            ),
        ],
        fees=[
            InvoiceFee(
                type="type_example",
                value=3.14,
            ),
        ],
    ) # CreateInvoiceRequest 
for_user_id = "62efe4c33e45694d63f585f0" # str | Business ID of the sub-account merchant (XP feature)

# example passing only required values which don't have defaults set
try:
    # Create an invoice
    api_response = api_instance.create_invoice(create_invoice_request)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling InvoiceApi->create_invoice: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Create an invoice
    api_response = api_instance.create_invoice(create_invoice_request, for_user_id=for_user_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling InvoiceApi->create_invoice: %s\n" % e)
```

# `get_invoice_by_id()` Function
> Invoice get_invoice_by_id(invoice_id)

Get invoice by invoice id

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `get_invoice_by_id` |
| Request Parameters  |  [GetInvoiceByIdRequestParams](#request-parameters--GetInvoiceByIdRequestParams)	 |
| Return Type  | [**Invoice**](invoice/Invoice.md) |

### Request Parameters - GetInvoiceByIdRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **invoice_id** | **str** | ☑️ | |
| **for_user_id** | **str**| |  |

### Usage Example
```python
import time
import xendit
from xendit.apis import InvoiceApi
from xendit.invoice.model.invoice import Invoice
from xendit.invoice.model.invoice_error404_response_definition import InvoiceError404ResponseDefinition
from xendit.invoice.model.unauthorized_error import UnauthorizedError
from xendit.invoice.model.server_error import ServerError
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = InvoiceApi(api_client)
invoice_id = "62efe4c33e45294d63f585f2" # str | Invoice ID
for_user_id = "62efe4c33e45694d63f585f0" # str | Business ID of the sub-account merchant (XP feature)

# example passing only required values which don't have defaults set
try:
    # Get invoice by invoice id
    api_response = api_instance.get_invoice_by_id(invoice_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling InvoiceApi->get_invoice_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get invoice by invoice id
    api_response = api_instance.get_invoice_by_id(invoice_id, for_user_id=for_user_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling InvoiceApi->get_invoice_by_id: %s\n" % e)
```

# `get_invoices()` Function
> [Invoice] get_invoices()

Get all Invoices

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `get_invoices` |
| Request Parameters  |  [GetInvoicesRequestParams](#request-parameters--GetInvoicesRequestParams)	 |
| Return Type  | [**[Invoice]**](invoice/Invoice.md) |

### Request Parameters - GetInvoicesRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **for_user_id** | **str**| |  |
| **external_id** | **str**| |  |
| **statuses** | [**[InvoiceStatus]**](invoice/InvoiceStatus.md)| |  |
| **limit** | **float**| |  |
| **created_after** | **datetime**| |  |
| **created_before** | **datetime**| |  |
| **paid_after** | **datetime**| |  |
| **paid_before** | **datetime**| |  |
| **expired_after** | **datetime**| |  |
| **expired_before** | **datetime**| |  |
| **last_invoice** | **str**| |  |
| **client_types** | [**[InvoiceClientType]**](invoice/InvoiceClientType.md)| |  |
| **payment_channels** | **[str]**| |  |
| **on_demand_link** | **str**| |  |
| **recurring_payment_id** | **str**| |  |

### Usage Example
```python
import time
import xendit
from xendit.apis import InvoiceApi
from xendit.invoice.model.invoice_status import InvoiceStatus
from xendit.invoice.model.invoice import Invoice
from xendit.invoice.model.invoice_client_type import InvoiceClientType
from xendit.invoice.model.unauthorized_error import UnauthorizedError
from xendit.invoice.model.server_error import ServerError
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = InvoiceApi(api_client)
for_user_id = "62efe4c33e45694d63f585f0" # str | Business ID of the sub-account merchant (XP feature)
external_id = "test-external" # str 
statuses = [
        InvoiceStatus("["PENDING","SETTLED"]"),
    ] # [InvoiceStatus] 
limit = 10 # float 
created_after = dateutil_parser('2016-08-29T09:12:33.001Z') # datetime 
created_before = dateutil_parser('2016-08-29T09:12:33.001Z') # datetime 
paid_after = dateutil_parser('2016-08-29T09:12:33.001Z') # datetime 
paid_before = dateutil_parser('2016-08-29T09:12:33.001Z') # datetime 
expired_after = dateutil_parser('2016-08-29T09:12:33.001Z') # datetime 
expired_before = dateutil_parser('2016-08-29T09:12:33.001Z') # datetime 
last_invoice = "62efe4c33e45294d63f585f2" # str 
client_types = [
        InvoiceClientType("["API_GATEWAY","DASHBOARD"]"),
    ] # [InvoiceClientType] 
payment_channels = ["BNI","BRI"] # [str] 
on_demand_link = "test-link" # str 
recurring_payment_id = "62efe4c33e45294d63f585f2" # str 

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get all Invoices
    api_response = api_instance.get_invoices(for_user_id=for_user_id, external_id=external_id, statuses=statuses, limit=limit, created_after=created_after, created_before=created_before, paid_after=paid_after, paid_before=paid_before, expired_after=expired_after, expired_before=expired_before, last_invoice=last_invoice, client_types=client_types, payment_channels=payment_channels, on_demand_link=on_demand_link, recurring_payment_id=recurring_payment_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling InvoiceApi->get_invoices: %s\n" % e)
```

# `expire_invoice()` Function
> Invoice expire_invoice(invoice_id)

Manually expire an invoice

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `expire_invoice` |
| Request Parameters  |  [ExpireInvoiceRequestParams](#request-parameters--ExpireInvoiceRequestParams)	 |
| Return Type  | [**Invoice**](invoice/Invoice.md) |

### Request Parameters - ExpireInvoiceRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **invoice_id** | **str** | ☑️ | |
| **for_user_id** | **str**| |  |

### Usage Example
```python
import time
import xendit
from xendit.apis import InvoiceApi
from xendit.invoice.model.invoice_not_found_error import InvoiceNotFoundError
from xendit.invoice.model.invoice import Invoice
from xendit.invoice.model.server_error import ServerError
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')


# Enter a context with an instance of the API client
api_client = xendit.ApiClient()
# Create an instance of the API class
api_instance = InvoiceApi(api_client)
invoice_id = "5f4708b7bd394b0400b96276" # str | Invoice ID to be expired
for_user_id = "62efe4c33e45694d63f585f0" # str | Business ID of the sub-account merchant (XP feature)

# example passing only required values which don't have defaults set
try:
    # Manually expire an invoice
    api_response = api_instance.expire_invoice(invoice_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling InvoiceApi->expire_invoice: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Manually expire an invoice
    api_response = api_instance.expire_invoice(invoice_id, for_user_id=for_user_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling InvoiceApi->expire_invoice: %s\n" % e)
```


## Callback Objects
Use the following callback objects provided by Xendit to receive callbacks (also known as webhooks) that Xendit sends you on events, such as successful payments. Note that the example is meant to illustrate the contents of the callback object -- you will not need to instantiate these objects in practice
### InvoiceCallback Object
>Invoice Callback Object

Model Documentation: [InvoiceCallback](invoice/InvoiceCallback.md)
#### Usage Example
Note that the example is meant to illustrate the contents of the callback object -- you will not need to instantiate these objects in practice
```python
import xendit
from xendit.invoice.model import InvoiceCallback
import json
from pprint import pprint

invoice_callback_obj = {
  "id" : "593f4ed1c3d3bb7f39733d83",
  "external_id" : "testing-invoice",
  "user_id" : "5848fdf860053555135587e7",
  "payment_method" : "RETAIL_OUTLET",
  "status" : "PAID",
  "merchant_name" : "Xendit",
  "amount" : 2000000,
  "paid_amount" : 2000000,
  "paid_at" : "2020-01-14T02:32:50.912Z",
  "payer_email" : "test@xendit.co",
  "description" : "Invoice webhook test",
  "created" : "2020-01-13T02:32:49.827Z",
  "updated" : "2020-01-13T02:32:50.912Z",
  "currency" : "IDR",
  "payment_channel" : "ALFAMART",
  "payment_destination" : "TEST815"
}
invoice_callback_json = json.dumps(invoice_callback_obj)
```

You may then use the callback object in your webhook or callback handler like so,
```python
def SimulateInvoiceCallback(invoice_callback_json) {
    callback_obj = InvoiceCallback(**json.loads(invoice_callback_json))
    // do things here with the callback
}
```
[[Back to README]](../README.md)
