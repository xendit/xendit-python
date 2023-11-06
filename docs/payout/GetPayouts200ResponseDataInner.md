# GetPayouts200ResponseDataInner
> xendit.payout.model.GetPayouts200ResponseDataInner


## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **description** | **str** | | Description to send with the payout, the recipient may see this e.g., in their bank statement (if supported) or in email receipts we send on your behalf  |  |
| **receipt_notification** | [**ReceiptNotification**](ReceiptNotification.md) | |   |  |
| **metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | | Object of additional information you may use  |  |
| **failure_code** | **str** | | If the Payout failed, we include a failure code for more details on the failure.  |  |
| **estimated_arrival_time** | **datetime** | | Our estimated time on to when your payout is reflected to the destination account  |  |
| **reference_id** | **str** | | A client defined payout identifier  |  |
| **channel_code** | **str** | | Channel code of selected destination bank or e-wallet  |  |
| **channel_properties** | [**DigitalPayoutChannelProperties**](DigitalPayoutChannelProperties.md) | |   |  |
| **amount** | **float** | | Amount to be sent to the destination account and should be a multiple of the minimum increment for the selected channel  |  |
| **currency** | **str** | | Currency of the destination channel using ISO-4217 currency code  |  |
| **id** | **str** | | Xendit-generated unique identifier for each payout  |  |
| **created** | **datetime** | | The time payout was created on Xendit&#39;s system, in ISO 8601 format  |  |
| **updated** | **datetime** | | The time payout was last updated on Xendit&#39;s system, in ISO 8601 format  |  |
| **business_id** | **str** | | Xendit Business ID  |  |
| **status** | **str** | | Status of payout  |  |


[[Back to README]](../../README.md)


