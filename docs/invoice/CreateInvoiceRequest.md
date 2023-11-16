# CreateInvoiceRequest
> xendit.invoice.model.CreateInvoiceRequest

An object representing for an invoice creation request.

## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **external_id** | **str** | ☑️ | The external ID of the invoice. |  | |
| **amount** | **float** | ☑️ | The invoice amount. |  | |
| **payer_email** | **str** | | The email address of the payer.  |  |
| **description** | **str** | | A description of the payment.  |  |
| **invoice_duration** | **str** | | The duration of the invoice.  |  |
| **callback_virtual_account_id** | **str** | | The ID of the callback virtual account.  |  |
| **should_send_email** | **bool** | | Indicates whether email notifications should be sent.  |  |
| **customer** | [**CustomerObject**](CustomerObject.md) | |   |  |
| **customer_notification_preference** | [**NotificationPreference**](NotificationPreference.md) | |   |  |
| **success_redirect_url** | **str** | | The URL to redirect to on successful payment.  |  |
| **failure_redirect_url** | **str** | | The URL to redirect to on payment failure.  |  |
| **payment_methods** | **[str]** | | An array of available payment methods.  |  |
| **mid_label** | **str** | | The middle label.  |  |
| **should_authenticate_credit_card** | **bool** | | Indicates whether credit card authentication is required.  |  |
| **currency** | **str** | | The currency of the invoice.  |  |
| **reminder_time** | **float** | | The reminder time.  |  |
| **local** | **str** | | The local.  |  |
| **reminder_time_unit** | **str** | | The unit of the reminder time.  |  |
| **items** | [**[InvoiceItem]**](InvoiceItem.md) | | An array of items included in the invoice.  |  |
| **fees** | [**[InvoiceFee]**](InvoiceFee.md) | | An array of fees associated with the invoice.  |  |


[[Back to README]](../../README.md)


