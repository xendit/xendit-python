# PaymentMethodParameters
> xendit.payment_method.model.PaymentMethodParameters


## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **type** | [**PaymentMethodType**](PaymentMethodType.md) | ☑️ |  |  | |
| **reusability** | [**PaymentMethodReusability**](PaymentMethodReusability.md) | ☑️ |  |  | |
| **country** | **str, none_type** | |   |  |
| **customer_id** | **str, none_type** | |   |  |
| **reference_id** | **str** | |   |  |
| **description** | **str, none_type** | |   |  |
| **card** | [**CardParameters**](CardParameters.md) | |   |  |
| **direct_debit** | [**DirectDebitParameters**](DirectDebitParameters.md) | |   |  |
| **ewallet** | [**EWalletParameters**](EWalletParameters.md) | |   |  |
| **over_the_counter** | [**OverTheCounterParameters**](OverTheCounterParameters.md) | |   |  |
| **virtual_account** | [**VirtualAccountParameters**](VirtualAccountParameters.md) | |   |  |
| **qr_code** | [**QRCodeParameters**](QRCodeParameters.md) | |   |  |
| **metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | |   |  |
| **billing_information** | [**BillingInformation**](BillingInformation.md) | |   |  |


[[Back to README]](../../README.md)


