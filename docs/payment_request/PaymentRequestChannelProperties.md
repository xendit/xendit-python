# PaymentRequestChannelProperties
> xendit.payment_request.model.PaymentRequestChannelProperties


## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **success_return_url** | **str** | | URL where the end-customer is redirected if the authorization is successful  |  |
| **failure_return_url** | **str** | | URL where the end-customer is redirected if the authorization failed  |  |
| **cancel_return_url** | **str** | | URL where the end-customer is redirected if the authorization cancelled  |  |
| **redeem_points** | **str** | | REDEEM_NONE will not use any point, REDEEM_ALL will use all available points before cash balance is used. For OVO and ShopeePay tokenized payment use only.  |  |
| **require_auth** | **bool** | | Toggle used to require end-customer to input undergo OTP validation before completing a payment. OTP will always be required for transactions greater than 1,000,000 IDR. For BRI tokenized payment use only.  |  |
| **merchant_id_tag** | **str** | | Tag for a Merchant ID that you want to associate this payment with. For merchants using their own MIDs to specify which MID they want to use   |  |
| **cardonfile_type** | **str, none_type** | | Type of “credential-on-file” / “card-on-file” payment being made. Indicate that this payment uses a previously linked Payment Method for charging.  |  |


[[Back to README]](../../README.md)


