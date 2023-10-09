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

from xendit.customer.model.address import Address
from xendit.customer.model.business_detail import BusinessDetail
from xendit.customer.model.end_customer_status import EndCustomerStatus
from xendit.customer.model.identity_account_response import IdentityAccountResponse
from xendit.customer.model.individual_detail import IndividualDetail
from xendit.customer.model.kyc_document_response import KYCDocumentResponse
globals()['Address'] = Address
globals()['BusinessDetail'] = BusinessDetail
globals()['EndCustomerStatus'] = EndCustomerStatus
globals()['IdentityAccountResponse'] = IdentityAccountResponse
globals()['IndividualDetail'] = IndividualDetail
globals()['KYCDocumentResponse'] = KYCDocumentResponse

def lazy_import():
    pass

class Customer(ModelNormal):
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
        ('type',): {
            'INDIVIDUAL': "INDIVIDUAL",
            'BUSINESS': "BUSINESS",
        },
    }

    validations = {
        ('reference_id',): {
            'max_length': 255,
        },
        ('description',): {
            'max_length': 1000,
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
            'type': (str,),  # noqa: E501
            'reference_id': (str,),  # noqa: E501
            'individual_detail': (IndividualDetail,),  # noqa: E501
            'business_detail': (BusinessDetail,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'email': (str, none_type,),  # noqa: E501
            'mobile_number': (str, none_type,),  # noqa: E501
            'phone_number': (str, none_type,),  # noqa: E501
            'addresses': ([Address], none_type,),  # noqa: E501
            'identity_accounts': ([IdentityAccountResponse], none_type,),  # noqa: E501
            'kyc_documents': ([KYCDocumentResponse], none_type,),  # noqa: E501
            'metadata': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'created': (datetime,),  # noqa: E501
            'updated': (datetime,),  # noqa: E501
            'status': (EndCustomerStatus, none_type),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'type': 'type',  # noqa: E501
        'reference_id': 'reference_id',  # noqa: E501
        'individual_detail': 'individual_detail',  # noqa: E501
        'business_detail': 'business_detail',  # noqa: E501
        'description': 'description',  # noqa: E501
        'email': 'email',  # noqa: E501
        'mobile_number': 'mobile_number',  # noqa: E501
        'phone_number': 'phone_number',  # noqa: E501
        'addresses': 'addresses',  # noqa: E501
        'identity_accounts': 'identity_accounts',  # noqa: E501
        'kyc_documents': 'kyc_documents',  # noqa: E501
        'metadata': 'metadata',  # noqa: E501
        'id': 'id',  # noqa: E501
        'created': 'created',  # noqa: E501
        'updated': 'updated',  # noqa: E501
        'status': 'status',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, reference_id, individual_detail, business_detail, description, email, mobile_number, phone_number, addresses, identity_accounts, kyc_documents, metadata, id, created, updated, *args, **kwargs):  # noqa: E501
        """Customer - a model defined in OpenAPI

        Args:
            reference_id (str): Merchant's reference of this end customer, eg Merchant's user's id. Must be unique.
            individual_detail (IndividualDetail):
            business_detail (BusinessDetail):
            description (str, none_type):
            email (str, none_type):
            mobile_number (str, none_type):
            phone_number (str, none_type):
            addresses ([Address], none_type):
            identity_accounts ([IdentityAccountResponse], none_type):
            kyc_documents ([KYCDocumentResponse], none_type):
            metadata ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type):
            id (str):
            created (datetime):
            updated (datetime):

        Keyword Args:
            type (str): defaults to "INDIVIDUAL", must be one of ["INDIVIDUAL", "BUSINESS", ]  # noqa: E501
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
            status (EndCustomerStatus): [optional]  # noqa: E501
        """

        type = kwargs.get('type', "INDIVIDUAL")
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

        self.type = type
        self.reference_id = reference_id
        self.individual_detail = individual_detail
        self.business_detail = business_detail
        self.description = description
        self.email = email
        self.mobile_number = mobile_number
        self.phone_number = phone_number
        self.addresses = addresses
        self.identity_accounts = identity_accounts
        self.kyc_documents = kyc_documents
        self.metadata = metadata
        self.id = id
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
        reference_id: str,
        individual_detail: IndividualDetail | None,
        business_detail: BusinessDetail | None,
        description: str | None,
        email: str | None,
        mobile_number: str | None,
        phone_number: str | None,
        addresses: list | None,
        identity_accounts: list | None,
        kyc_documents: list | None,
        metadata: dict | None,
        id: str,
        created: datetime,
        updated: datetime,
        status: EndCustomerStatus | None = None,
        type: str = "INDIVIDUAL",
        *args, **kwargs
    ):  # noqa: E501
        """Customer - a model defined in OpenAPI

        Args:
            reference_id (str): Merchant's reference of this end customer, eg Merchant's user's id. Must be unique.
            individual_detail (IndividualDetail):
            business_detail (BusinessDetail):
            description (str, none_type):
            email (str, none_type):
            mobile_number (str, none_type):
            phone_number (str, none_type):
            addresses ([Address], none_type):
            identity_accounts ([IdentityAccountResponse], none_type):
            kyc_documents ([KYCDocumentResponse], none_type):
            metadata ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type):
            id (str):
            created (datetime):
            updated (datetime):


        Keyword Args:
            type (str): defaults to "INDIVIDUAL", must be one of ["INDIVIDUAL", "BUSINESS", ]  # noqa: E501
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
            status (EndCustomerStatus): [optional]  # noqa: E501
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

        self.type = type
        self.reference_id = reference_id
        self.individual_detail = individual_detail
        self.business_detail = business_detail
        self.description = description
        self.email = email
        self.mobile_number = mobile_number
        self.phone_number = phone_number
        self.addresses = addresses
        self.identity_accounts = identity_accounts
        self.kyc_documents = kyc_documents
        self.metadata = metadata
        self.id = id
        self.created = created
        self.updated = updated
        if status is not None:
            self.status = status
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
