# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from xendit.customer.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from xendit.customer.model.account_bank import AccountBank
from xendit.customer.model.account_card import AccountCard
from xendit.customer.model.account_ewallet import AccountEwallet
from xendit.customer.model.account_otc import AccountOTC
from xendit.customer.model.account_pay_later import AccountPayLater
from xendit.customer.model.account_qr_code import AccountQRCode
from xendit.customer.model.address import Address
from xendit.customer.model.address_request import AddressRequest
from xendit.customer.model.address_status import AddressStatus
from xendit.customer.model.business_detail import BusinessDetail
from xendit.customer.model.country_code import CountryCode
from xendit.customer.model.create_customer400_response import CreateCustomer400Response
from xendit.customer.model.create_customer400_response_all_of import CreateCustomer400ResponseAllOf
from xendit.customer.model.customer import Customer
from xendit.customer.model.customer_request import CustomerRequest
from xendit.customer.model.employment_detail import EmploymentDetail
from xendit.customer.model.end_customer_status import EndCustomerStatus
from xendit.customer.model.error import Error
from xendit.customer.model.get_customer_by_reference_id200_response import GetCustomerByReferenceID200Response
from xendit.customer.model.get_customer_by_reference_id400_response import GetCustomerByReferenceID400Response
from xendit.customer.model.get_customer_by_reference_id400_response_all_of import GetCustomerByReferenceID400ResponseAllOf
from xendit.customer.model.identity_account_request import IdentityAccountRequest
from xendit.customer.model.identity_account_request_properties import IdentityAccountRequestProperties
from xendit.customer.model.identity_account_response import IdentityAccountResponse
from xendit.customer.model.identity_account_response_properties import IdentityAccountResponseProperties
from xendit.customer.model.identity_account_type import IdentityAccountType
from xendit.customer.model.individual_detail import IndividualDetail
from xendit.customer.model.kyc_document_request import KYCDocumentRequest
from xendit.customer.model.kyc_document_response import KYCDocumentResponse
from xendit.customer.model.kyc_document_sub_type import KYCDocumentSubType
from xendit.customer.model.kyc_document_type import KYCDocumentType
from xendit.customer.model.patch_customer import PatchCustomer
from xendit.customer.model.response_data_not_found import ResponseDataNotFound
from xendit.customer.model.update_customer400_response import UpdateCustomer400Response
from xendit.customer.model.update_customer400_response_all_of import UpdateCustomer400ResponseAllOf
