"""
    The version of the XENDIT API: 1.59.0
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

class DirectDebitChannelCode(ModelSimple):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('value',): {
            'BCA_KLIKPAY': "BCA_KLIKPAY",
            'BCA_ONEKLIK': "BCA_ONEKLIK",
            'BRI': "BRI",
            'BNI': "BNI",
            'MANDIRI': "MANDIRI",
            'BPI': "BPI",
            'BPI_RECURRING': "BPI_RECURRING",
            'BDO': "BDO",
            'CIMBNIAGA': "CIMBNIAGA",
            'MTB': "MTB",
            'RCBC': "RCBC",
            'UBP': "UBP",
            'UBP_EADA': "UBP_EADA",
            'UBP_DEBIT_PULL': "UBP_DEBIT_PULL",
            'CHINABANK': "CHINABANK",
            'BAY': "BAY",
            'KTB': "KTB",
            'BBL': "BBL",
            'SCB': "SCB",
            'KBANK_MB': "KBANK_MB",
            'BAY_MB': "BAY_MB",
            'KTB_MB': "KTB_MB",
            'BBL_MB': "BBL_MB",
            'SCB_MB': "SCB_MB",
            'BDO_EPAY': "BDO_EPAY",
            'AFFIN_FPX': "AFFIN_FPX",
            'AGRO_FPX': "AGRO_FPX",
            'ALLIANCE_FPX': "ALLIANCE_FPX",
            'AMBANK_FPX': "AMBANK_FPX",
            'ISLAM_FPX': "ISLAM_FPX",
            'MUAMALAT_FPX': "MUAMALAT_FPX",
            'BOC_FPX': "BOC_FPX",
            'RAKYAT_FPX': "RAKYAT_FPX",
            'BSN_FPX': "BSN_FPX",
            'CIMB_FPX': "CIMB_FPX",
            'HLB_FPX': "HLB_FPX",
            'HSBC_FPX': "HSBC_FPX",
            'KFH_FPX': "KFH_FPX",
            'MAYB2E_FPX': "MAYB2E_FPX",
            'MAYB2U_FPX': "MAYB2U_FPX",
            'OCBC_FPX': "OCBC_FPX",
            'PUBLIC_FPX': "PUBLIC_FPX",
            'RHB_FPX': "RHB_FPX",
            'SCH_FPX': "SCH_FPX",
            'UOB_FPX': "UOB_FPX",
            'AFFIN_FPX_BUSINESS': "AFFIN_FPX_BUSINESS",
            'AGRO_FPX_BUSINESS': "AGRO_FPX_BUSINESS",
            'ALLIANCE_FPX_BUSINESS': "ALLIANCE_FPX_BUSINESS",
            'AMBANK_FPX_BUSINESS': "AMBANK_FPX_BUSINESS",
            'ISLAM_FPX_BUSINESS': "ISLAM_FPX_BUSINESS",
            'MUAMALAT_FPX_BUSINESS': "MUAMALAT_FPX_BUSINESS",
            'BNP_FPX_BUSINESS': "BNP_FPX_BUSINESS",
            'CIMB_FPX_BUSINESS': "CIMB_FPX_BUSINESS",
            'CITIBANK_FPX_BUSINESS': "CITIBANK_FPX_BUSINESS",
            'DEUTSCHE_FPX_BUSINESS': "DEUTSCHE_FPX_BUSINESS",
            'HLB_FPX_BUSINESS': "HLB_FPX_BUSINESS",
            'HSBC_FPX_BUSINESS': "HSBC_FPX_BUSINESS",
            'RAKYAT_FPX_BUSINESS': "RAKYAT_FPX_BUSINESS",
            'KFH_FPX_BUSINESS': "KFH_FPX_BUSINESS",
            'MAYB2E_FPX_BUSINESS': "MAYB2E_FPX_BUSINESS",
            'OCBC_FPX_BUSINESS': "OCBC_FPX_BUSINESS",
            'PUBLIC_FPX_BUSINESS': "PUBLIC_FPX_BUSINESS",
            'RHB_FPX_BUSINESS': "RHB_FPX_BUSINESS",
            'SCH_FPX_BUSINESS': "SCH_FPX_BUSINESS",
            'UOB_FPX_BUSINESS': "UOB_FPX_BUSINESS",
            'BDO_ONLINE_BANKING': "BDO_ONLINE_BANKING",
            'BPI_ONLINE_BANKING': "BPI_ONLINE_BANKING",
            'UNIONBANK_ONLINE_BANKING': "UNIONBANK_ONLINE_BANKING",
            'BOC_ONLINE_BANKING': "BOC_ONLINE_BANKING",
            'CHINABANK_ONLINE_BANKING': "CHINABANK_ONLINE_BANKING",
            'INSTAPAY_ONLINE_BANKING': "INSTAPAY_ONLINE_BANKING",
            'LANDBANK_ONLINE_BANKING': "LANDBANK_ONLINE_BANKING",
            'MAYBANK_ONLINE_BANKING': "MAYBANK_ONLINE_BANKING",
            'METROBANK_ONLINE_BANKING': "METROBANK_ONLINE_BANKING",
            'PNB_ONLINE_BANKING': "PNB_ONLINE_BANKING",
            'PSBANK_ONLINE_BANKING': "PSBANK_ONLINE_BANKING",
            'PESONET_ONLINE_BANKING': "PESONET_ONLINE_BANKING",
            'RCBC_ONLINE_BANKING': "RCBC_ONLINE_BANKING",
            'ROBINSONS_BANK_ONLINE_BANKING': "ROBINSONS_BANK_ONLINE_BANKING",
            'SECURITY_BANK_ONLINE_BANKING': "SECURITY_BANK_ONLINE_BANKING",
            'XENDIT_ENUM_DEFAULT_FALLBACK': 'UNKNOWN_ENUM_VALUE',
        },
    }

    validations = {
    }

    additional_properties_type = None

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
            'value': (str,),
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {}

    read_only_vars = set()

    _composed_schemas = None

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):
        """DirectDebitChannelCode - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): Direct Debit Channel Code., must be one of ["BCA_KLIKPAY", "BCA_ONEKLIK", "BRI", "BNI", "MANDIRI", "BPI", "BPI_RECURRING", "BDO", "CIMBNIAGA", "MTB", "RCBC", "UBP", "UBP_EADA", "UBP_DEBIT_PULL", "CHINABANK", "BAY", "KTB", "BBL", "SCB", "KBANK_MB", "BAY_MB", "KTB_MB", "BBL_MB", "SCB_MB", "BDO_EPAY", "AFFIN_FPX", "AGRO_FPX", "ALLIANCE_FPX", "AMBANK_FPX", "ISLAM_FPX", "MUAMALAT_FPX", "BOC_FPX", "RAKYAT_FPX", "BSN_FPX", "CIMB_FPX", "HLB_FPX", "HSBC_FPX", "KFH_FPX", "MAYB2E_FPX", "MAYB2U_FPX", "OCBC_FPX", "PUBLIC_FPX", "RHB_FPX", "SCH_FPX", "UOB_FPX", "AFFIN_FPX_BUSINESS", "AGRO_FPX_BUSINESS", "ALLIANCE_FPX_BUSINESS", "AMBANK_FPX_BUSINESS", "ISLAM_FPX_BUSINESS", "MUAMALAT_FPX_BUSINESS", "BNP_FPX_BUSINESS", "CIMB_FPX_BUSINESS", "CITIBANK_FPX_BUSINESS", "DEUTSCHE_FPX_BUSINESS", "HLB_FPX_BUSINESS", "HSBC_FPX_BUSINESS", "RAKYAT_FPX_BUSINESS", "KFH_FPX_BUSINESS", "MAYB2E_FPX_BUSINESS", "OCBC_FPX_BUSINESS", "PUBLIC_FPX_BUSINESS", "RHB_FPX_BUSINESS", "SCH_FPX_BUSINESS", "UOB_FPX_BUSINESS", "BDO_ONLINE_BANKING", "BPI_ONLINE_BANKING", "UNIONBANK_ONLINE_BANKING", "BOC_ONLINE_BANKING", "CHINABANK_ONLINE_BANKING", "INSTAPAY_ONLINE_BANKING", "LANDBANK_ONLINE_BANKING", "MAYBANK_ONLINE_BANKING", "METROBANK_ONLINE_BANKING", "PNB_ONLINE_BANKING", "PSBANK_ONLINE_BANKING", "PESONET_ONLINE_BANKING", "RCBC_ONLINE_BANKING", "ROBINSONS_BANK_ONLINE_BANKING", "SECURITY_BANK_ONLINE_BANKING", ]  # noqa: E501

        Keyword Args:
            value (str): Direct Debit Channel Code., must be one of ["BCA_KLIKPAY", "BCA_ONEKLIK", "BRI", "BNI", "MANDIRI", "BPI", "BPI_RECURRING", "BDO", "CIMBNIAGA", "MTB", "RCBC", "UBP", "UBP_EADA", "UBP_DEBIT_PULL", "CHINABANK", "BAY", "KTB", "BBL", "SCB", "KBANK_MB", "BAY_MB", "KTB_MB", "BBL_MB", "SCB_MB", "BDO_EPAY", "AFFIN_FPX", "AGRO_FPX", "ALLIANCE_FPX", "AMBANK_FPX", "ISLAM_FPX", "MUAMALAT_FPX", "BOC_FPX", "RAKYAT_FPX", "BSN_FPX", "CIMB_FPX", "HLB_FPX", "HSBC_FPX", "KFH_FPX", "MAYB2E_FPX", "MAYB2U_FPX", "OCBC_FPX", "PUBLIC_FPX", "RHB_FPX", "SCH_FPX", "UOB_FPX", "AFFIN_FPX_BUSINESS", "AGRO_FPX_BUSINESS", "ALLIANCE_FPX_BUSINESS", "AMBANK_FPX_BUSINESS", "ISLAM_FPX_BUSINESS", "MUAMALAT_FPX_BUSINESS", "BNP_FPX_BUSINESS", "CIMB_FPX_BUSINESS", "CITIBANK_FPX_BUSINESS", "DEUTSCHE_FPX_BUSINESS", "HLB_FPX_BUSINESS", "HSBC_FPX_BUSINESS", "RAKYAT_FPX_BUSINESS", "KFH_FPX_BUSINESS", "MAYB2E_FPX_BUSINESS", "OCBC_FPX_BUSINESS", "PUBLIC_FPX_BUSINESS", "RHB_FPX_BUSINESS", "SCH_FPX_BUSINESS", "UOB_FPX_BUSINESS", "BDO_ONLINE_BANKING", "BPI_ONLINE_BANKING", "UNIONBANK_ONLINE_BANKING", "BOC_ONLINE_BANKING", "CHINABANK_ONLINE_BANKING", "INSTAPAY_ONLINE_BANKING", "LANDBANK_ONLINE_BANKING", "MAYBANK_ONLINE_BANKING", "METROBANK_ONLINE_BANKING", "PNB_ONLINE_BANKING", "PSBANK_ONLINE_BANKING", "PESONET_ONLINE_BANKING", "RCBC_ONLINE_BANKING", "ROBINSONS_BANK_ONLINE_BANKING", "SECURITY_BANK_ONLINE_BANKING", ]  # noqa: E501
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
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):
        """DirectDebitChannelCode - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): Direct Debit Channel Code., must be one of ["BCA_KLIKPAY", "BCA_ONEKLIK", "BRI", "BNI", "MANDIRI", "BPI", "BPI_RECURRING", "BDO", "CIMBNIAGA", "MTB", "RCBC", "UBP", "UBP_EADA", "UBP_DEBIT_PULL", "CHINABANK", "BAY", "KTB", "BBL", "SCB", "KBANK_MB", "BAY_MB", "KTB_MB", "BBL_MB", "SCB_MB", "BDO_EPAY", "AFFIN_FPX", "AGRO_FPX", "ALLIANCE_FPX", "AMBANK_FPX", "ISLAM_FPX", "MUAMALAT_FPX", "BOC_FPX", "RAKYAT_FPX", "BSN_FPX", "CIMB_FPX", "HLB_FPX", "HSBC_FPX", "KFH_FPX", "MAYB2E_FPX", "MAYB2U_FPX", "OCBC_FPX", "PUBLIC_FPX", "RHB_FPX", "SCH_FPX", "UOB_FPX", "AFFIN_FPX_BUSINESS", "AGRO_FPX_BUSINESS", "ALLIANCE_FPX_BUSINESS", "AMBANK_FPX_BUSINESS", "ISLAM_FPX_BUSINESS", "MUAMALAT_FPX_BUSINESS", "BNP_FPX_BUSINESS", "CIMB_FPX_BUSINESS", "CITIBANK_FPX_BUSINESS", "DEUTSCHE_FPX_BUSINESS", "HLB_FPX_BUSINESS", "HSBC_FPX_BUSINESS", "RAKYAT_FPX_BUSINESS", "KFH_FPX_BUSINESS", "MAYB2E_FPX_BUSINESS", "OCBC_FPX_BUSINESS", "PUBLIC_FPX_BUSINESS", "RHB_FPX_BUSINESS", "SCH_FPX_BUSINESS", "UOB_FPX_BUSINESS", "BDO_ONLINE_BANKING", "BPI_ONLINE_BANKING", "UNIONBANK_ONLINE_BANKING", "BOC_ONLINE_BANKING", "CHINABANK_ONLINE_BANKING", "INSTAPAY_ONLINE_BANKING", "LANDBANK_ONLINE_BANKING", "MAYBANK_ONLINE_BANKING", "METROBANK_ONLINE_BANKING", "PNB_ONLINE_BANKING", "PSBANK_ONLINE_BANKING", "PESONET_ONLINE_BANKING", "RCBC_ONLINE_BANKING", "ROBINSONS_BANK_ONLINE_BANKING", "SECURITY_BANK_ONLINE_BANKING", ]  # noqa: E501

        Keyword Args:
            value (str): Direct Debit Channel Code., must be one of ["BCA_KLIKPAY", "BCA_ONEKLIK", "BRI", "BNI", "MANDIRI", "BPI", "BPI_RECURRING", "BDO", "CIMBNIAGA", "MTB", "RCBC", "UBP", "UBP_EADA", "UBP_DEBIT_PULL", "CHINABANK", "BAY", "KTB", "BBL", "SCB", "KBANK_MB", "BAY_MB", "KTB_MB", "BBL_MB", "SCB_MB", "BDO_EPAY", "AFFIN_FPX", "AGRO_FPX", "ALLIANCE_FPX", "AMBANK_FPX", "ISLAM_FPX", "MUAMALAT_FPX", "BOC_FPX", "RAKYAT_FPX", "BSN_FPX", "CIMB_FPX", "HLB_FPX", "HSBC_FPX", "KFH_FPX", "MAYB2E_FPX", "MAYB2U_FPX", "OCBC_FPX", "PUBLIC_FPX", "RHB_FPX", "SCH_FPX", "UOB_FPX", "AFFIN_FPX_BUSINESS", "AGRO_FPX_BUSINESS", "ALLIANCE_FPX_BUSINESS", "AMBANK_FPX_BUSINESS", "ISLAM_FPX_BUSINESS", "MUAMALAT_FPX_BUSINESS", "BNP_FPX_BUSINESS", "CIMB_FPX_BUSINESS", "CITIBANK_FPX_BUSINESS", "DEUTSCHE_FPX_BUSINESS", "HLB_FPX_BUSINESS", "HSBC_FPX_BUSINESS", "RAKYAT_FPX_BUSINESS", "KFH_FPX_BUSINESS", "MAYB2E_FPX_BUSINESS", "OCBC_FPX_BUSINESS", "PUBLIC_FPX_BUSINESS", "RHB_FPX_BUSINESS", "SCH_FPX_BUSINESS", "UOB_FPX_BUSINESS", "BDO_ONLINE_BANKING", "BPI_ONLINE_BANKING", "UNIONBANK_ONLINE_BANKING", "BOC_ONLINE_BANKING", "CHINABANK_ONLINE_BANKING", "INSTAPAY_ONLINE_BANKING", "LANDBANK_ONLINE_BANKING", "MAYBANK_ONLINE_BANKING", "METROBANK_ONLINE_BANKING", "PNB_ONLINE_BANKING", "PSBANK_ONLINE_BANKING", "PESONET_ONLINE_BANKING", "RCBC_ONLINE_BANKING", "ROBINSONS_BANK_ONLINE_BANKING", "SECURITY_BANK_ONLINE_BANKING", ]  # noqa: E501
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
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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
        try:
            self.value = value
        except ValueError:
            self.value = self.allowed_values[('value',)]['XENDIT_ENUM_DEFAULT_FALLBACK']
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        return self
