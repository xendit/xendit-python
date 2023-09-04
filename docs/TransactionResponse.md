# xendit.balance_and_transaction.model.TransactionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**TransactionId**](TransactionId.md) |  | 
**product_id** | **str** | The product_id of the transaction. Product id will have a different prefix for each product. You can use this id to match the transaction from this API to each product API. | 
**type** | [**TransactionResponseType**](TransactionResponseType.md) |  | 
**status** | [**TransactionStatuses**](TransactionStatuses.md) |  | 
**channel_category** | [**ChannelsCategories**](ChannelsCategories.md) |  | 
**channel_code** | **str, none_type** | The channel of the transaction that is used. See [channel codes](https://docs.xendit.co/xendisburse/channel-codes) for the list of available per channel categories. | 
**account_identifier** | **str, none_type** | Account identifier of transaction. The format will be different from each channel. | 
**reference_id** | **str** | customer supplied reference/external_id | 
**currency** | [**Currency**](Currency.md) |  | 
**amount** | **float** | The transaction amount. The number of decimal places will be different for each currency according to ISO 4217. | 
**cashflow** | **str** | Representing whether the transaction is money in or money out For transfer, the transfer out side it will shows up as money out and on transfer in side in will shows up as money-in. Available values are &#x60;MONEY_IN&#x60; for money in and &#x60;MONEY_OUT&#x60; for money out. | 
**business_id** | **str** | The id of business where this transaction belong to | 
**fee** | [**FeeResponse**](FeeResponse.md) |  | 
**created** | **datetime** | Transaction created timestamp (UTC+0) | 
**updated** | **datetime** | Transaction updated timestamp (UTC+0) | 
**settlement_status** | **str, none_type** | The settlement status of the transaction. &#x60;PENDING&#x60; - Transaction amount has not been settled to merchant&#39;s balance. &#x60;SETTLED&#x60; - Transaction has been settled to merchant&#39;s balance | [optional] 
**estimated_settlement_time** | **datetime, none_type** | Estimated settlement time will only apply to money-in transactions. For money-out transaction, the value will be &#x60;NULL&#x60;. Estimated settlement time in which transaction amount will be settled to merchant&#39;s balance. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


