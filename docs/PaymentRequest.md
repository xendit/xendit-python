# xendit.payment_request.model.PaymentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created** | **str** |  | 
**updated** | **str** |  | 
**reference_id** | **str** |  | 
**business_id** | **str** |  | 
**currency** | [**PaymentRequestCurrency**](PaymentRequestCurrency.md) |  | 
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | 
**status** | [**PaymentRequestStatus**](PaymentRequestStatus.md) |  | 
**customer_id** | **str, none_type** |  | [optional] 
**customer** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**amount** | **float** |  | [optional] 
**min_amount** | **float, none_type** |  | [optional] 
**max_amount** | **float, none_type** |  | [optional] 
**country** | [**PaymentRequestCountry**](PaymentRequestCountry.md) |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**failure_code** | **str, none_type** |  | [optional] 
**capture_method** | [**PaymentRequestCaptureMethod**](PaymentRequestCaptureMethod.md) |  | [optional] 
**initiator** | [**PaymentRequestInitiator**](PaymentRequestInitiator.md) |  | [optional] 
**card_verification_results** | [**PaymentRequestCardVerificationResults**](PaymentRequestCardVerificationResults.md) |  | [optional] 
**actions** | [**[PaymentRequestAction]**](PaymentRequestAction.md) |  | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**shipping_information** | [**PaymentRequestShippingInformation**](PaymentRequestShippingInformation.md) |  | [optional] 
**items** | [**PaymentRequestBasket**](PaymentRequestBasket.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


