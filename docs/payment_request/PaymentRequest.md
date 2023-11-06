# PaymentRequest
> xendit.payment_request.model.PaymentRequest


## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **id** | **str** | ☑️ |  |  | |
| **created** | **str** | ☑️ |  |  | |
| **updated** | **str** | ☑️ |  |  | |
| **reference_id** | **str** | ☑️ |  |  | |
| **business_id** | **str** | ☑️ |  |  | |
| **currency** | [**PaymentRequestCurrency**](PaymentRequestCurrency.md) | ☑️ |  |  | |
| **payment_method** | [**PaymentMethod**](PaymentMethod.md) | ☑️ |  |  | |
| **status** | [**PaymentRequestStatus**](PaymentRequestStatus.md) | ☑️ |  |  | |
| **customer_id** | **str, none_type** | |   |  |
| **customer** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | |   |  |
| **amount** | **float** | |   |  |
| **min_amount** | **float, none_type** | |   |  |
| **max_amount** | **float, none_type** | |   |  |
| **country** | [**PaymentRequestCountry**](PaymentRequestCountry.md) | |   |  |
| **description** | **str, none_type** | |   |  |
| **failure_code** | **str, none_type** | |   |  |
| **capture_method** | [**PaymentRequestCaptureMethod**](PaymentRequestCaptureMethod.md) | |   |  |
| **initiator** | [**PaymentRequestInitiator**](PaymentRequestInitiator.md) | |   |  |
| **card_verification_results** | [**PaymentRequestCardVerificationResults**](PaymentRequestCardVerificationResults.md) | |   |  |
| **actions** | [**[PaymentRequestAction]**](PaymentRequestAction.md) | |   |  |
| **metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | |   |  |
| **shipping_information** | [**PaymentRequestShippingInformation**](PaymentRequestShippingInformation.md) | |   |  |
| **items** | [**PaymentRequestBasket**](PaymentRequestBasket.md) | |   |  |


[[Back to README]](../../README.md)


