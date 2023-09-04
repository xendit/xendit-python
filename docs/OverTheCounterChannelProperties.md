# xendit.payment_request.model.OverTheCounterChannelProperties

Over The Counter Channel Properties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_name** | **str** | Name of customer. | 
**payment_code** | **str** | The payment code that you want to assign, e.g 12345. If you do not send one, one will be picked at random. | [optional] 
**expires_at** | **datetime** | The time when the payment code will be expired. The minimum is 2 hours and the maximum is 9 days for 7ELEVEN. Default expired date will be 2 days from payment code generated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


