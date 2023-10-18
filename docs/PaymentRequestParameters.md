# xendit.payment_request.model.PaymentRequestParameters


## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **currency** | [**PaymentRequestCurrency**](PaymentRequestCurrency.md) |  |  |
| **reference_id** | **str** |  | [optional]  |
| **amount** | **float** |  | [optional]  |
| **payment_method** | [**PaymentMethodParameters**](PaymentMethodParameters.md) |  | [optional]  |
| **description** | **str, none_type** |  | [optional]  |
| **capture_method** | [**PaymentRequestCaptureMethod**](PaymentRequestCaptureMethod.md) |  | [optional]  |
| **initiator** | [**PaymentRequestInitiator**](PaymentRequestInitiator.md) |  | [optional]  |
| **payment_method_id** | **str** |  | [optional]  |
| **channel_properties** | [**PaymentRequestParametersChannelProperties**](PaymentRequestParametersChannelProperties.md) |  | [optional]  |
| **shipping_information** | [**PaymentRequestShippingInformation**](PaymentRequestShippingInformation.md) |  | [optional]  |
| **items** | [**PaymentRequestBasket**](PaymentRequestBasket.md) |  | [optional]  |
| **customer_id** | **str, none_type** |  | [optional]  |
| **customer** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional]  |
| **metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional]  |


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


