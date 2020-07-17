from enum import Enum


class DirectDebitPaymentMethodType(Enum):
    """Payment method type for Create Payment Methods"""

    DEBIT_CARD = "DEBIT_CARD"
    BANK_ACCOUNT = "BANK_ACCOUNT"
