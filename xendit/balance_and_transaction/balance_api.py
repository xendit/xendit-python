"""
    Transaction Service V4 API

    # Introduction This specification describes how to use the Transaction Service V4 API.   **Transaction Service** is the service that records the customer transactions and is responsible to calculate their balance.  All products that move customer money around whether it is money-in, money-out, or transfer will interact with the Transaction Service on its flow. Transaction Service is the source of truth of Xendit and Customer regarding how much money that customer has that is stored in Xendit. Transaction Service is the source that is used for both our internal and customer financial reconciliation. Internally, the Transaction Service data structure is similar to how double-entry accounting works.  ## How Xendit teams/services do integrate with Transaction Service V4   **Channel product team/service** They interact with the Transaction Service when they want to record the transactions. This transaction can be money-in (balance added), money-out (balance deducted), transfer, refund/void/reversal, or other kind of transaction that affects customer balance. Product team also interacts with the Transaction Service for getting information about the transaction or balance.  **Billing/Fee team/service** They interact with Transaction Service either as the dependency of Transaction Service for getting the correct fee calculation/settings. Or using Transaction Service for getting the transaction/fee information to calculate the bill for the customer.  **NUX team/service** They interact with the Transaction Service to set up the customer ledger_account that is used to record their transactions.  **Finance team/service** They interact with the Transaction Service to get the transaction and balance data for each customer to do reconciliation.  **Dashboard/API team/service** They interact with the Transaction Service as a proxy to show the data to the Customer.  ## Prerequisites  Before staring to use **Transaction Service API** you need to complete a few things: 1. Find out **Base URL** for the API. Every endpoint definition in this document contains list of available servers (local, staging, production) 2. Set up ledger accounts using business id and currency. **Ledger Account** represents the account of the customer that will be used to associate with ledger lines. Each business may have at least 1 ledger account group (a group consists of a few accounts of types such as cash, liability, holding), and the money movement of their ledger will revolve around those ledger accounts. **Ledger Lines** that show a debit or credit transaction for a ledger account. We’re using the double-entry principle in accounting where we should post 2 lines every time we make a transaction, 1 to debit an account and 1 to credit another account. See how to call <a href=\"#operation/setupLedgerAccounts\">Create cash, liability, holding, and tax account for a business (api/ledger-accounts/setup)</a> section of this document 3. To be able to create payments with fee/VAT the Product rate settings and VAT rate settings should be created using Transaction Fee Service. See <a href=\"https://docs.google.com/document/d/1HrrA4GhWD1DaJS5dn0dh9VyMhLR6TOUMW1qhRUZ9d_k/edit?pli=1#heading=h.518me3lwf8rb\">Fee Service Documentation</a> for details about how to create Product/VAT rate settings.   ## Transaction flows  To integrate with the Transaction Service you should decide what types of transaction flows your integration will be using. Transaction flow is set by the transaction `type` during transaction creation  1. Money In flows     1. Payment from credit card           `type: CREDIT_CARD_PAYMENT`           3. Payment from other sources without fee/VAT           `type: DEPOSIT, FOREX_DEPOSIT, ISSUING_FUNDING_REFUND, BNPL_PARTNER_SETTLEMENT_CREDIT, PROMO_FEE_CASHBACK, PROMO_VAT_CASHBACK, BATCH_VA_PAYMENT`           4. Payment from other sources with fee/VAT           `type: VA_PAYMENT, IM_ESCROW_VA_PAYMENT, IM_DEPOSIT, RO_PAYMENT, EWALLET_PAYMENT, CARDLESS_CREDIT_PAYMENT, IM_REMITTANCE_VA_PAYMENT, PAYLATER_PAYMENT, INVOICE, QR_CODE_PAYMENT, DIRECT_DEBIT_PAYMENT, DIRECT_BANK_TRANSFER, ACH_PAYMENT, CRYPTO_PAYMENT`           5. Billing deposit from cash           `type: BILLING_DEPOSIT`           6. Billing deposit from other sources           `type: BILLING_DIRECT_DEPOSIT, BILLING_VA_DIRECT_DEPOSIT`       2. Money out flows     1. Instant payment           `type: simple money out types`              `status: COMPLETED`           2. Simple payment without fee/VAT           `type: CHARGEBACK_DEDUCTION, FRAUD_DEDUCTION, LOAN_REPAYMENT, FOREX_DEDUCTION, BNPL_PARTNER_SETTLEMENT_DEBIT, WITHDRAWAL`       3. Simple payment with fee/VAT           `type: ISSUING_FUNDING, BATCH_DISBURSEMENT, CASH_DISBURSEMENT, DISBURSEMENT, REMITTANCE, REMITTANCE_PAYOUT, TAX_DISBURSEMENT`           4. Billing withdraw to cash           `type: BILLING_WITHDRAWAL`           4. Billing withdraw to other destinations           `type: BILL_PAYMENT`       3. Reversal flow      Some of transactions could be reversed. See <a href=\"#section/Introduction/Reversible-non-reversible-transaction-types\">Reversible / non reversible transaction types</a> section of this document. To reverse transaction you should call <a href=\"#operation/updateTransaction\">Update transaction (/api/transactions/:id)</a>  endpoint with the transaction status `REVERSED`.    4. Void/Cancellation Flow      Transaction in the `PENDING_SETTLEMENT` status could be canceled. To do that you should call <a href=\"#operation/updateTransaction\">Update transaction (/api/transactions/:id)</a>  endpoint with the transaction status `VOIDED`.       5. Switcher flow      Switchers are transactions that do not affect the customer balance. These are transactions that goes directly to the customers’ account and simply passes through Xendit. Therefore, it will not impact the customer balance and we will only charge Fee and VAT. To create switcher flow you should set `is_switcher_payment` field to `true`.       ## Instant/non instant settlement  Transactions can be performed instantly (instant settlement) or with delay (non instant settlement).  Some of the transaction types are only instantly processed, some of them support both instant and non instant settlement and some of them have only non instant settlement. If settlement is instant than balance will be changed instantly. In opposite case the transaction status has to be set into PENDING_SETTLEMENT and settlement date should be provided.   1. Instant settlement Money In transaction types      `DEPOSIT, BATCH_VA_PAYMENT, FOREX_DEPOSIT, IM_DEPOSIT, CARDLESS_CREDIT_PAYMENT, ISSUING_FUNDING_REFUND, BNPL_PARTNER_SETTLEMENT_CREDIT, PROMO_FEE_CASHBACK, PROMO_VAT_CASHBACK, REMITTANCE_VA_PAYMENT_CLAIM`    2. Both instant and non instant Money In transaction types      `DIRECT_DEBIT_PAYMENT, DIRECT_BANK_TRANSFER, ACH_PAYMENT, RO_PAYMENT, EWALLET_PAYMENT, QR_CODE_PAYMENT, VA_PAYMENT, INVOICE, PAYLATER_PAYMENT`  3. Non Instant settlement Money In transaction types      `CREDIT_CARD_PAYMENT`    4. Instant settlement Money Out transaction types      `LOAN_REPAYMENT, FOREX_DEDUCTION, BILL_PAYMENT, ISSUING_FUNDING, BNPL_PARTNER_SETTLEMENT_DEBIT, FRAUD_DEDUCTION`  5. Both instant and non instant settlement supported Money Out transaction types      `CHARGEBACK_DEDUCTION`  6. Non Instant settlement Money Out transaction types      All other money out types are non instant settlement  ## Reversible / non reversible transaction types  Some transactions can be reversed. Here are the list of transaction types that could be reversed:   `CASH_DISBURSEMENT, DISBURSEMENT, BATCH_DISBURSEMENT, REMITTANCE, REMITTANCE_PAYOUT, TAX_DISBURSEMENT, WITHDRAWAL, DEPOSIT, FOREX_DEPOSIT, FOREX_DEDUCTION, VA_PAYMENT, BATCH_VA_PAYMENT, IM_REMITTANCE_VA_PAYMENT, IM_ESCROW_VA_PAYMENT, IM_DEPOSIT, REMITTANCE_VA_PAYMENT, REMITTANCE_VA_PAYMENT_CLAIM, RO_PAYMENT, CARDLESS_CREDIT_PAYMENT, PAYLATER_PAYMENT, INVOICE, QR_CODE_PAYMENT, CREDIT_CARD_PAYMENT, EWALLET_PAYMENT, DIRECT_DEBIT_PAYMENT, DIRECT_BANK_TRANSFER, ACH_PAYMENT, CHARGEBACK_DEDUCTION, FRAUD_DEDUCTION, LOAN_REPAYMENT, ISSUING_FUNDING, ISSUING_FUNDING_REFUND, BNPL_PARTNER_SETTLEMENT_DEBIT, BNPL_PARTNER_SETTLEMENT_CREDIT, BILLING_DEPOSIT, BILLING_DIRECT_DEPOSIT, BILLING_VA_DIRECT_DEPOSIT, BILLING_WITHDRAWAL, BILL_PAYMENT, PROMO_FEE_CASHBACK, PROMO_VAT_CASHBACK`       ## How to create transaction  After you created or already have the `BUSINESS_CASH` ledger account ID (See <a href=\"#section/Introduction/Prerequisites\">Prerequisites</a> section) and you know what transaction flows are going to be used  you can create the new transaction using POST request to the  <a href=\"#operation/createTransaction\">Create a new transaction (/api/transactions)</a>  endpoint  ## How to update transaction  To update transaction you should do  PATCH request to the  <a href=\"#operation/updateTransaction\">Update transaction (/api/transactions/::id)</a>  endpoint     # noqa: E501

    The version of the OpenAPI document: 3.4.1
"""

