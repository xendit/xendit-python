# xendit.payment_request.model.PaymentMethod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | [**PaymentMethodType**](PaymentMethodType.md) |  | 
**reusability** | [**PaymentMethodReusability**](PaymentMethodReusability.md) |  | 
**status** | [**PaymentMethodStatus**](PaymentMethodStatus.md) |  | 
**created** | **str** |  | [optional] 
**updated** | **str** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**reference_id** | **str** |  | [optional] 
**card** | [**Card**](Card.md) |  | [optional] 
**direct_debit** | [**DirectDebit**](DirectDebit.md) |  | [optional] 
**ewallet** | [**EWallet**](EWallet.md) |  | [optional] 
**over_the_counter** | [**OverTheCounter**](OverTheCounter.md) |  | [optional] 
**virtual_account** | [**VirtualAccount**](VirtualAccount.md) |  | [optional] 
**qr_code** | [**QRCode**](QRCode.md) |  | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


