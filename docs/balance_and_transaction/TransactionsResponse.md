# TransactionsResponse
> xendit.balance_and_transaction.model.TransactionsResponse

Returns an array of Transaction Objects. Returns empty array when there is no result.

## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **has_more** | **bool** | ☑️ | Indicates whether there are more items to be queried with &#x60;after_id&#x60; of the last item from the current result. Use the &#x60;links&#x60; to follow to the next result. |  | |
| **data** | [**[TransactionResponse]**](TransactionResponse.md) | ☑️ |  |  | |
| **links** | [**[LinkItem]**](LinkItem.md) | | The links to the next page based on LinkItem if there is next result.  |  |


[[Back to README]](../../README.md)


