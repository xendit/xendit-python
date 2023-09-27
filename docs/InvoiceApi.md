# xendit.apis.InvoiceApi

All URIs are relative to *https://api.xendit.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_invoice**](InvoiceApi.md#create_invoice) | **POST** /v2/invoices/ | Create an invoice
[**expire_invoice**](InvoiceApi.md#expire_invoice) | **POST** /invoices/{invoice_id}/expire! | Manually expire an invoice
[**get_invoice_by_id**](InvoiceApi.md#get_invoice_by_id) | **GET** /v2/invoices/{invoice_id} | Get invoice by invoice id
[**get_invoices**](InvoiceApi.md#get_invoices) | **GET** /v2/invoices | Get all Invoices


# **create_invoice**
> Invoice create_invoice(create_invoice_request)

Create an invoice

### Example


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
    ) # CreateInvoiceRequest | 

# example passing only required values which don't have defaults set
try:
    # Create an invoice
    api_response = api_instance.create_invoice(create_invoice_request)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling InvoiceApi->create_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_invoice_request** | [**CreateInvoiceRequest**](CreateInvoiceRequest.md)|  |

### Return type

[**Invoice**](Invoice.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **expire_invoice**
> Invoice expire_invoice(invoice_id)

Manually expire an invoice

### Example


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

# example passing only required values which don't have defaults set
try:
    # Manually expire an invoice
    api_response = api_instance.expire_invoice(invoice_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling InvoiceApi->expire_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| Invoice ID to be expired |

### Return type

[**Invoice**](Invoice.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_by_id**
> Invoice get_invoice_by_id(invoice_id)

Get invoice by invoice id

### Example


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

# example passing only required values which don't have defaults set
try:
    # Get invoice by invoice id
    api_response = api_instance.get_invoice_by_id(invoice_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling InvoiceApi->get_invoice_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| Invoice ID |

### Return type

[**Invoice**](Invoice.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices**
> [Invoice] get_invoices()

Get all Invoices

### Example


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

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get all Invoices
    api_response = api_instance.get_invoices(external_id=external_id, statuses=statuses, limit=limit, created_after=created_after, created_before=created_before, paid_after=paid_after, paid_before=paid_before, expired_after=expired_after, expired_before=expired_before, last_invoice=last_invoice, client_types=client_types, payment_channels=payment_channels, on_demand_link=on_demand_link, recurring_payment_id=recurring_payment_id)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling InvoiceApi->get_invoices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  | [optional]
 **statuses** | [**[InvoiceStatus]**](InvoiceStatus.md)|  | [optional]
 **limit** | **float**|  | [optional]
 **created_after** | **datetime**|  | [optional]
 **created_before** | **datetime**|  | [optional]
 **paid_after** | **datetime**|  | [optional]
 **paid_before** | **datetime**|  | [optional]
 **expired_after** | **datetime**|  | [optional]
 **expired_before** | **datetime**|  | [optional]
 **last_invoice** | **str**|  | [optional]
 **client_types** | [**[InvoiceClientType]**](InvoiceClientType.md)|  | [optional]
 **payment_channels** | **[str]**|  | [optional]
 **on_demand_link** | **str**|  | [optional]
 **recurring_payment_id** | **str**|  | [optional]

### Return type

[**[Invoice]**](Invoice.md)


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

