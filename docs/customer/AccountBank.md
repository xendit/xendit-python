# AccountBank
> xendit.customer.model.AccountBank


## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **account_number** | **str** | | Unique account identifier as per the bank records.  |  |
| **account_holder_name** | **str, none_type** | | Name of account holder as per the bank records. Needs to match the registered account name exactly. .  |  |
| **swift_code** | **str, none_type** | | The SWIFT code for international payments  |  |
| **account_type** | **str, none_type** | | Free text account type, e.g., Savings, Transaction, Virtual Account.  |  |
| **account_details** | **str, none_type** | | Potentially masked account detail, for display purposes only.  |  |
| **currency** | **bool, date, datetime, dict, float, int, list, str, none_type** | |   |  |


[[Back to README]](../../README.md)


