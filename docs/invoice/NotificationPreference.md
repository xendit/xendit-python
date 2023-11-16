# NotificationPreference
> xendit.invoice.model.NotificationPreference

An object representing notification preferences for different invoice events.

## Properties
| Name | Type | Required | Description | Examples |
|------------|:-------------:|:-------------:|-------------|:-------------:|
| **invoice_created** | [**[NotificationChannel]**](NotificationChannel.md) | | Notification channels for when an invoice is created.  |  |
| **invoice_reminder** | [**[NotificationChannel]**](NotificationChannel.md) | | Notification channels for invoice reminders.  |  |
| **invoice_expired** | [**[NotificationChannel]**](NotificationChannel.md) | | Notification channels for expired invoices.  |  |
| **invoice_paid** | [**[NotificationChannel]**](NotificationChannel.md) | | Notification channels for when an invoice is paid.  |  |


[[Back to README]](../../README.md)


