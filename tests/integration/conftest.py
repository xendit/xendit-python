import pytest
from xendit import Xendit


@pytest.fixture(scope="class")
def xendit_instance():
    return Xendit(
        "xnd_development_xRH6Hd5fYBmWWQSM61U5GAM5bTgwKui0AGdKji4FVQQLkovYHsgFm5DdyiNtCi8i"
    )
