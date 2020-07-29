import pytest
from xendit import Xendit


@pytest.fixture(scope="class")
def xendit_instance():
    return Xendit(
        "xnd_development_xRH6Hd5fYBmWWQSM61U5GAM5bTgwKui0AGdKji4FVQQLkovYHsgFm5DdyiNtCi8i"
    )


@pytest.fixture(scope="class")
def xendit_instance_cardless_enabled():
    return Xendit(
        "xnd_development_s1Y7IemQRBU9IOE2Q0mWshKfcchUBDCHqCeKOBY3BBLwfuD562diFdYjiem7Ek0"
    )
