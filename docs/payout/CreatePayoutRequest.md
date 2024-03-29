# CreatePayoutRequest
> xendit.payout.model.CreatePayoutRequest

Information needed by Xendit to send money to the destination channel provided

## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **reference_id** | **str** | ☑️ | A client defined payout identifier |  | |
| **channel_code** | **str** | ☑️ | Channel code of selected destination bank or e-wallet |  | |
| **channel_properties** | [**DigitalPayoutChannelProperties**](DigitalPayoutChannelProperties.md) | ☑️ |  |  | |
| **amount** | **float** | ☑️ | Amount to be sent to the destination account and should be a multiple of the minimum increment for the selected channel |  | |
| **currency** | **str** | ☑️ | Currency of the destination channel using ISO-4217 currency code |  | |
| **description** | **str** | | Description to send with the payout, the recipient may see this e.g., in their bank statement (if supported) or in email receipts we send on your behalf  |  |
| **receipt_notification** | [**ReceiptNotification**](ReceiptNotification.md) | |   |  |
| **metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | | Object of additional information you may use  |  |


[[Back to README]](../../README.md)


