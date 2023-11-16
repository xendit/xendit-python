# PatchCustomer
> xendit.customer.model.PatchCustomer


## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **client_name** | **str, none_type** | | Entity&#39;s name for this client  |  |
| **reference_id** | **str, none_type** | | Merchant&#39;s reference of this end customer, eg Merchant&#39;s user&#39;s id. Must be unique.  |  |
| **individual_detail** | [**IndividualDetail**](IndividualDetail.md) | |   |  |
| **business_detail** | [**BusinessDetail**](BusinessDetail.md) | |   |  |
| **description** | **str, none_type** | |   |  |
| **email** | **str, none_type** | |   |  |
| **mobile_number** | **str, none_type** | |   |  |
| **phone_number** | **str, none_type** | |   |  |
| **metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | |   |  |
| **addresses** | [**[AddressRequest], none_type**](AddressRequest.md) | |   |  |
| **identity_accounts** | [**[IdentityAccountRequest], none_type**](IdentityAccountRequest.md) | |   |  |
| **kyc_documents** | [**[KYCDocumentRequest], none_type**](KYCDocumentRequest.md) | |   |  |
| **status** | [**EndCustomerStatus**](EndCustomerStatus.md) | |   |  |


[[Back to README]](../../README.md)


