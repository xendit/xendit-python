# xendit.payout.model.PayoutAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Xendit-generated unique identifier for each payout | 
**created** | **datetime** | The time payout was created on Xendit&#39;s system, in ISO 8601 format | 
**updated** | **datetime** | The time payout was last updated on Xendit&#39;s system, in ISO 8601 format | 
**business_id** | **str** | Xendit Business ID | 
**status** | **str** | Status of payout | 
**failure_code** | **str** | If the Payout failed, we include a failure code for more details on the failure. | [optional] 
**estimated_arrival_time** | **datetime** | Our estimated time on to when your payout is reflected to the destination account | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


