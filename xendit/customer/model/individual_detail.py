"""
    The version of the XENDIT API: 1.0.0
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

from xendit.customer.model.country_code import CountryCode
from xendit.customer.model.employment_detail import EmploymentDetail
globals()['CountryCode'] = CountryCode
globals()['EmploymentDetail'] = EmploymentDetail

def lazy_import():
    pass

class IndividualDetail(ModelNormal):
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
        ('gender',): {
            'None': None,
            'MALE': "MALE",
            'FEMALE': "FEMALE",
            'OTHER': "OTHER",
        },
    }

    validations = {
        ('given_names',): {
            'max_length': 255,
        },
        ('given_names_non_roman',): {
            'max_length': 255,
        },
        ('middle_name',): {
            'max_length': 255,
        },
        ('surname',): {
            'max_length': 255,
        },
        ('surname_non_roman',): {
            'max_length': 255,
        },
        ('mother_maiden_name',): {
            'max_length': 255,
        },
        ('date_of_birth',): {
            'max_length': 30,
        },
        ('place_of_birth',): {
            'max_length': 255,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = True

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
            'given_names': (str, none_type),  # noqa: E501
            'given_names_non_roman': (str, none_type, none_type),  # noqa: E501
            'middle_name': (str, none_type, none_type),  # noqa: E501
            'surname': (str, none_type, none_type),  # noqa: E501
            'surname_non_roman': (str, none_type, none_type),  # noqa: E501
            'mother_maiden_name': (str, none_type, none_type),  # noqa: E501
            'gender': (str, none_type, none_type),  # noqa: E501
            'date_of_birth': (str, none_type, none_type),  # noqa: E501
            'nationality': (CountryCode, none_type),  # noqa: E501
            'place_of_birth': (str, none_type, none_type),  # noqa: E501
            'employment': (EmploymentDetail, none_type),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'given_names': 'given_names',  # noqa: E501
        'given_names_non_roman': 'given_names_non_roman',  # noqa: E501
        'middle_name': 'middle_name',  # noqa: E501
        'surname': 'surname',  # noqa: E501
        'surname_non_roman': 'surname_non_roman',  # noqa: E501
        'mother_maiden_name': 'mother_maiden_name',  # noqa: E501
        'gender': 'gender',  # noqa: E501
        'date_of_birth': 'date_of_birth',  # noqa: E501
        'nationality': 'nationality',  # noqa: E501
        'place_of_birth': 'place_of_birth',  # noqa: E501
        'employment': 'employment',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """IndividualDetail - a model defined in OpenAPI

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
            given_names (str): [optional]  # noqa: E501
            given_names_non_roman (str, none_type): [optional]  # noqa: E501
            middle_name (str, none_type): [optional]  # noqa: E501
            surname (str, none_type): [optional]  # noqa: E501
            surname_non_roman (str, none_type): [optional]  # noqa: E501
            mother_maiden_name (str, none_type): [optional]  # noqa: E501
            gender (str, none_type): [optional]  # noqa: E501
            date_of_birth (str, none_type): [optional]  # noqa: E501
            nationality (CountryCode): [optional]  # noqa: E501
            place_of_birth (str, none_type): [optional]  # noqa: E501
            employment (EmploymentDetail): [optional]  # noqa: E501
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
        given_names: str | None = None,
        given_names_non_roman: str | None = None,
        middle_name: str | None = None,
        surname: str | None = None,
        surname_non_roman: str | None = None,
        mother_maiden_name: str | None = None,
        gender: str | None = None,
        date_of_birth: str | None = None,
        nationality: str | None = None,
        place_of_birth: str | None = None,
        employment: EmploymentDetail | None = None,
        *args, **kwargs
    ):  # noqa: E501
        """IndividualDetail - a model defined in OpenAPI


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
            given_names (str): [optional]  # noqa: E501
            given_names_non_roman (str, none_type): [optional]  # noqa: E501
            middle_name (str, none_type): [optional]  # noqa: E501
            surname (str, none_type): [optional]  # noqa: E501
            surname_non_roman (str, none_type): [optional]  # noqa: E501
            mother_maiden_name (str, none_type): [optional]  # noqa: E501
            gender (str, none_type): [optional]  # noqa: E501
            date_of_birth (str, none_type): [optional]  # noqa: E501
            nationality (CountryCode): [optional]  # noqa: E501
            place_of_birth (str, none_type): [optional]  # noqa: E501
            employment (EmploymentDetail): [optional]  # noqa: E501
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

        if given_names is not None:
            self.given_names = given_names
        if given_names_non_roman is not None:
            self.given_names_non_roman = given_names_non_roman
        if middle_name is not None:
            self.middle_name = middle_name
        if surname is not None:
            self.surname = surname
        if surname_non_roman is not None:
            self.surname_non_roman = surname_non_roman
        if mother_maiden_name is not None:
            self.mother_maiden_name = mother_maiden_name
        if gender is not None:
            self.gender = gender
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if nationality is not None:
            self.nationality = nationality
        if place_of_birth is not None:
            self.place_of_birth = place_of_birth
        if employment is not None:
            self.employment = employment
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