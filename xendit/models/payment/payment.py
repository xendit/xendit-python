from typing import List

from xendit.models._base_model import BaseModel, BaseListModel
from xendit.models.paymentmethod.payment_method import PaymentMethod


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


class PaymentList(BaseListModel):
    has_more: bool
    data: List[Payment]
