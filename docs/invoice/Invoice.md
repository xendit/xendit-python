# Invoice
> xendit.invoice.model.Invoice

An object representing details for an invoice.

## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **external_id** | **str** | ☑️ | The external identifier for the invoice. |  | |
| **user_id** | **str** | ☑️ | The user ID associated with the invoice. |  | |
| **status** | [**InvoiceStatus**](InvoiceStatus.md) | ☑️ |  |  | |
| **merchant_name** | **str** | ☑️ | The name of the merchant. |  | |
| **merchant_profile_picture_url** | **str** | ☑️ | The URL of the merchant&#39;s profile picture. |  | |
| **amount** | **float** | ☑️ | The total amount of the invoice. |  | |
| **expiry_date** | **datetime** | ☑️ | Representing a date and time in ISO 8601 format. |  | |
| **invoice_url** | **str** | ☑️ | The URL to view the invoice. |  | |
| **available_banks** | [**[Bank]**](Bank.md) | ☑️ | An array of available banks for payment. |  | |
| **available_retail_outlets** | [**[RetailOutlet]**](RetailOutlet.md) | ☑️ | An array of available retail outlets for payment. |  | |
| **available_ewallets** | [**[Ewallet]**](Ewallet.md) | ☑️ | An array of available e-wallets for payment. |  | |
| **available_qr_codes** | [**[QrCode]**](QrCode.md) | ☑️ | An array of available QR codes for payment. |  | |
| **available_direct_debits** | [**[DirectDebit]**](DirectDebit.md) | ☑️ | An array of available direct debit options for payment. |  | |
| **available_paylaters** | [**[Paylater]**](Paylater.md) | ☑️ | An array of available pay-later options for payment. |  | |
| **should_send_email** | **bool** | ☑️ | Indicates whether email notifications should be sent. |  | |
| **created** | **datetime** | ☑️ | Representing a date and time in ISO 8601 format. |  | |
| **updated** | **datetime** | ☑️ | Representing a date and time in ISO 8601 format. |  | |
| **id** | **str** | | The unique identifier for the invoice.  |  |
| **payer_email** | **str** | | The email address of the payer.  |  |
| **description** | **str** | | A description of the invoice.  |  |
| **payment_method** | [**InvoicePaymentMethod**](InvoicePaymentMethod.md) | |   |  |
| **locale** | **str** | | The locale or language used for the invoice.  |  |
| **should_exclude_credit_card** | **bool** | | Indicates whether credit card payments should be excluded.  |  |
| **success_redirect_url** | **str** | | The URL to redirect to on successful payment.  |  |
| **failure_redirect_url** | **str** | | The URL to redirect to on payment failure.  |  |
| **should_authenticate_credit_card** | **bool** | | Indicates whether credit card authentication is required.  |  |
| **currency** | [**InvoiceCurrency**](InvoiceCurrency.md) | |   |  |
| **items** | [**[InvoiceItem]**](InvoiceItem.md) | | An array of items included in the invoice.  |  |
| **fixed_va** | **bool** | | Indicates whether the virtual account is fixed.  |  |
| **reminder_date** | **datetime** | | Representing a date and time in ISO 8601 format.  |  |
| **customer** | [**CustomerObject**](CustomerObject.md) | |   |  |
| **customer_notification_preference** | [**NotificationPreference**](NotificationPreference.md) | |   |  |
| **fees** | [**[InvoiceFee]**](InvoiceFee.md) | | An array of fees associated with the invoice.  |  |


[[Back to README]](../../README.md)


