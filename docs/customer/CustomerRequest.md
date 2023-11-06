# CustomerRequest
> xendit.customer.model.CustomerRequest


## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **reference_id** | **str** | ☑️ | Merchant&#39;s reference of this end customer, eg Merchant&#39;s user&#39;s id. Must be unique. |  | |
| **client_name** | **str** | | Entity&#39;s name for this client  |  |
| **type** | **str** | |   | "INDIVIDUAL" |
| **individual_detail** | [**IndividualDetail**](IndividualDetail.md) | |   |  |
| **business_detail** | [**BusinessDetail**](BusinessDetail.md) | |   |  |
| **description** | **str, none_type** | |   |  |
| **email** | **str** | |   |  |
| **mobile_number** | **str** | |   |  |
| **phone_number** | **str** | |   |  |
| **addresses** | [**[AddressRequest]**](AddressRequest.md) | |   |  |
| **identity_accounts** | [**[IdentityAccountRequest]**](IdentityAccountRequest.md) | |   |  |
| **kyc_documents** | [**[KYCDocumentRequest]**](KYCDocumentRequest.md) | |   |  |
| **metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | |   |  |


[[Back to README]](../../README.md)


