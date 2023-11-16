# OverTheCounterChannelProperties
> xendit.payment_request.model.OverTheCounterChannelProperties

Over The Counter Channel Properties

## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **customer_name** | **str** | ☑️ | Name of customer. |  | |
| **payment_code** | **str** | | The payment code that you want to assign, e.g 12345. If you do not send one, one will be picked at random.  |  |
| **expires_at** | **datetime** | | The time when the payment code will be expired. The minimum is 2 hours and the maximum is 9 days for 7ELEVEN. Default expired date will be 2 days from payment code generated.  |  |


[[Back to README]](../../README.md)


