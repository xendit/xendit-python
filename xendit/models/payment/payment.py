from typing import List

from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params
from xendit.models._base_model import BaseModel
from xendit.models.paymentmethod.payment_method import PaymentMethod
from xendit.xendit_error import XenditError

class Payment(BaseModel):
    id: str
    payment_request_id: str
    reference_id: str
    customer_id: str
    currency: str
    amount: str
    country: str
    status: str
    payment_method: PaymentMethod
    channel_properties: dict
    payment_detail: dict
    failure_code: str
    created: str
    updated: str
    metadata: dict


class PaymentList(BaseModel):
    has_more: bool
    data: List[Payment]
