# EWalletChannelProperties
> xendit.payment_method.model.EWalletChannelProperties

EWallet Channel Properties

## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **success_return_url** | **str** | | URL where the end-customer is redirected if the authorization is successful  |  |
| **failure_return_url** | **str** | | URL where the end-customer is redirected if the authorization failed  |  |
| **cancel_return_url** | **str** | | URL where the end-customer is redirected if the authorization cancelled  |  |
| **mobile_number** | **str** | | Mobile number of customer in E.164 format (e.g. +628123123123). For OVO one time payment use only.  |  |
| **redeem_points** | **str** | | REDEEM_NONE will not use any point, REDEEM_ALL will use all available points before cash balance is used. For OVO and ShopeePay tokenized payment use only.  |  |
| **cashtag** | **str** | | Available for JENIUSPAY only  |  |


[[Back to README]](../../README.md)


