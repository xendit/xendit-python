# xendit.customer.model.CustomerRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_id** | **str** | Merchant&#39;s reference of this end customer, eg Merchant&#39;s user&#39;s id. Must be unique. | 
**client_name** | **str** | Entity&#39;s name for this client | [optional] 
**type** | **str** |  | [optional]  if omitted the server will use the default value of "INDIVIDUAL"
**individual_detail** | [**IndividualDetail**](IndividualDetail.md) |  | [optional] 
**business_detail** | [**BusinessDetail**](BusinessDetail.md) |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**email** | **str** |  | [optional] 
**mobile_number** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**addresses** | [**[AddressRequest]**](AddressRequest.md) |  | [optional] 
**identity_accounts** | [**[IdentityAccountRequest]**](IdentityAccountRequest.md) |  | [optional] 
**kyc_documents** | [**[KYCDocumentRequest]**](KYCDocumentRequest.md) |  | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


