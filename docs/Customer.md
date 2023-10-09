# xendit.customer.model.Customer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_id** | **str** | Merchant&#39;s reference of this end customer, eg Merchant&#39;s user&#39;s id. Must be unique. | 
**individual_detail** | [**IndividualDetail**](IndividualDetail.md) |  | 
**business_detail** | [**BusinessDetail**](BusinessDetail.md) |  | 
**description** | **str, none_type** |  | 
**email** | **str, none_type** |  | 
**mobile_number** | **str, none_type** |  | 
**phone_number** | **str, none_type** |  | 
**addresses** | [**[Address], none_type**](Address.md) |  | 
**identity_accounts** | [**[IdentityAccountResponse], none_type**](IdentityAccountResponse.md) |  | 
**kyc_documents** | [**[KYCDocumentResponse], none_type**](KYCDocumentResponse.md) |  | 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | 
**id** | **str** |  | 
**created** | **datetime** |  | 
**updated** | **datetime** |  | 
**type** | **str** |  | defaults to "INDIVIDUAL"
**status** | [**EndCustomerStatus**](EndCustomerStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


