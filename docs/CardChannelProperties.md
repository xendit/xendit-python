# xendit.payment_request.model.CardChannelProperties

Card Channel Properties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **skip_three_d_secure** | **bool, none_type** | To indicate whether to perform 3DS during the linking phase | [optional]  |
| **success_return_url** | **str, none_type** | URL where the end-customer is redirected if the authorization is successful | [optional]  |
| **failure_return_url** | **str, none_type** | URL where the end-customer is redirected if the authorization failed | [optional]  |
| **cardonfile_type** | **str, none_type** | Type of “credential-on-file” / “card-on-file” payment being made. Indicate that this payment uses a previously linked Payment Method for charging. | [optional]  |
| **merchant_id_tag** | **str** | Tag for a Merchant ID that you want to associate this payment with. For merchants using their own MIDs to specify which MID they want to use | [optional]  |


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


