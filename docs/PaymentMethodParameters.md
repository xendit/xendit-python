# xendit.payment_method.model.PaymentMethodParameters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PaymentMethodType**](PaymentMethodType.md) |  | 
**reusability** | [**PaymentMethodReusability**](PaymentMethodReusability.md) |  | 
**country** | **str, none_type** |  | [optional] 
**customer_id** | **str, none_type** |  | [optional] 
**reference_id** | **str** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**card** | [**CardParameters**](CardParameters.md) |  | [optional] 
**direct_debit** | [**DirectDebitParameters**](DirectDebitParameters.md) |  | [optional] 
**ewallet** | [**EWalletParameters**](EWalletParameters.md) |  | [optional] 
**over_the_counter** | [**OverTheCounterParameters**](OverTheCounterParameters.md) |  | [optional] 
**virtual_account** | [**VirtualAccountParameters**](VirtualAccountParameters.md) |  | [optional] 
**qr_code** | [**QRCodeParameters**](QRCodeParameters.md) |  | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**billing_information** | [**BillingInformation**](BillingInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


