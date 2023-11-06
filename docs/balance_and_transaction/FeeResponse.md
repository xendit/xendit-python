# FeeResponse
> xendit.balance_and_transaction.model.FeeResponse


## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **xendit_fee** | **float** | ☑️ | Amount of the Xendit fee for this transaction. |  | |
| **value_added_tax** | **float** | ☑️ | Amount of the VAT for this transaction. |  | |
| **xendit_withholding_tax** | **float** | | Amount of the Xendit Withholding Tax for this transaction if applicable. See [Tax Documentation](https://docs.xendit.co/fees-and-vat#vat) for more information.  |  |
| **third_party_withholding_tax** | **float** | | Amount of the 3rd Party Withholding Tax for this transaction if applicable. 3rd party example: Bank   |  |
| **status** | **str** | |   |  |


[[Back to README]](../../README.md)


