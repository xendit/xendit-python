from enum import Enum


class XenPlatformURLType(Enum):
    """Callback URL Type for xenPlatform"""

    INVOICE = "invoice"
    FVA_STATUS = "fva_status"
    FVA_PAID = "fva_paid"
    RO_FPC_PAID = "ro_fpc_paid"
    OVO_PAID = "ovo_paid"
    DISBURSEMENT = "disbursement"
    BATCH_DISBURSEMENT = "batch_disbursement"
