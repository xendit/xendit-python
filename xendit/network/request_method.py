from enum import Enum


class RequestMethod(Enum):
    """Enum of HTTP Method.

    Member:
    - RequestMethod.GET
    - RequestMethod.POST
    - RequestMethod.PATCH
    """

    GET = "GET"
    POST = "POST"
    PATCH = "PATCH"
