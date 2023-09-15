# xendit.invoice.model.CreateInvoiceRequest

An object representing for an invoice creation request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | The external ID of the invoice. | 
**amount** | **float** | The invoice amount. | 
**payer_email** | **str** | The email address of the payer. | [optional] 
**description** | **str** | A description of the payment. | [optional] 
**invoice_duration** | **str** | The duration of the invoice. | [optional] 
**callback_virtual_account_id** | **str** | The ID of the callback virtual account. | [optional] 
**should_send_email** | **bool** | Indicates whether email notifications should be sent. | [optional] 
**customer** | [**CustomerObject**](CustomerObject.md) |  | [optional] 
**customer_notification_preference** | [**NotificationPreference**](NotificationPreference.md) |  | [optional] 
**success_redirect_url** | **str** | The URL to redirect to on successful payment. | [optional] 
**failure_redirect_url** | **str** | The URL to redirect to on payment failure. | [optional] 
**payment_methods** | **[str]** | An array of available payment methods. | [optional] 
**mid_label** | **str** | The middle label. | [optional] 
**should_authenticate_credit_card** | **bool** | Indicates whether credit card authentication is required. | [optional] 
**currency** | **str** | The currency of the invoice. | [optional] 
**reminder_time** | **float** | The reminder time. | [optional] 
**local** | **str** | The local. | [optional] 
**reminder_time_unit** | **str** | The unit of the reminder time. | [optional] 
**items** | [**[InvoiceItem]**](InvoiceItem.md) | An array of items included in the invoice. | [optional] 
**fees** | [**[InvoiceFee]**](InvoiceFee.md) | An array of fees associated with the invoice. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


