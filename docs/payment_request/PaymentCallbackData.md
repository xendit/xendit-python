# PaymentCallbackData
> xendit.payment_request.model.PaymentCallbackData

Represents the actual funds transaction/attempt made to a payment method

## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **id** | **str** | ☑️ |  |  | |
| **reference_id** | **str** | ☑️ |  |  | |
| **currency** | **str** | ☑️ |  |  | |
| **amount** | **float** | ☑️ |  |  | |
| **country** | **str** | ☑️ |  |  | |
| **status** | **str** | ☑️ |  |  | |
| **payment_method** | [**PaymentMethod**](PaymentMethod.md) | ☑️ |  |  | |
| **created** | **str** | ☑️ |  |  | |
| **updated** | **str** | ☑️ |  |  | |
| **payment_request_id** | **str, none_type** | |   |  |
| **customer_id** | **str, none_type** | |   |  |
| **channel_properties** | [**PaymentRequestChannelProperties**](PaymentRequestChannelProperties.md) | |   |  |
| **payment_detail** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | |   |  |
| **failure_code** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | |   |  |
| **metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | |   |  |


[[Back to README]](../../README.md)


