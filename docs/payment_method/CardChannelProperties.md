# CardChannelProperties
> xendit.payment_method.model.CardChannelProperties

Card Channel Properties

## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **skip_three_d_secure** | **bool, none_type** | | This field value is only being used for reusability &#x3D; MULTIPLE_USE. To indicate whether to perform 3DS during the linking phase. Defaults to false.  |  |
| **success_return_url** | **str, none_type** | | URL where the end-customer is redirected if the authorization is successful  |  |
| **failure_return_url** | **str, none_type** | | URL where the end-customer is redirected if the authorization failed  |  |
| **cardonfile_type** | **str, none_type** | | Type of “credential-on-file” / “card-on-file” payment being made. Indicate that this payment uses a previously linked Payment Method for charging.  |  |
| **expires_at** | **datetime** | |   |  |
| **installment_configuration** | [**CardInstallmentConfiguration**](CardInstallmentConfiguration.md) | |   |  |
| **merchant_id_tag** | **str** | | Tag for a Merchant ID that you want to associate this payment with. For merchants using their own MIDs to specify which MID they want to use  |  |


[[Back to README]](../../README.md)


