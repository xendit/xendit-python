# xendit.payment_method.model.EWalletChannelProperties

EWallet Channel Properties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success_return_url** | **str** | URL where the end-customer is redirected if the authorization is successful | [optional] 
**failure_return_url** | **str** | URL where the end-customer is redirected if the authorization failed | [optional] 
**cancel_return_url** | **str** | URL where the end-customer is redirected if the authorization cancelled | [optional] 
**mobile_number** | **str** | Mobile number of customer in E.164 format (e.g. +628123123123). For OVO one time payment use only. | [optional] 
**redeem_points** | **str** | REDEEM_NONE will not use any point, REDEEM_ALL will use all available points before cash balance is used. For OVO and ShopeePay tokenized payment use only. | [optional] 
**cashtag** | **str** | Available for JENIUSPAY only | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


