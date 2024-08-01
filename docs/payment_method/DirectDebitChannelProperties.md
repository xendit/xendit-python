# DirectDebitChannelProperties
> xendit.payment_method.model.DirectDebitChannelProperties

Direct Debit Channel Properties

## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **success_return_url** | **str** | |   |  |
| **failure_return_url** | **str, none_type** | |   |  |
| **mobile_number** | **str, none_type** | | Mobile number of the customer registered to the partner channel  |  |
| **card_last_four** | **str, none_type** | | Last four digits of the debit card  |  |
| **card_expiry** | **str, none_type** | | Expiry month and year of the debit card (in MM/YY format)  |  |
| **email** | **str, none_type** | | Email address of the customer that is registered to the partner channel  |  |
| **identity_document_number** | **str, none_type** | | Identity number of the customer registered to the partner channel  |  |
| **require_auth** | **bool, none_type** | |   |  |
| **account_number** | **str, none_type** | | Account number of the customer  |  |
| **destination_account_id** | **str, none_type** | | Destination Account ID for BaaS topups  |  |


[[Back to README]](../../README.md)