import re  # noqa: F401
import sys  # noqa: F401

from xendit.api_client import ApiClient, Endpoint as _Endpoint
from xendit.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)

from xendit.balance_and_transaction.model import *  # noqa: F401,E501

class BalanceApi(object):
    """NOTE: This class is auto generated by the OpenAPI Generator.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_balance_endpoint = _Endpoint(
            settings={
                'response_type': (Balance,),
                'auth': [],
                'endpoint_path': '/balance',
                'operation_id': 'get_balance',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'account_type',
                    'currency',
                    'for_user_id',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'account_type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('account_type',): {

                        "CASH": "CASH",
                        "HOLDING": "HOLDING",
                        "TAX": "TAX"
                    },
                },
                'openapi_types': {
                    'account_type':
                        (str,),
                    'currency':
                        (str,),
                    'for_user_id':
                        (str,),
                },
                'attribute_map': {
                    'account_type': 'account_type',
                    'currency': 'currency',
                    'for_user_id': 'for-user-id',
                },
                'location_map': {
                    'account_type': 'query',
                    'currency': 'query',
                    'for_user_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_balance(
        self,
        **kwargs
    ):
        """Retrieves balances for a business, default to CASH type  # noqa: E501

        Retrieves balance for your business, defaults to CASH type  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_balance(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            account_type (str): The selected balance type. [optional] if omitted the server will use the default value of "CASH"
            currency (str): Currency for filter for customers with multi currency accounts. [optional]
            for_user_id (str): The sub-account user-id that you want to make this transaction for. This header is only used if you have access to xenPlatform. See xenPlatform for more information. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Balance
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.get_balance_endpoint.call_with_http_info(**kwargs)

