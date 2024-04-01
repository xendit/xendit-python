# TokenizedCardInformation
> xendit.payment_method.model.TokenizedCardInformation

Tokenized Card Information

## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **token_id** | **str** | |   |  |
| **masked_card_number** | **str** | | 1st 6 and last 4 digits of the card  |  |
| **cardholder_name** | **str, none_type** | | Cardholder name is optional but recommended for 3DS 2 / AVS verification  |  |
| **expiry_month** | **str** | | Card expiry month in MM format  |  |
| **expiry_year** | **str** | | Card expiry month in YY format  |  |
| **fingerprint** | **str** | | Xendit-generated identifier for the unique card number. Multiple payment method objects can be created for the same account - e.g. if the user first creates a one-time payment request, and then later on creates a multiple-use payment method using the same account.   The fingerprint helps to identify the unique account being used.  |  |
| **type** | **str** | | Whether the card is a credit or debit card  |  |
| **network** | **str** | | Card network - VISA, MASTERCARD, JCB, AMEX, DISCOVER, BCA  |  |
| **country** | **str** | | Country where the card was issued ISO 3166-1 Alpha-2  |  |
| **issuer** | **str** | | Issuer of the card, most often an issuing bank For example, “BCA”, “MANDIRI”  |  |
| **card_number** | **str** | |   |  |
| **one_time_token** | **str** | |   |  |


[[Back to README]](../../README.md)


