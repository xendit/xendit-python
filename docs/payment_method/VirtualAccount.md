# VirtualAccount
> xendit.payment_method.model.VirtualAccount

Virtual Account Payment Method Details

## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **channel_code** | [**VirtualAccountChannelCode**](VirtualAccountChannelCode.md) | ☑️ |  |  | |
| **channel_properties** | [**VirtualAccountChannelProperties**](VirtualAccountChannelProperties.md) | ☑️ |  |  | |
| **amount** | **float, none_type** | |   |  |
| **min_amount** | **float, none_type** | |   |  |
| **max_amount** | **float, none_type** | |   |  |
| **currency** | **str** | |   |  |
| **alternative_display_types** | **[str]** | | For payments in Vietnam only, alternative display requested for the virtual account  |  |
| **alternative_displays** | [**[VirtualAccountAlternativeDisplay]**](VirtualAccountAlternativeDisplay.md) | |   |  |


[[Back to README]](../../README.md)


