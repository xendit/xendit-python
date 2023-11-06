# IdentityAccountResponseProperties
> xendit.customer.model.IdentityAccountResponseProperties


## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **account_number** | **str** | | Unique account identifier as per the bank records.  |  |
| **account_holder_name** | **str, none_type** | | Name of account holder as per the cardless credit account.  |  |
| **swift_code** | **str, none_type** | | The SWIFT code for international payments  |  |
| **account_type** | **str, none_type** | | Free text account type, e.g., Savings, Transaction, Virtual Account.  |  |
| **account_details** | **str, none_type** | | Potentially masked account detail, for display purposes only.  |  |
| **currency** | **bool, date, datetime, dict, float, int, list, str, none_type** | |   |  |
| **token_id** | **str** | | The token id returned in tokenisation  |  |
| **payment_code** | **str** | | Complete fixed payment code (including prefix)  |  |
| **expires_at** | **str, none_type** | | YYYY-MM-DD string with expiry date for the payment code  |  |
| **qr_string** | **str** | | String representation of the QR Code image  |  |
| **account_id** | **str** | | Alphanumeric string identifying this account. Usually an email address or phone number.  |  |


[[Back to README]](../../README.md)


