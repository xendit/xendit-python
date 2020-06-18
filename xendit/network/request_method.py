from enum import Enum


class RequestMethod(Enum):
    """Enum of HTTP Method."""

    GET = "GET"
    POST = "POST"
    PATCH = "PATCH"
