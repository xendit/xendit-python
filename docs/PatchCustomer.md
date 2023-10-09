# xendit.customer.model.PatchCustomer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_name** | **str, none_type** | Entity&#39;s name for this client | [optional] 
**reference_id** | **str, none_type** | Merchant&#39;s reference of this end customer, eg Merchant&#39;s user&#39;s id. Must be unique. | [optional] 
**individual_detail** | [**IndividualDetail**](IndividualDetail.md) |  | [optional] 
**business_detail** | [**BusinessDetail**](BusinessDetail.md) |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**email** | **str, none_type** |  | [optional] 
**mobile_number** | **str, none_type** |  | [optional] 
**phone_number** | **str, none_type** |  | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**addresses** | [**[AddressRequest], none_type**](AddressRequest.md) |  | [optional] 
**identity_accounts** | [**[IdentityAccountRequest], none_type**](IdentityAccountRequest.md) |  | [optional] 
**kyc_documents** | [**[KYCDocumentRequest], none_type**](KYCDocumentRequest.md) |  | [optional] 
**status** | [**EndCustomerStatus**](EndCustomerStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


