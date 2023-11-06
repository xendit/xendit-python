# PaymentRequestParameters
> xendit.payment_request.model.PaymentRequestParameters


## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **currency** | [**PaymentRequestCurrency**](PaymentRequestCurrency.md) | ☑️ |  |  | |
| **reference_id** | **str** | |   |  |
| **amount** | **float** | |   |  |
| **payment_method** | [**PaymentMethodParameters**](PaymentMethodParameters.md) | |   |  |
| **description** | **str, none_type** | |   |  |
| **capture_method** | [**PaymentRequestCaptureMethod**](PaymentRequestCaptureMethod.md) | |   |  |
| **initiator** | [**PaymentRequestInitiator**](PaymentRequestInitiator.md) | |   |  |
| **payment_method_id** | **str** | |   |  |
| **channel_properties** | [**PaymentRequestParametersChannelProperties**](PaymentRequestParametersChannelProperties.md) | |   |  |
| **shipping_information** | [**PaymentRequestShippingInformation**](PaymentRequestShippingInformation.md) | |   |  |
| **items** | [**PaymentRequestBasket**](PaymentRequestBasket.md) | |   |  |
| **customer_id** | **str, none_type** | |   |  |
| **customer** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | |   |  |
| **metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | |   |  |


[[Back to README]](../../README.md)


