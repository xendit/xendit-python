# PaymentMethod
> xendit.payment_request.model.PaymentMethod


## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **id** | **str** | ☑️ |  |  | |
| **type** | [**PaymentMethodType**](PaymentMethodType.md) | ☑️ |  |  | |
| **reusability** | [**PaymentMethodReusability**](PaymentMethodReusability.md) | ☑️ |  |  | |
| **status** | [**PaymentMethodStatus**](PaymentMethodStatus.md) | ☑️ |  |  | |
| **created** | **str** | |   |  |
| **updated** | **str** | |   |  |
| **description** | **str, none_type** | |   |  |
| **reference_id** | **str** | |   |  |
| **card** | [**Card**](Card.md) | |   |  |
| **direct_debit** | [**DirectDebit**](DirectDebit.md) | |   |  |
| **ewallet** | [**EWallet**](EWallet.md) | |   |  |
| **over_the_counter** | [**OverTheCounter**](OverTheCounter.md) | |   |  |
| **virtual_account** | [**VirtualAccount**](VirtualAccount.md) | |   |  |
| **qr_code** | [**QRCode**](QRCode.md) | |   |  |
| **metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | |   |  |


[[Back to README]](../../README.md)


