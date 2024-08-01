"""
    The version of the XENDIT API: 2.128.0
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


def lazy_import():
    pass

class EWalletChannelProperties(ModelNormal):
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
        ('success_return_url',): {
            'regex': {
                'pattern': r'^\S{1,255}:\/\/\S{0,1000}$',  # noqa: E501
            },
        },
        ('failure_return_url',): {
            'regex': {
                'pattern': r'^\S{1,255}:\/\/\S{0,1000}$',  # noqa: E501
            },
        },
        ('pending_return_url',): {
            'regex': {
                'pattern': r'^\S{1,255}:\/\/\S{0,1000}$',  # noqa: E501
            },
        },
        ('cancel_return_url',): {
            'regex': {
                'pattern': r'^\S{1,255}:\/\/\S{0,1000}$',  # noqa: E501
            },
        },
        ('cashtag',): {
            'regex': {
                'pattern': r'^[$][a-zA-Z0-9_]{3,15}$',  # noqa: E501
            },
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
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
        return {
            'success_return_url': (str, none_type),  # noqa: E501
            'failure_return_url': (str, none_type),  # noqa: E501
            'pending_return_url': (str, none_type),  # noqa: E501
            'cancel_return_url': (str, none_type),  # noqa: E501
            'mobile_number': (str, none_type),  # noqa: E501
            'redeem_points': (str, none_type),  # noqa: E501
            'cashtag': (str, none_type),  # noqa: E501
            'promotion_label': (str, none_type),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'success_return_url': 'success_return_url',  # noqa: E501
        'failure_return_url': 'failure_return_url',  # noqa: E501
        'pending_return_url': 'pending_return_url',  # noqa: E501
        'cancel_return_url': 'cancel_return_url',  # noqa: E501
        'mobile_number': 'mobile_number',  # noqa: E501
        'redeem_points': 'redeem_points',  # noqa: E501
        'cashtag': 'cashtag',  # noqa: E501
        'promotion_label': 'promotion_label',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """EWalletChannelProperties - a model defined in OpenAPI

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
            success_return_url (str): URL where the end-customer is redirected if the authorization is successful. [optional]  # noqa: E501
            failure_return_url (str): URL where the end-customer is redirected if the authorization failed. [optional]  # noqa: E501
            pending_return_url (str): URL where the end-customer is redirected if the authorization is pending. [optional]  # noqa: E501
            cancel_return_url (str): URL where the end-customer is redirected if the authorization cancelled. [optional]  # noqa: E501
            mobile_number (str): Mobile number of customer in E.164 format (e.g. +628123123123). For OVO one time payment use only.. [optional]  # noqa: E501
            redeem_points (str): REDEEM_NONE will not use any point, REDEEM_ALL will use all available points before cash balance is used. For OVO and ShopeePay tokenized payment use only.. [optional]  # noqa: E501
            cashtag (str): Available for JENIUSPAY only. [optional]  # noqa: E501
            promotion_label (str): Available only for OVO. [optional]  # noqa: E501
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
        success_return_url: str | None = None,
        failure_return_url: str | None = None,
        pending_return_url: str | None = None,
        cancel_return_url: str | None = None,
        mobile_number: str | None = None,
        redeem_points: str | None = None,
        cashtag: str | None = None,
        promotion_label: str | None = None,
        *args, **kwargs
    ):  # noqa: E501
        """EWalletChannelProperties - a model defined in OpenAPI


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
            success_return_url (str): URL where the end-customer is redirected if the authorization is successful. [optional]  # noqa: E501
            failure_return_url (str): URL where the end-customer is redirected if the authorization failed. [optional]  # noqa: E501
            pending_return_url (str): URL where the end-customer is redirected if the authorization is pending. [optional]  # noqa: E501
            cancel_return_url (str): URL where the end-customer is redirected if the authorization cancelled. [optional]  # noqa: E501
            mobile_number (str): Mobile number of customer in E.164 format (e.g. +628123123123). For OVO one time payment use only.. [optional]  # noqa: E501
            redeem_points (str): REDEEM_NONE will not use any point, REDEEM_ALL will use all available points before cash balance is used. For OVO and ShopeePay tokenized payment use only.. [optional]  # noqa: E501
            cashtag (str): Available for JENIUSPAY only. [optional]  # noqa: E501
            promotion_label (str): Available only for OVO. [optional]  # noqa: E501
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

        if success_return_url is not None:
            self.success_return_url = success_return_url
        if failure_return_url is not None:
            self.failure_return_url = failure_return_url
        if pending_return_url is not None:
            self.pending_return_url = pending_return_url
        if cancel_return_url is not None:
            self.cancel_return_url = cancel_return_url
        if mobile_number is not None:
            self.mobile_number = mobile_number
        if redeem_points is not None:
            self.redeem_points = redeem_points
        if cashtag is not None:
            self.cashtag = cashtag
        if promotion_label is not None:
            self.promotion_label = promotion_label
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
