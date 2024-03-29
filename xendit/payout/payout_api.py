"""
    Payout Service

    This API allows Xendit to send money from an account to a channel (banks, eWallets, retail outlets) from across regions  # noqa: E501

    The version of the OpenAPI document: 1.0.0
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

from xendit.payout.model import *  # noqa: F401,E501

class PayoutApi(object):
    """NOTE: This class is auto generated by the OpenAPI Generator.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_payout_endpoint = _Endpoint(
            settings={
                'response_type': (GetPayouts200ResponseDataInner,),
                'auth': [],
                'endpoint_path': '/v2/payouts',
                'operation_id': 'create_payout',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'idempotency_key',
                    'for_user_id',
                    'create_payout_request',
                ],
                'required': [
                    'idempotency_key',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'idempotency_key':
                        (str,),
                    'for_user_id':
                        (str,),
                    'create_payout_request':
                        (CreatePayoutRequest,),
                },
                'attribute_map': {
                    'idempotency_key': 'idempotency-key',
                    'for_user_id': 'for-user-id',
                },
                'location_map': {
                    'idempotency_key': 'header',
                    'for_user_id': 'header',
                    'create_payout_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.get_payout_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (GetPayouts200ResponseDataInner,),
                'auth': [],
                'endpoint_path': '/v2/payouts/{id}',
                'operation_id': 'get_payout_by_id',
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
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
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
        self.get_payout_channels_endpoint = _Endpoint(
            settings={
                'response_type': ([Channel],),
                'auth': [],
                'endpoint_path': '/payouts_channels',
                'operation_id': 'get_payout_channels',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'currency',
                    'channel_category',
                    'channel_code',
                    'for_user_id',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'currency':
                        (str,),
                    'channel_category':
                        ([ChannelCategory],),
                    'channel_code':
                        (str,),
                    'for_user_id':
                        (str,),
                },
                'attribute_map': {
                    'currency': 'currency',
                    'channel_category': 'channel_category',
                    'channel_code': 'channel_code',
                    'for_user_id': 'for-user-id',
                },
                'location_map': {
                    'currency': 'query',
                    'channel_category': 'query',
                    'channel_code': 'query',
                    'for_user_id': 'header',
                },
                'collection_format_map': {
                    'channel_category': 'csv',
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
        self.get_payouts_endpoint = _Endpoint(
            settings={
                'response_type': (GetPayouts200Response,),
                'auth': [],
                'endpoint_path': '/v2/payouts',
                'operation_id': 'get_payouts',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'reference_id',
                    'limit',
                    'after_id',
                    'before_id',
                    'for_user_id',
                ],
                'required': [
                    'reference_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'reference_id':
                        (str,),
                    'limit':
                        (float,),
                    'after_id':
                        (str,),
                    'before_id':
                        (str,),
                    'for_user_id':
                        (str,),
                },
                'attribute_map': {
                    'reference_id': 'reference_id',
                    'limit': 'limit',
                    'after_id': 'after_id',
                    'before_id': 'before_id',
                    'for_user_id': 'for-user-id',
                },
                'location_map': {
                    'reference_id': 'query',
                    'limit': 'query',
                    'after_id': 'query',
                    'before_id': 'query',
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
        self.cancel_payout_endpoint = _Endpoint(
            settings={
                'response_type': (GetPayouts200ResponseDataInner,),
                'auth': [],
                'endpoint_path': '/v2/payouts/{id}/cancel',
                'operation_id': 'cancel_payout',
                'http_method': 'POST',
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
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
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

    def create_payout(
        self,
        idempotency_key: str,
        for_user_id: Optional[str] = None,
        create_payout_request: Optional[CreatePayoutRequest] = None,
        **kwargs
    ) -> GetPayouts200ResponseDataInner:
        """API to send money at scale to bank accounts & eWallets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_payout(idempotency_key, for_user_id, create_payout_request, async_req=True)
        >>> result = thread.get()

        Args:
            idempotency_key (str): A unique key to prevent duplicate requests from pushing through our system. No expiration.

        Keyword Args:
            for_user_id (str): The sub-account user-id that you want to make this transaction for. This header is only used if you have access to xenPlatform. See xenPlatform for more information.. [optional]
            create_payout_request (CreatePayoutRequest): [optional]
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
            GetPayouts200ResponseDataInner
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
        kwargs['idempotency_key'] = idempotency_key
        if for_user_id is not None:
            kwargs['for_user_id'] = for_user_id
        if create_payout_request is not None:
            kwargs['create_payout_request'] = create_payout_request
        return self.create_payout_endpoint.call_with_http_info(**kwargs)

    def get_payout_by_id(
        self,
        id: str,
        for_user_id: Optional[str] = None,
        **kwargs
    ) -> GetPayouts200ResponseDataInner:
        """API to fetch the current status, or details of the payout  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_payout_by_id(id, for_user_id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): Payout id returned from the response of /v2/payouts

        Keyword Args:
            for_user_id (str): The sub-account user-id that you want to make this transaction for. This header is only used if you have access to xenPlatform. See xenPlatform for more information.. [optional]
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
            GetPayouts200ResponseDataInner
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
        return self.get_payout_by_id_endpoint.call_with_http_info(**kwargs)

    def get_payout_channels(
        self,
        currency: Optional[str] = None,
        channel_category: Optional[List[ChannelCategory]] = None,
        channel_code: Optional[str] = None,
        for_user_id: Optional[str] = None,
        **kwargs
    ) -> [Channel]:
        """API providing the current list of banks and e-wallets we support for payouts for both regions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_payout_channels(currency, channel_category, channel_code, for_user_id, async_req=True)
        >>> result = thread.get()


        Keyword Args:
            currency (str): Filter channels by currency from ISO-4217 values. [optional]
            channel_category ([ChannelCategory]): Filter channels by category. [optional]
            channel_code (str): Filter channels by channel code, prefixed by ISO-3166 country code. [optional]
            for_user_id (str): The sub-account user-id that you want to make this transaction for. This header is only used if you have access to xenPlatform. See xenPlatform for more information.. [optional]
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
            [Channel]
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
        if currency is not None:
            kwargs['currency'] = currency
        if channel_category is not None:
            kwargs['channel_category'] = channel_category
        if channel_code is not None:
            kwargs['channel_code'] = channel_code
        if for_user_id is not None:
            kwargs['for_user_id'] = for_user_id
        return self.get_payout_channels_endpoint.call_with_http_info(**kwargs)

    def get_payouts(
        self,
        reference_id: str,
        limit: Optional[float] = None,
        after_id: Optional[str] = None,
        before_id: Optional[str] = None,
        for_user_id: Optional[str] = None,
        **kwargs
    ) -> GetPayouts200Response:
        """API to retrieve all matching payouts with reference ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_payouts(reference_id, limit, after_id, before_id, for_user_id, async_req=True)
        >>> result = thread.get()

        Args:
            reference_id (str): Reference_id provided when creating the payout

        Keyword Args:
            limit (float): Number of records to fetch per API call. [optional]
            after_id (str): Used to fetch record after this payout unique id. [optional]
            before_id (str): Used to fetch record before this payout unique id. [optional]
            for_user_id (str): The sub-account user-id that you want to make this transaction for. This header is only used if you have access to xenPlatform. See xenPlatform for more information.. [optional]
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
            GetPayouts200Response
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
        kwargs['reference_id'] = reference_id
        if limit is not None:
            kwargs['limit'] = limit
        if after_id is not None:
            kwargs['after_id'] = after_id
        if before_id is not None:
            kwargs['before_id'] = before_id
        if for_user_id is not None:
            kwargs['for_user_id'] = for_user_id
        return self.get_payouts_endpoint.call_with_http_info(**kwargs)

    def cancel_payout(
        self,
        id: str,
        for_user_id: Optional[str] = None,
        **kwargs
    ) -> GetPayouts200ResponseDataInner:
        """API to cancel requested payouts that have not yet been sent to partner banks and e-wallets. Cancellation is possible if the payout has not been sent out via our partner and when payout status is ACCEPTED.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.cancel_payout(id, for_user_id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): Payout id returned from the response of /v2/payouts

        Keyword Args:
            for_user_id (str): The sub-account user-id that you want to make this transaction for. This header is only used if you have access to xenPlatform. See xenPlatform for more information.. [optional]
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
            GetPayouts200ResponseDataInner
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
        return self.cancel_payout_endpoint.call_with_http_info(**kwargs)

