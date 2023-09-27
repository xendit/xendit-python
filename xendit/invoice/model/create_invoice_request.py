"""
    The version of the XENDIT API: 1.5.0
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

from xendit.invoice.model.customer_object import CustomerObject
from xendit.invoice.model.invoice_fee import InvoiceFee
from xendit.invoice.model.invoice_item import InvoiceItem
from xendit.invoice.model.notification_preference import NotificationPreference
globals()['CustomerObject'] = CustomerObject
globals()['InvoiceFee'] = InvoiceFee
globals()['InvoiceItem'] = InvoiceItem
globals()['NotificationPreference'] = NotificationPreference


def lazy_import():
    pass

class CreateInvoiceRequest(ModelNormal):
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
            'amount': (float,),  # noqa: E501
            'payer_email': (str, none_type),  # noqa: E501
            'description': (str, none_type),  # noqa: E501
            'invoice_duration': (str, none_type),  # noqa: E501
            'callback_virtual_account_id': (str, none_type),  # noqa: E501
            'should_send_email': (bool, none_type),  # noqa: E501
            'customer': (CustomerObject, none_type),  # noqa: E501
            'customer_notification_preference': (NotificationPreference, none_type),  # noqa: E501
            'success_redirect_url': (str, none_type),  # noqa: E501
            'failure_redirect_url': (str, none_type),  # noqa: E501
            'payment_methods': ([str], none_type),  # noqa: E501
            'mid_label': (str, none_type),  # noqa: E501
            'should_authenticate_credit_card': (bool, none_type),  # noqa: E501
            'currency': (str, none_type),  # noqa: E501
            'reminder_time': (float, none_type),  # noqa: E501
            'local': (str, none_type),  # noqa: E501
            'reminder_time_unit': (str, none_type),  # noqa: E501
            'items': ([InvoiceItem], none_type),  # noqa: E501
            'fees': ([InvoiceFee], none_type),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'external_id': 'external_id',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'payer_email': 'payer_email',  # noqa: E501
        'description': 'description',  # noqa: E501
        'invoice_duration': 'invoice_duration',  # noqa: E501
        'callback_virtual_account_id': 'callback_virtual_account_id',  # noqa: E501
        'should_send_email': 'should_send_email',  # noqa: E501
        'customer': 'customer',  # noqa: E501
        'customer_notification_preference': 'customer_notification_preference',  # noqa: E501
        'success_redirect_url': 'success_redirect_url',  # noqa: E501
        'failure_redirect_url': 'failure_redirect_url',  # noqa: E501
        'payment_methods': 'payment_methods',  # noqa: E501
        'mid_label': 'mid_label',  # noqa: E501
        'should_authenticate_credit_card': 'should_authenticate_credit_card',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'reminder_time': 'reminder_time',  # noqa: E501
        'local': 'local',  # noqa: E501
        'reminder_time_unit': 'reminder_time_unit',  # noqa: E501
        'items': 'items',  # noqa: E501
        'fees': 'fees',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, external_id, amount, *args, **kwargs):  # noqa: E501
        """CreateInvoiceRequest - a model defined in OpenAPI

        Args:
            external_id (str): The external ID of the invoice.
            amount (float): The invoice amount.

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
            payer_email (str): The email address of the payer.. [optional]  # noqa: E501
            description (str): A description of the payment.. [optional]  # noqa: E501
            invoice_duration (str): The duration of the invoice.. [optional]  # noqa: E501
            callback_virtual_account_id (str): The ID of the callback virtual account.. [optional]  # noqa: E501
            should_send_email (bool): Indicates whether email notifications should be sent.. [optional]  # noqa: E501
            customer (CustomerObject): [optional]  # noqa: E501
            customer_notification_preference (NotificationPreference): [optional]  # noqa: E501
            success_redirect_url (str): The URL to redirect to on successful payment.. [optional]  # noqa: E501
            failure_redirect_url (str): The URL to redirect to on payment failure.. [optional]  # noqa: E501
            payment_methods ([str]): An array of available payment methods.. [optional]  # noqa: E501
            mid_label (str): The middle label.. [optional]  # noqa: E501
            should_authenticate_credit_card (bool): Indicates whether credit card authentication is required.. [optional]  # noqa: E501
            currency (str): The currency of the invoice.. [optional]  # noqa: E501
            reminder_time (float): The reminder time.. [optional]  # noqa: E501
            local (str): The local.. [optional]  # noqa: E501
            reminder_time_unit (str): The unit of the reminder time.. [optional]  # noqa: E501
            items ([InvoiceItem]): An array of items included in the invoice.. [optional]  # noqa: E501
            fees ([InvoiceFee]): An array of fees associated with the invoice.. [optional]  # noqa: E501
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
        self.amount = amount
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
        amount: float,
        payer_email: str | None = None,
        description: str | None = None,
        invoice_duration: str | None = None,
        callback_virtual_account_id: str | None = None,
        should_send_email: bool | None = None,
        customer: CustomerObject | None = None,
        customer_notification_preference: NotificationPreference | None = None,
        success_redirect_url: str | None = None,
        failure_redirect_url: str | None = None,
        payment_methods: list | None = None,
        mid_label: str | None = None,
        should_authenticate_credit_card: bool | None = None,
        currency: str | None = None,
        reminder_time: float | None = None,
        local: str | None = None,
        reminder_time_unit: str | None = None,
        items: list | None = None,
        fees: list | None = None,
        *args, **kwargs
    ):  # noqa: E501
        """CreateInvoiceRequest - a model defined in OpenAPI

        Args:
            external_id (str): The external ID of the invoice.
            amount (float): The invoice amount.


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
            payer_email (str): The email address of the payer.. [optional]  # noqa: E501
            description (str): A description of the payment.. [optional]  # noqa: E501
            invoice_duration (str): The duration of the invoice.. [optional]  # noqa: E501
            callback_virtual_account_id (str): The ID of the callback virtual account.. [optional]  # noqa: E501
            should_send_email (bool): Indicates whether email notifications should be sent.. [optional]  # noqa: E501
            customer (CustomerObject): [optional]  # noqa: E501
            customer_notification_preference (NotificationPreference): [optional]  # noqa: E501
            success_redirect_url (str): The URL to redirect to on successful payment.. [optional]  # noqa: E501
            failure_redirect_url (str): The URL to redirect to on payment failure.. [optional]  # noqa: E501
            payment_methods ([str]): An array of available payment methods.. [optional]  # noqa: E501
            mid_label (str): The middle label.. [optional]  # noqa: E501
            should_authenticate_credit_card (bool): Indicates whether credit card authentication is required.. [optional]  # noqa: E501
            currency (str): The currency of the invoice.. [optional]  # noqa: E501
            reminder_time (float): The reminder time.. [optional]  # noqa: E501
            local (str): The local.. [optional]  # noqa: E501
            reminder_time_unit (str): The unit of the reminder time.. [optional]  # noqa: E501
            items ([InvoiceItem]): An array of items included in the invoice.. [optional]  # noqa: E501
            fees ([InvoiceFee]): An array of fees associated with the invoice.. [optional]  # noqa: E501
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
        self.amount = amount
        if payer_email is not None:
            self.payer_email = payer_email
        if description is not None:
            self.description = description
        if invoice_duration is not None:
            self.invoice_duration = invoice_duration
        if callback_virtual_account_id is not None:
            self.callback_virtual_account_id = callback_virtual_account_id
        if should_send_email is not None:
            self.should_send_email = should_send_email
        if customer is not None:
            self.customer = customer
        if customer_notification_preference is not None:
            self.customer_notification_preference = customer_notification_preference
        if success_redirect_url is not None:
            self.success_redirect_url = success_redirect_url
        if failure_redirect_url is not None:
            self.failure_redirect_url = failure_redirect_url
        if payment_methods is not None:
            self.payment_methods = payment_methods
        if mid_label is not None:
            self.mid_label = mid_label
        if should_authenticate_credit_card is not None:
            self.should_authenticate_credit_card = should_authenticate_credit_card
        if currency is not None:
            self.currency = currency
        if reminder_time is not None:
            self.reminder_time = reminder_time
        if local is not None:
            self.local = local
        if reminder_time_unit is not None:
            self.reminder_time_unit = reminder_time_unit
        if items is not None:
            self.items = items
        if fees is not None:
            self.fees = fees
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
