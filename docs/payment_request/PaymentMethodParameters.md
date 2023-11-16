# PaymentMethodParameters
> xendit.payment_request.model.PaymentMethodParameters


## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **type** | [**PaymentMethodType**](PaymentMethodType.md) | ☑️ |  |  | |
| **reusability** | [**PaymentMethodReusability**](PaymentMethodReusability.md) | ☑️ |  |  | |
| **description** | **str, none_type** | |   |  |
| **reference_id** | **str** | |   |  |
| **direct_debit** | [**DirectDebitParameters**](DirectDebitParameters.md) | |   |  |
| **ewallet** | [**EWalletParameters**](EWalletParameters.md) | |   |  |
| **over_the_counter** | [**OverTheCounterParameters**](OverTheCounterParameters.md) | |   |  |
| **virtual_account** | [**VirtualAccountParameters**](VirtualAccountParameters.md) | |   |  |
| **qr_code** | [**QRCodeParameters**](QRCodeParameters.md) | |   |  |


[[Back to README]](../../README.md)


