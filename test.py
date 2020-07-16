import time
from xendit import Xendit

amount = "50000"
phone = "08223322"

args = {
    "external_id": f"ovo-pay-{int(time.time())}",
    "amount": amount,
    "phone": phone,
}
xendit_instance = Xendit(
    "xnd_development_xRH6Hd5fYBmWWQSM61U5GAM5bTgwKui0AGdKji4FVQQLkovYHsgFm5DdyiNtCi8i"
)
xendit_instance.EWallet.create_ovo_payment(**args)
