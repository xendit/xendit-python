"""
    The version of the XENDIT API: 1.9.0
"""


import re  # noqa: F401
import sys  # noqa: F401
from typing import List  # noqa: F401

from xendit.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from xendit.exceptions import ApiAttributeError

from xendit.invoice.model.bank import Bank
from xendit.invoice.model.channel_properties import ChannelProperties
from xendit.invoice.model.customer_object import CustomerObject
from xendit.invoice.model.direct_debit import DirectDebit
from xendit.invoice.model.ewallet import Ewallet
from xendit.invoice.model.invoice_currency import InvoiceCurrency
from xendit.invoice.model.invoice_fee import InvoiceFee
from xendit.invoice.model.invoice_item import InvoiceItem
from xendit.invoice.model.invoice_payment_method import InvoicePaymentMethod
from xendit.invoice.model.invoice_status import InvoiceStatus
from xendit.invoice.model.notification_preference import NotificationPreference
from xendit.invoice.model.paylater import Paylater
from xendit.invoice.model.qr_code import QrCode
from xendit.invoice.model.retail_outlet import RetailOutlet
globals()['Bank'] = Bank
globals()['ChannelProperties'] = ChannelProperties
globals()['CustomerObject'] = CustomerObject
globals()['DirectDebit'] = DirectDebit
globals()['Ewallet'] = Ewallet
globals()['InvoiceCurrency'] = InvoiceCurrency
globals()['InvoiceFee'] = InvoiceFee
globals()['InvoiceItem'] = InvoiceItem
globals()['InvoicePaymentMethod'] = InvoicePaymentMethod
globals()['InvoiceStatus'] = InvoiceStatus
globals()['NotificationPreference'] = NotificationPreference
globals()['Paylater'] = Paylater
globals()['QrCode'] = QrCode
globals()['RetailOutlet'] = RetailOutlet

def lazy_import():
    pass

