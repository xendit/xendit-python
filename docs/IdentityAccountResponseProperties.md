# xendit.customer.model.IdentityAccountResponseProperties


## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **account_number** | **str** | Unique account identifier as per the bank records. | [optional]  |
| **account_holder_name** | **str, none_type** | Name of account holder as per the cardless credit account. | [optional]  |
| **swift_code** | **str, none_type** | The SWIFT code for international payments | [optional]  |
| **account_type** | **str, none_type** | Free text account type, e.g., Savings, Transaction, Virtual Account. | [optional]  |
| **account_details** | **str, none_type** | Potentially masked account detail, for display purposes only. | [optional]  |
| **currency** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional]  |
| **token_id** | **str** | The token id returned in tokenisation | [optional]  |
| **payment_code** | **str** | Complete fixed payment code (including prefix) | [optional]  |
| **expires_at** | **str, none_type** | YYYY-MM-DD string with expiry date for the payment code | [optional]  |
| **qr_string** | **str** | String representation of the QR Code image | [optional]  |
| **account_id** | **str** | Alphanumeric string identifying this account. Usually an email address or phone number. | [optional]  |


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


