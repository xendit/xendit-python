"""
    Transaction Service V4 API

    # Introduction This specification describes how to use the Transaction Service V4 API.   **Transaction Service** is the service that records the customer transactions and is responsible to calculate their balance.  All products that move customer money around whether it is money-in, money-out, or transfer will interact with the Transaction Service on its flow. Transaction Service is the source of truth of Xendit and Customer regarding how much money that customer has that is stored in Xendit. Transaction Service is the source that is used for both our internal and customer financial reconciliation. Internally, the Transaction Service data structure is similar to how double-entry accounting works.  ## How Xendit teams/services do integrate with Transaction Service V4   **Channel product team/service** They interact with the Transaction Service when they want to record the transactions. This transaction can be money-in (balance added), money-out (balance deducted), transfer, refund/void/reversal, or other kind of transaction that affects customer balance. Product team also interacts with the Transaction Service for getting information about the transaction or balance.  **Billing/Fee team/service** They interact with Transaction Service either as the dependency of Transaction Service for getting the correct fee calculation/settings. Or using Transaction Service for getting the transaction/fee information to calculate the bill for the customer.  **NUX team/service** They interact with the Transaction Service to set up the customer ledger_account that is used to record their transactions.  **Finance team/service** They interact with the Transaction Service to get the transaction and balance data for each customer to do reconciliation.  **Dashboard/API team/service** They interact with the Transaction Service as a proxy to show the data to the Customer.  ## Prerequisites  Before staring to use **Transaction Service API** you need to complete a few things: 1. Find out **Base URL** for the API. Every endpoint definition in this document contains list of available servers (local, staging, production) 2. Set up ledger accounts using business id and currency. **Ledger Account** represents the account of the customer that will be used to associate with ledger lines. Each business may have at least 1 ledger account group (a group consists of a few accounts of types such as cash, liability, holding), and the money movement of their ledger will revolve around those ledger accounts. **Ledger Lines** that show a debit or credit transaction for a ledger account. We’re using the double-entry principle in accounting where we should post 2 lines every time we make a transaction, 1 to debit an account and 1 to credit another account. See how to call <a href=\"#operation/setupLedgerAccounts\">Create cash, liability, holding, and tax account for a business (api/ledger-accounts/setup)</a> section of this document 3. To be able to create payments with fee/VAT the Product rate settings and VAT rate settings should be created using Transaction Fee Service. See <a href=\"https://docs.google.com/document/d/1HrrA4GhWD1DaJS5dn0dh9VyMhLR6TOUMW1qhRUZ9d_k/edit?pli=1#heading=h.518me3lwf8rb\">Fee Service Documentation</a> for details about how to create Product/VAT rate settings.   ## Transaction flows  To integrate with the Transaction Service you should decide what types of transaction flows your integration will be using. Transaction flow is set by the transaction `type` during transaction creation  1. Money In flows     1. Payment from credit card           `type: CREDIT_CARD_PAYMENT`           3. Payment from other sources without fee/VAT           `type: DEPOSIT, FOREX_DEPOSIT, ISSUING_FUNDING_REFUND, BNPL_PARTNER_SETTLEMENT_CREDIT, PROMO_FEE_CASHBACK, PROMO_VAT_CASHBACK, BATCH_VA_PAYMENT`           4. Payment from other sources with fee/VAT           `type: VA_PAYMENT, IM_ESCROW_VA_PAYMENT, IM_DEPOSIT, RO_PAYMENT, EWALLET_PAYMENT, CARDLESS_CREDIT_PAYMENT, IM_REMITTANCE_VA_PAYMENT, PAYLATER_PAYMENT, INVOICE, QR_CODE_PAYMENT, DIRECT_DEBIT_PAYMENT, DIRECT_BANK_TRANSFER, ACH_PAYMENT, CRYPTO_PAYMENT`           5. Billing deposit from cash           `type: BILLING_DEPOSIT`           6. Billing deposit from other sources           `type: BILLING_DIRECT_DEPOSIT, BILLING_VA_DIRECT_DEPOSIT`       2. Money out flows     1. Instant payment           `type: simple money out types`              `status: COMPLETED`           2. Simple payment without fee/VAT           `type: CHARGEBACK_DEDUCTION, FRAUD_DEDUCTION, LOAN_REPAYMENT, FOREX_DEDUCTION, BNPL_PARTNER_SETTLEMENT_DEBIT, WITHDRAWAL`       3. Simple payment with fee/VAT           `type: ISSUING_FUNDING, BATCH_DISBURSEMENT, CASH_DISBURSEMENT, DISBURSEMENT, REMITTANCE, REMITTANCE_PAYOUT, TAX_DISBURSEMENT`           4. Billing withdraw to cash           `type: BILLING_WITHDRAWAL`           4. Billing withdraw to other destinations           `type: BILL_PAYMENT`       3. Reversal flow      Some of transactions could be reversed. See <a href=\"#section/Introduction/Reversible-non-reversible-transaction-types\">Reversible / non reversible transaction types</a> section of this document. To reverse transaction you should call <a href=\"#operation/updateTransaction\">Update transaction (/api/transactions/:id)</a>  endpoint with the transaction status `REVERSED`.    4. Void/Cancellation Flow      Transaction in the `PENDING_SETTLEMENT` status could be canceled. To do that you should call <a href=\"#operation/updateTransaction\">Update transaction (/api/transactions/:id)</a>  endpoint with the transaction status `VOIDED`.       5. Switcher flow      Switchers are transactions that do not affect the customer balance. These are transactions that goes directly to the customers’ account and simply passes through Xendit. Therefore, it will not impact the customer balance and we will only charge Fee and VAT. To create switcher flow you should set `is_switcher_payment` field to `true`.       ## Instant/non instant settlement  Transactions can be performed instantly (instant settlement) or with delay (non instant settlement).  Some of the transaction types are only instantly processed, some of them support both instant and non instant settlement and some of them have only non instant settlement. If settlement is instant than balance will be changed instantly. In opposite case the transaction status has to be set into PENDING_SETTLEMENT and settlement date should be provided.   1. Instant settlement Money In transaction types      `DEPOSIT, BATCH_VA_PAYMENT, FOREX_DEPOSIT, IM_DEPOSIT, CARDLESS_CREDIT_PAYMENT, ISSUING_FUNDING_REFUND, BNPL_PARTNER_SETTLEMENT_CREDIT, PROMO_FEE_CASHBACK, PROMO_VAT_CASHBACK, REMITTANCE_VA_PAYMENT_CLAIM`    2. Both instant and non instant Money In transaction types      `DIRECT_DEBIT_PAYMENT, DIRECT_BANK_TRANSFER, ACH_PAYMENT, RO_PAYMENT, EWALLET_PAYMENT, QR_CODE_PAYMENT, VA_PAYMENT, INVOICE, PAYLATER_PAYMENT`  3. Non Instant settlement Money In transaction types      `CREDIT_CARD_PAYMENT`    4. Instant settlement Money Out transaction types      `LOAN_REPAYMENT, FOREX_DEDUCTION, BILL_PAYMENT, ISSUING_FUNDING, BNPL_PARTNER_SETTLEMENT_DEBIT, FRAUD_DEDUCTION`  5. Both instant and non instant settlement supported Money Out transaction types      `CHARGEBACK_DEDUCTION`  6. Non Instant settlement Money Out transaction types      All other money out types are non instant settlement  ## Reversible / non reversible transaction types  Some transactions can be reversed. Here are the list of transaction types that could be reversed:   `CASH_DISBURSEMENT, DISBURSEMENT, BATCH_DISBURSEMENT, REMITTANCE, REMITTANCE_PAYOUT, TAX_DISBURSEMENT, WITHDRAWAL, DEPOSIT, FOREX_DEPOSIT, FOREX_DEDUCTION, VA_PAYMENT, BATCH_VA_PAYMENT, IM_REMITTANCE_VA_PAYMENT, IM_ESCROW_VA_PAYMENT, IM_DEPOSIT, REMITTANCE_VA_PAYMENT, REMITTANCE_VA_PAYMENT_CLAIM, RO_PAYMENT, CARDLESS_CREDIT_PAYMENT, PAYLATER_PAYMENT, INVOICE, QR_CODE_PAYMENT, CREDIT_CARD_PAYMENT, EWALLET_PAYMENT, DIRECT_DEBIT_PAYMENT, DIRECT_BANK_TRANSFER, ACH_PAYMENT, CHARGEBACK_DEDUCTION, FRAUD_DEDUCTION, LOAN_REPAYMENT, ISSUING_FUNDING, ISSUING_FUNDING_REFUND, BNPL_PARTNER_SETTLEMENT_DEBIT, BNPL_PARTNER_SETTLEMENT_CREDIT, BILLING_DEPOSIT, BILLING_DIRECT_DEPOSIT, BILLING_VA_DIRECT_DEPOSIT, BILLING_WITHDRAWAL, BILL_PAYMENT, PROMO_FEE_CASHBACK, PROMO_VAT_CASHBACK`       ## How to create transaction  After you created or already have the `BUSINESS_CASH` ledger account ID (See <a href=\"#section/Introduction/Prerequisites\">Prerequisites</a> section) and you know what transaction flows are going to be used  you can create the new transaction using POST request to the  <a href=\"#operation/createTransaction\">Create a new transaction (/api/transactions)</a>  endpoint  ## How to update transaction  To update transaction you should do  PATCH request to the  <a href=\"#operation/updateTransaction\">Update transaction (/api/transactions/::id)</a>  endpoint     # noqa: E501

    The version of the OpenAPI document: 3.5.2
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
from typing import Optional, List # noqa: F401

from xendit.balance_and_transaction.model import *  # noqa: F401,E501

class TransactionApi(object):
    """NOTE: This class is auto generated by the OpenAPI Generator.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_transaction_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (TransactionResponse,),
                'auth': [],
                'endpoint_path': '/transactions/{id}',
                'operation_id': 'get_transaction_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'for_user_id',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'id',
                ]
            },
            root_map={
                'validations': {
                    ('id',): {

                        'regex': {
                            'pattern': r'^txn_[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (TransactionId,),
                    'for_user_id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'for_user_id': 'for-user-id',
                },
                'location_map': {
                    'id': 'path',
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
        self.get_all_transactions_endpoint = _Endpoint(
            settings={
                'response_type': (TransactionsResponse,),
                'auth': [],
                'endpoint_path': '/transactions',
                'operation_id': 'get_all_transactions',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'for_user_id',
                    'types',
                    'statuses',
                    'channel_categories',
                    'reference_id',
                    'product_id',
                    'account_identifier',
                    'amount',
                    'currency',
                    'created',
                    'updated',
                    'limit',
                    'after_id',
                    'before_id',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'limit',
                    'after_id',
                    'before_id',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_maximum': 50,
                    },
                    ('after_id',): {

                        'regex': {
                            'pattern': r'^txn_[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$',  # noqa: E501
                        },
                    },
                    ('before_id',): {

                        'regex': {
                            'pattern': r'^txn_[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'for_user_id':
                        (str,),
                    'types':
                        ([TransactionTypes],),
                    'statuses':
                        ([TransactionStatuses],),
                    'channel_categories':
                        ([ChannelsCategories],),
                    'reference_id':
                        (str,),
                    'product_id':
                        (str,),
                    'account_identifier':
                        (str,),
                    'amount':
                        (float,),
                    'currency':
                        (Currency,),
                    'created':
                        (DateRangeFilter,),
                    'updated':
                        (DateRangeFilter,),
                    'limit':
                        (float,),
                    'after_id':
                        (TransactionId,),
                    'before_id':
                        (TransactionId,),
                },
                'attribute_map': {
                    'for_user_id': 'for-user-id',
                    'types': 'types',
                    'statuses': 'statuses',
                    'channel_categories': 'channel_categories',
                    'reference_id': 'reference_id',
                    'product_id': 'product_id',
                    'account_identifier': 'account_identifier',
                    'amount': 'amount',
                    'currency': 'currency',
                    'created': 'created',
                    'updated': 'updated',
                    'limit': 'limit',
                    'after_id': 'after_id',
                    'before_id': 'before_id',
                },
                'location_map': {
                    'for_user_id': 'header',
                    'types': 'query',
                    'statuses': 'query',
                    'channel_categories': 'query',
                    'reference_id': 'query',
                    'product_id': 'query',
                    'account_identifier': 'query',
                    'amount': 'query',
                    'currency': 'query',
                    'created': 'query',
                    'updated': 'query',
                    'limit': 'query',
                    'after_id': 'query',
                    'before_id': 'query',
                },
                'collection_format_map': {
                    'types': 'multi',
                    'statuses': 'multi',
                    'channel_categories': 'multi',
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

    def get_transaction_by_id(
        self,
        id: TransactionId,
        for_user_id: Optional[str] = None,
        **kwargs
    ) -> TransactionResponse:
        """Get a transaction based on its id  # noqa: E501

        Get single specific transaction by transaction id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_transaction_by_id(id, for_user_id, async_req=True)
        >>> result = thread.get()

        Args:
            id (TransactionId):

        Keyword Args:
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
            TransactionResponse
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
        kwargs['id'] = id
        if for_user_id is not None:
            kwargs['for_user_id'] = for_user_id
        return self.get_transaction_by_id_endpoint.call_with_http_info(**kwargs)

    def get_all_transactions(
        self,
        for_user_id: Optional[str] = None,
        types: Optional[List[TransactionTypes]] = None,
        statuses: Optional[List[TransactionStatuses]] = None,
        channel_categories: Optional[List[ChannelsCategories]] = None,
        reference_id: Optional[str] = None,
        product_id: Optional[str] = None,
        account_identifier: Optional[str] = None,
        amount: Optional[float] = None,
        currency: Optional[Currency] = None,
        created: Optional[DateRangeFilter] = None,
        updated: Optional[DateRangeFilter] = None,
        limit: Optional[float] = 10,
        after_id: Optional[TransactionId] = None,
        before_id: Optional[TransactionId] = None,
        **kwargs
    ) -> TransactionsResponse:
        """Get a list of transactions  # noqa: E501

        Get a list of all transactions based on filter and search parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_all_transactions(for_user_id, types, statuses, channel_categories, reference_id, product_id, account_identifier, amount, currency, created, updated, after_id, before_id, limit=10, async_req=True)
        >>> result = thread.get()


        Keyword Args:
            for_user_id (str): The sub-account user-id that you want to make this transaction for. This header is only used if you have access to xenPlatform. See xenPlatform for more information. [optional]
            types ([TransactionTypes]): Transaction types that will be included in the result. Default is to include all transaction types. [optional]
            statuses ([TransactionStatuses]): Status of the transaction. Default is to include all status.. [optional]
            channel_categories ([ChannelsCategories]): Payment channels in which the transaction is carried out. Default is to include all channels.. [optional]
            reference_id (str): To filter the result for transactions with matching reference given (case sensitive). [optional]
            product_id (str): To filter the result for transactions with matching product_id (a.k.a payment_id) given (case sensitive). [optional]
            account_identifier (str): Account identifier of transaction. The format will be different from each channel. For example, on `BANK` channel it will be account number and on `CARD` it will be masked card number.. [optional]
            amount (float): Specific transaction amount to search for. [optional]
            currency (Currency): [optional]
            created (DateRangeFilter): Filter time of transaction by created date. If not specified will list all dates.. [optional]
            updated (DateRangeFilter): Filter time of transaction by updated date. If not specified will list all dates.. [optional]
            limit (float): number of items in the result per page. Another name for \"results_per_page\". [optional] if omitted the server will use the default value of 10
            after_id (TransactionId): [optional]
            before_id (TransactionId): [optional]
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
            TransactionsResponse
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
        if for_user_id is not None:
            kwargs['for_user_id'] = for_user_id
        if types is not None:
            kwargs['types'] = types
        if statuses is not None:
            kwargs['statuses'] = statuses
        if channel_categories is not None:
            kwargs['channel_categories'] = channel_categories
        if reference_id is not None:
            kwargs['reference_id'] = reference_id
        if product_id is not None:
            kwargs['product_id'] = product_id
        if account_identifier is not None:
            kwargs['account_identifier'] = account_identifier
        if amount is not None:
            kwargs['amount'] = amount
        if currency is not None:
            kwargs['currency'] = currency
        if created is not None:
            kwargs['created'] = created
        if updated is not None:
            kwargs['updated'] = updated
        if limit is not None:
            kwargs['limit'] = limit
        if after_id is not None:
            kwargs['after_id'] = after_id
        if before_id is not None:
            kwargs['before_id'] = before_id
        return self.get_all_transactions_endpoint.call_with_http_info(**kwargs)

