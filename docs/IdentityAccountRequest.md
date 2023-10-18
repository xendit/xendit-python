# xendit.customer.model.IdentityAccountRequest


## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **type** | [**IdentityAccountType**](IdentityAccountType.md) |  | [optional]  |
| **company** | **str** | The issuing institution associated with the account (e.g., OCBC, GOPAY, 7-11). If adding financial accounts that Xendit supports, we recommend you use the channel_name found at https://xendit.github.io/apireference/#payment-channels for this field | [optional]  |
| **description** | **str** | Free text description of this account | [optional]  |
| **country** | [**CountryCode**](CountryCode.md) |  | [optional]  |
| **properties** | [**IdentityAccountRequestProperties**](IdentityAccountRequestProperties.md) |  | [optional]  |


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


