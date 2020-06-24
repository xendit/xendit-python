class BatchDisbursementItem:
    def __init__(
        self,
        amount,
        bank_code,
        bank_account_name,
        bank_account_number,
        description,
        external_id=None,
        email_to=[],
        email_cc=[],
        email_bcc=[],
    ):
        self.amount = amount
        self.bank_code = bank_code
        self.bank_account_name = bank_account_name
        self.bank_account_number = bank_account_number
        self.description = description
        if external_id is not None:
            self.external_id = external_id
        if len(email_to) > 0:
            self.email_to = email_to
        if len(email_cc) > 0:
            self.email_cc = email_cc
        if len(email_bcc) > 0:
            self.email_bcc = email_bcc

    def to_json(self):
        return vars(self)
