# Channel
> xendit.payout.model.Channel

Channel information where you can send the money to

## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **channel_code** | **str** | ☑️ | Destination channel to send the money to, prefixed by ISO-3166 country code |  | |
| **channel_category** | [**ChannelCategory**](ChannelCategory.md) | ☑️ |  |  | |
| **currency** | **str** | ☑️ | Currency of the destination channel using ISO-4217 currency code |  | |
| **channel_name** | **str** | ☑️ | Name of the destination channel |  | |
| **amount_limits** | [**ChannelAmountLimits**](ChannelAmountLimits.md) | ☑️ |  |  | |


[[Back to README]](../../README.md)


