# Capture
> xendit.payment_request.model.Capture


## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **id** | **str** | ☑️ |  |  | |
| **payment_request_id** | **str** | ☑️ |  |  | |
| **payment_id** | **str** | ☑️ |  |  | |
| **reference_id** | **str** | ☑️ |  |  | |
| **currency** | **str** | ☑️ |  |  | |
| **authorized_amount** | **float** | ☑️ |  |  | |
| **captured_amount** | **float** | ☑️ |  |  | |
| **status** | **str** | ☑️ |  |  | |
| **payment_method** | [**PaymentMethod**](PaymentMethod.md) | ☑️ |  |  | |
| **failure_code** | **str, none_type** | ☑️ |  |  | |
| **customer_id** | **str, none_type** | ☑️ |  |  | |
| **metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | ☑️ |  |  | |
| **channel_properties** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | ☑️ |  |  | |
| **created** | **str** | ☑️ |  |  | |
| **updated** | **str** | ☑️ |  |  | |


[[Back to README]](../../README.md)


