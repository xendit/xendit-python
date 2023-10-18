# xendit.customer.model.AddressRequest


## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **category** | **str** | Home, work or provincial | [optional]  |
| **country_code** | [**CountryCode**](CountryCode.md) |  | [optional]  |
| **province_state** | **str** |  | [optional]  |
| **city** | **str** |  | [optional]  |
| **suburb** | **str** |  | [optional]  |
| **postal_code** | **str** |  | [optional]  |
| **line_1** | **str** |  | [optional]  |
| **line_2** | **str** |  | [optional]  |
| **status** | [**AddressStatus**](AddressStatus.md) |  | [optional]  |
| **is_primary** | **bool** |  | [optional]  if omitted the server will use the default value of False |


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


