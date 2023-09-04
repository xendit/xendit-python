# xendit.payment_method.model.PaymentMethod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**business_id** | **str** |  | [optional] 
**type** | [**PaymentMethodType**](PaymentMethodType.md) |  | [optional] 
**country** | [**PaymentMethodCountry**](PaymentMethodCountry.md) |  | [optional] 
**customer_id** | **str, none_type** |  | [optional] 
**customer** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**reference_id** | **str** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**status** | [**PaymentMethodStatus**](PaymentMethodStatus.md) |  | [optional] 
**reusability** | [**PaymentMethodReusability**](PaymentMethodReusability.md) |  | [optional] 
**actions** | [**[PaymentMethodAction]**](PaymentMethodAction.md) |  | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**billing_information** | [**BillingInformation**](BillingInformation.md) |  | [optional] 
**failure_code** | **str, none_type** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**ewallet** | [**EWallet**](EWallet.md) |  | [optional] 
**direct_debit** | [**DirectDebit**](DirectDebit.md) |  | [optional] 
**over_the_counter** | [**OverTheCounter**](OverTheCounter.md) |  | [optional] 
**card** | [**Card**](Card.md) |  | [optional] 
**qr_code** | [**QRCode**](QRCode.md) |  | [optional] 
**virtual_account** | [**VirtualAccount**](VirtualAccount.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


