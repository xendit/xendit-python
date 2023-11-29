# CustomerApi


You can use the APIs below to interface with Xendit's `CustomerApi`.
To start using the API, you need to configure the secret key and initiate the client instance.

```python
import time
import xendit
from xendit.apis import CustomerApi

# See configuration.py for a list of all supported configuration parameters.
xendit.set_api_key('XENDIT API KEY')

# Enter a context with an instance of the API client
api_client = xendit.ApiClient()

# Create an instance of the API class
api_instance = CustomerApi(api_client)
```

All URIs are relative to *https://api.xendit.co*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**create_customer**](CustomerApi.md#create_customer-function) | **POST** /customers | Create Customer |
| [**get_customer**](CustomerApi.md#get_customer-function) | **GET** /customers/{id} | Get Customer By ID |
| [**get_customer_by_reference_id**](CustomerApi.md#get_customer_by_reference_id-function) | **GET** /customers | GET customers by reference id |
| [**update_customer**](CustomerApi.md#update_customer-function) | **PATCH** /customers/{id} | Update End Customer Resource |


# `create_customer()` Function
> Customer create_customer()

Create Customer

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `create_customer` |
| Request Parameters  |  [CreateCustomerRequestParams](#request-parameters--CreateCustomerRequestParams)	 |
| Return Type  | [**Customer**](customer/Customer.md) |

### Request Parameters - CreateCustomerRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **idempotency_key** | **str**| |  |
| **for_user_id** | **str**| |  |
| **customer_request** | [**CustomerRequest**](customer/CustomerRequest.md)| |  |

### Usage Example
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
idempotency_key = "idempotency-123" # str | A unique key to prevent processing duplicate requests.
for_user_id = "user-1" # str | The sub-account user-id that you want to make this transaction for.
customer_request = CustomerRequest(
        client_name="AirAsia Indonesia",
        reference_id="reference_id_example",
        type="INDIVIDUAL",
        individual_detail=IndividualDetail(
            given_names="given_names_example",
            given_names_non_roman="given_names_non_roman_example",
            middle_name="middle_name_example",
            surname="surname_example",
            surname_non_roman="surname_non_roman_example",
            mother_maiden_name="mother_maiden_name_example",
            gender="MALE",
            date_of_birth="2017-07-21",
            nationality=CountryCode("ID"),
            place_of_birth="place_of_birth_example",
            employment=EmploymentDetail(
                employer_name="employer_name_example",
                nature_of_business="nature_of_business_example",
                role_description="role_description_example",
            ),
        ),
        business_detail=BusinessDetail(
            business_name="business_name_example",
            business_type="CORPORATION",
            date_of_registration="2017-07-21",
            nature_of_business="nature_of_business_example",
            business_domicile=CountryCode("ID"),
        ),
        description="description_example",
        email="info@xendit.co",
        mobile_number="+6281295412345",
        phone_number="+6281295412345",
        addresses=[
            AddressRequest(
                category="category_example",
                country_code=CountryCode("ID"),
                province_state="province_state_example",
                city="city_example",
                suburb="suburb_example",
                postal_code="postal_code_example",
                line_1="line_1_example",
                line_2="line_2_example",
                status=AddressStatus("ACTIVE"),
                is_primary=False,
            ),
        ],
        identity_accounts=[
            IdentityAccountRequest(
                type=IdentityAccountType("BANK_ACCOUNT"),
                company="company_example",
                description="description_example",
                country=CountryCode("ID"),
                properties=IdentityAccountRequestProperties(None),
            ),
        ],
        kyc_documents=[
            KYCDocumentRequest(
                country=CountryCode("ID"),
                type=KYCDocumentType("BIRTH_CERTIFICATE"),
                sub_type=KYCDocumentSubType("NATIONAL_ID"),
                document_name="KTP",
                document_number="AA123467890",
                expires_at="2017-07-21",
                holder_name="John Doe",
                document_images=[
                    "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwc=",
                ],
            ),
        ],
        metadata={},
    ) # CustomerRequest | Request object for end customer object

# example passing only required values which don't have defaults set
# and optional values
try:
    # Create Customer
    api_response = api_instance.create_customer(idempotency_key=idempotency_key, for_user_id=for_user_id, customer_request=customer_request)
    pprint(api_response)
except xendit.XenditSdkException as e:
    print("Exception when calling CustomerApi->create_customer: %s\n" % e)
```

# `get_customer()` Function
> Customer get_customer(id)

Get Customer By ID

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `get_customer` |
| Request Parameters  |  [GetCustomerRequestParams](#request-parameters--GetCustomerRequestParams)	 |
| Return Type  | [**Customer**](customer/Customer.md) |

### Request Parameters - GetCustomerRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **id** | **str** | ☑️ | |
| **for_user_id** | **str**| |  |

### Usage Example
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
for_user_id = "user-1" # str | The sub-account user-id that you want to make this transaction for.

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

# `get_customer_by_reference_id()` Function
> GetCustomerByReferenceID200Response get_customer_by_reference_id(reference_id)

GET customers by reference id

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `get_customer_by_reference_id` |
| Request Parameters  |  [GetCustomerByReferenceIdRequestParams](#request-parameters--GetCustomerByReferenceIdRequestParams)	 |
| Return Type  | [**GetCustomerByReferenceID200Response**](customer/GetCustomerByReferenceID200Response.md) |

### Request Parameters - GetCustomerByReferenceIdRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **reference_id** | **str** | ☑️ | |
| **for_user_id** | **str**| |  |

### Usage Example
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
for_user_id = "user-1" # str | The sub-account user-id that you want to make this transaction for.

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

# `update_customer()` Function
> Customer update_customer(id)

Update End Customer Resource

| Name          |    Value 	     |
|--------------------|:-------------:|
| Function Name | `update_customer` |
| Request Parameters  |  [UpdateCustomerRequestParams](#request-parameters--UpdateCustomerRequestParams)	 |
| Return Type  | [**Customer**](customer/Customer.md) |

### Request Parameters - UpdateCustomerRequestParams

| Name | Type | Required | Default |
|-------------|:-------------:|:-------------:|-------------|
| **id** | **str** | ☑️ | |
| **for_user_id** | **str**| |  |
| **patch_customer** | [**PatchCustomer**](customer/PatchCustomer.md)| |  |

### Usage Example
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
for_user_id = "user-1" # str | The sub-account user-id that you want to make this transaction for.
patch_customer = PatchCustomer(
        client_name="AirAsia Indonesia",
        reference_id="reference_id_example",
        individual_detail=IndividualDetail(
            given_names="given_names_example",
            given_names_non_roman="given_names_non_roman_example",
            middle_name="middle_name_example",
            surname="surname_example",
            surname_non_roman="surname_non_roman_example",
            mother_maiden_name="mother_maiden_name_example",
            gender="MALE",
            date_of_birth="2017-07-21",
            nationality=CountryCode("ID"),
            place_of_birth="place_of_birth_example",
            employment=EmploymentDetail(
                employer_name="employer_name_example",
                nature_of_business="nature_of_business_example",
                role_description="role_description_example",
            ),
        ),
        business_detail=BusinessDetail(
            business_name="business_name_example",
            business_type="CORPORATION",
            date_of_registration="2017-07-21",
            nature_of_business="nature_of_business_example",
            business_domicile=CountryCode("ID"),
        ),
        description="description_example",
        email="info@xendit.co",
        mobile_number="+6281295412345",
        phone_number="+6281295412345",
        metadata={},
        addresses=[
            AddressRequest(
                category="category_example",
                country_code=CountryCode("ID"),
                province_state="province_state_example",
                city="city_example",
                suburb="suburb_example",
                postal_code="postal_code_example",
                line_1="line_1_example",
                line_2="line_2_example",
                status=AddressStatus("ACTIVE"),
                is_primary=False,
            ),
        ],
        identity_accounts=[
            IdentityAccountRequest(
                type=IdentityAccountType("BANK_ACCOUNT"),
                company="company_example",
                description="description_example",
                country=CountryCode("ID"),
                properties=IdentityAccountRequestProperties(None),
            ),
        ],
        kyc_documents=[
            KYCDocumentRequest(
                country=CountryCode("ID"),
                type=KYCDocumentType("BIRTH_CERTIFICATE"),
                sub_type=KYCDocumentSubType("NATIONAL_ID"),
                document_name="KTP",
                document_number="AA123467890",
                expires_at="2017-07-21",
                holder_name="John Doe",
                document_images=[
                    "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwc=",
                ],
            ),
        ],
        status=EndCustomerStatus("ACTIVE"),
    ) # PatchCustomer | Update Request for end customer object

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


[[Back to README]](../README.md)
