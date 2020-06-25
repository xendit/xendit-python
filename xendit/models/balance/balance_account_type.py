from enum import Enum


class BalanceAccountType(Enum):
    """Account Type for Get Balance"""

    CASH = "CASH"
    HOLDING = "HOLDING"
    TAX = "TAX"