class Invoice(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'external_id': (str,),  # noqa: E501
            'user_id': (str,),  # noqa: E501
            'status': (InvoiceStatus,),  # noqa: E501
            'merchant_name': (str,),  # noqa: E501
            'merchant_profile_picture_url': (str,),  # noqa: E501
            'amount': (float,),  # noqa: E501
            'expiry_date': (datetime,),  # noqa: E501
            'invoice_url': (str,),  # noqa: E501
            'available_banks': ([Bank],),  # noqa: E501
            'available_retail_outlets': ([RetailOutlet],),  # noqa: E501
            'available_ewallets': ([Ewallet],),  # noqa: E501
            'available_qr_codes': ([QrCode],),  # noqa: E501
            'available_direct_debits': ([DirectDebit],),  # noqa: E501
            'available_paylaters': ([Paylater],),  # noqa: E501
            'should_send_email': (bool,),  # noqa: E501
            'created': (datetime,),  # noqa: E501
            'updated': (datetime,),  # noqa: E501
            'id': (str, none_type),  # noqa: E501
            'payer_email': (str, none_type),  # noqa: E501
            'description': (str, none_type),  # noqa: E501
            'payment_method': (InvoicePaymentMethod, none_type),  # noqa: E501
            'locale': (str, none_type),  # noqa: E501
            'should_exclude_credit_card': (bool, none_type),  # noqa: E501
            'success_redirect_url': (str, none_type),  # noqa: E501
            'failure_redirect_url': (str, none_type),  # noqa: E501
            'should_authenticate_credit_card': (bool, none_type),  # noqa: E501
            'currency': (InvoiceCurrency, none_type),  # noqa: E501
            'items': ([InvoiceItem], none_type),  # noqa: E501
            'fixed_va': (bool, none_type),  # noqa: E501
            'reminder_date': (datetime, none_type),  # noqa: E501
            'customer': (CustomerObject, none_type),  # noqa: E501
            'customer_notification_preference': (NotificationPreference, none_type),  # noqa: E501
            'fees': ([InvoiceFee], none_type),  # noqa: E501
            'channel_properties': (ChannelProperties, none_type),  # noqa: E501
            'metadata': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'external_id': 'external_id',  # noqa: E501
        'user_id': 'user_id',  # noqa: E501
        'status': 'status',  # noqa: E501
        'merchant_name': 'merchant_name',  # noqa: E501
        'merchant_profile_picture_url': 'merchant_profile_picture_url',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'expiry_date': 'expiry_date',  # noqa: E501
        'invoice_url': 'invoice_url',  # noqa: E501
        'available_banks': 'available_banks',  # noqa: E501
        'available_retail_outlets': 'available_retail_outlets',  # noqa: E501
        'available_ewallets': 'available_ewallets',  # noqa: E501
        'available_qr_codes': 'available_qr_codes',  # noqa: E501
        'available_direct_debits': 'available_direct_debits',  # noqa: E501
        'available_paylaters': 'available_paylaters',  # noqa: E501
        'should_send_email': 'should_send_email',  # noqa: E501
        'created': 'created',  # noqa: E501
        'updated': 'updated',  # noqa: E501
        'id': 'id',  # noqa: E501
        'payer_email': 'payer_email',  # noqa: E501
        'description': 'description',  # noqa: E501
        'payment_method': 'payment_method',  # noqa: E501
        'locale': 'locale',  # noqa: E501
        'should_exclude_credit_card': 'should_exclude_credit_card',  # noqa: E501
        'success_redirect_url': 'success_redirect_url',  # noqa: E501
        'failure_redirect_url': 'failure_redirect_url',  # noqa: E501
        'should_authenticate_credit_card': 'should_authenticate_credit_card',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'items': 'items',  # noqa: E501
        'fixed_va': 'fixed_va',  # noqa: E501
        'reminder_date': 'reminder_date',  # noqa: E501
        'customer': 'customer',  # noqa: E501
        'customer_notification_preference': 'customer_notification_preference',  # noqa: E501
        'fees': 'fees',  # noqa: E501
        'channel_properties': 'channel_properties',  # noqa: E501
        'metadata': 'metadata',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, external_id, user_id, status, merchant_name, merchant_profile_picture_url, amount, expiry_date, invoice_url, available_banks, available_retail_outlets, available_ewallets, available_qr_codes, available_direct_debits, available_paylaters, should_send_email, created, updated, *args, **kwargs):  # noqa: E501
        """Invoice - a model defined in OpenAPI

        Args:
            external_id (str): The external identifier for the invoice.
            user_id (str): The user ID associated with the invoice.
            status (InvoiceStatus):
            merchant_name (str): The name of the merchant.
            merchant_profile_picture_url (str): The URL of the merchant's profile picture.
            amount (float): The total amount of the invoice.
            expiry_date (datetime): Representing a date and time in ISO 8601 format.
            invoice_url (str): The URL to view the invoice.
            available_banks ([Bank]): An array of available banks for payment.
            available_retail_outlets ([RetailOutlet]): An array of available retail outlets for payment.
            available_ewallets ([Ewallet]): An array of available e-wallets for payment.
            available_qr_codes ([QrCode]): An array of available QR codes for payment.
            available_direct_debits ([DirectDebit]): An array of available direct debit options for payment.
            available_paylaters ([Paylater]): An array of available pay-later options for payment.
            should_send_email (bool): Indicates whether email notifications should be sent.
            created (datetime): Representing a date and time in ISO 8601 format.
            updated (datetime): Representing a date and time in ISO 8601 format.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): The unique identifier for the invoice.. [optional]  # noqa: E501
            payer_email (str): The email address of the payer.. [optional]  # noqa: E501
            description (str): A description of the invoice.. [optional]  # noqa: E501
            payment_method (InvoicePaymentMethod): [optional]  # noqa: E501
            locale (str): The locale or language used for the invoice.. [optional]  # noqa: E501
            should_exclude_credit_card (bool): Indicates whether credit card payments should be excluded.. [optional]  # noqa: E501
            success_redirect_url (str): The URL to redirect to on successful payment.. [optional]  # noqa: E501
            failure_redirect_url (str): The URL to redirect to on payment failure.. [optional]  # noqa: E501
            should_authenticate_credit_card (bool): Indicates whether credit card authentication is required.. [optional]  # noqa: E501
            currency (InvoiceCurrency): [optional]  # noqa: E501
            items ([InvoiceItem]): An array of items included in the invoice.. [optional]  # noqa: E501
            fixed_va (bool): Indicates whether the virtual account is fixed.. [optional]  # noqa: E501
            reminder_date (datetime): Representing a date and time in ISO 8601 format.. [optional]  # noqa: E501
            customer (CustomerObject): [optional]  # noqa: E501
            customer_notification_preference (NotificationPreference): [optional]  # noqa: E501
            fees ([InvoiceFee]): An array of fees associated with the invoice.. [optional]  # noqa: E501
            channel_properties (ChannelProperties): [optional]  # noqa: E501
            metadata ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): A free-format JSON for additional information that you may use. Object can be up to 50 keys, with key names up to 40 characters long and values up to 500 characters long.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                elif isinstance(arg, str):
                    kwargs.update({"value": arg})
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.external_id = external_id
        self.user_id = user_id
        self.status = status
        self.merchant_name = merchant_name
        self.merchant_profile_picture_url = merchant_profile_picture_url
        self.amount = amount
        self.expiry_date = expiry_date
        self.invoice_url = invoice_url
        self.available_banks = available_banks
        self.available_retail_outlets = available_retail_outlets
        self.available_ewallets = available_ewallets
        self.available_qr_codes = available_qr_codes
        self.available_direct_debits = available_direct_debits
        self.available_paylaters = available_paylaters
        self.should_send_email = should_send_email
        self.created = created
        self.updated = updated
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self,
        external_id: str,
        user_id: str,
        status: InvoiceStatus,
        merchant_name: str,
        merchant_profile_picture_url: str,
        amount: float,
        expiry_date: datetime,
        invoice_url: str,
        available_banks: list,
        available_retail_outlets: list,
        available_ewallets: list,
        available_qr_codes: list,
        available_direct_debits: list,
        available_paylaters: list,
        should_send_email: bool,
        created: datetime,
        updated: datetime,
        id: str | None = None,
        payer_email: str | None = None,
        description: str | None = None,
        payment_method: InvoicePaymentMethod | None = None,
        locale: str | None = None,
        should_exclude_credit_card: bool | None = None,
        success_redirect_url: str | None = None,
        failure_redirect_url: str | None = None,
        should_authenticate_credit_card: bool | None = None,
        currency: InvoiceCurrency | None = None,
        items: list | None = None,
        fixed_va: bool | None = None,
        reminder_date: datetime | None = None,
        customer: CustomerObject | None = None,
        customer_notification_preference: NotificationPreference | None = None,
        fees: list | None = None,
        channel_properties: ChannelProperties | None = None,
        metadata: dict | None = None,
        *args, **kwargs
    ):  # noqa: E501
        """Invoice - a model defined in OpenAPI

        Args:
            external_id (str): The external identifier for the invoice.
            user_id (str): The user ID associated with the invoice.
            status (InvoiceStatus):
            merchant_name (str): The name of the merchant.
            merchant_profile_picture_url (str): The URL of the merchant's profile picture.
            amount (float): The total amount of the invoice.
            expiry_date (datetime): Representing a date and time in ISO 8601 format.
            invoice_url (str): The URL to view the invoice.
            available_banks ([Bank]): An array of available banks for payment.
            available_retail_outlets ([RetailOutlet]): An array of available retail outlets for payment.
            available_ewallets ([Ewallet]): An array of available e-wallets for payment.
            available_qr_codes ([QrCode]): An array of available QR codes for payment.
            available_direct_debits ([DirectDebit]): An array of available direct debit options for payment.
            available_paylaters ([Paylater]): An array of available pay-later options for payment.
            should_send_email (bool): Indicates whether email notifications should be sent.
            created (datetime): Representing a date and time in ISO 8601 format.
            updated (datetime): Representing a date and time in ISO 8601 format.


        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): The unique identifier for the invoice.. [optional]  # noqa: E501
            payer_email (str): The email address of the payer.. [optional]  # noqa: E501
            description (str): A description of the invoice.. [optional]  # noqa: E501
            payment_method (InvoicePaymentMethod): [optional]  # noqa: E501
            locale (str): The locale or language used for the invoice.. [optional]  # noqa: E501
            should_exclude_credit_card (bool): Indicates whether credit card payments should be excluded.. [optional]  # noqa: E501
            success_redirect_url (str): The URL to redirect to on successful payment.. [optional]  # noqa: E501
            failure_redirect_url (str): The URL to redirect to on payment failure.. [optional]  # noqa: E501
            should_authenticate_credit_card (bool): Indicates whether credit card authentication is required.. [optional]  # noqa: E501
            currency (InvoiceCurrency): [optional]  # noqa: E501
            items ([InvoiceItem]): An array of items included in the invoice.. [optional]  # noqa: E501
            fixed_va (bool): Indicates whether the virtual account is fixed.. [optional]  # noqa: E501
            reminder_date (datetime): Representing a date and time in ISO 8601 format.. [optional]  # noqa: E501
            customer (CustomerObject): [optional]  # noqa: E501
            customer_notification_preference (NotificationPreference): [optional]  # noqa: E501
            fees ([InvoiceFee]): An array of fees associated with the invoice.. [optional]  # noqa: E501
            channel_properties (ChannelProperties): [optional]  # noqa: E501
            metadata ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): A free-format JSON for additional information that you may use. Object can be up to 50 keys, with key names up to 40 characters long and values up to 500 characters long.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                elif isinstance(arg, str):
                    kwargs.update({"value": arg})
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.external_id = external_id
        self.user_id = user_id
        self.status = status
        self.merchant_name = merchant_name
        self.merchant_profile_picture_url = merchant_profile_picture_url
        self.amount = amount
        self.expiry_date = expiry_date
        self.invoice_url = invoice_url
        self.available_banks = available_banks
        self.available_retail_outlets = available_retail_outlets
        self.available_ewallets = available_ewallets
        self.available_qr_codes = available_qr_codes
        self.available_direct_debits = available_direct_debits
        self.available_paylaters = available_paylaters
        self.should_send_email = should_send_email
        self.created = created
        self.updated = updated
        if id is not None:
            self.id = id
        if payer_email is not None:
            self.payer_email = payer_email
        if description is not None:
            self.description = description
        if payment_method is not None:
            self.payment_method = payment_method
        if locale is not None:
            self.locale = locale
        if should_exclude_credit_card is not None:
            self.should_exclude_credit_card = should_exclude_credit_card
        if success_redirect_url is not None:
            self.success_redirect_url = success_redirect_url
        if failure_redirect_url is not None:
            self.failure_redirect_url = failure_redirect_url
        if should_authenticate_credit_card is not None:
            self.should_authenticate_credit_card = should_authenticate_credit_card
        if currency is not None:
            self.currency = currency
        if items is not None:
            self.items = items
        if fixed_va is not None:
            self.fixed_va = fixed_va
        if reminder_date is not None:
            self.reminder_date = reminder_date
        if customer is not None:
            self.customer = customer
        if customer_notification_preference is not None:
            self.customer_notification_preference = customer_notification_preference
        if fees is not None:
            self.fees = fees
        if channel_properties is not None:
            self.channel_properties = channel_properties
        if metadata is not None:
            self.metadata = metadata
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
