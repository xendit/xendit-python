"""
    The version of the XENDIT API: 1.45.2
"""

import json

class OpenApiException(Exception):
    """The base exception class for all OpenAPIExceptions"""


class ApiTypeError(OpenApiException, TypeError):
    def __init__(self, msg, path_to_item=None, valid_classes=None,
                 key_type=None):
        """ Raises an exception for TypeErrors

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list): a list of keys an indices to get to the
                                 current_item
                                 None if unset
            valid_classes (tuple): the primitive classes that current item
                                   should be an instance of
                                   None if unset
            key_type (bool): False if our value is a value in a dict
                             True if it is a key in a dict
                             False if our item is an item in a list
                             None if unset
        """
        self.path_to_item = path_to_item
        self.valid_classes = valid_classes
        self.key_type = key_type
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiTypeError, self).__init__(full_msg)


class ApiValueError(OpenApiException, ValueError):
    def __init__(self, msg, path_to_item=None):
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list) the path to the exception in the
                received_data dict. None if unset
        """

        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiValueError, self).__init__(full_msg)


class ApiAttributeError(OpenApiException, AttributeError):
    def __init__(self, msg, path_to_item=None):
        """
        Raised when an attribute reference or assignment fails.

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiAttributeError, self).__init__(full_msg)


class ApiKeyError(OpenApiException, KeyError):
    def __init__(self, msg, path_to_item=None):
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiKeyError, self).__init__(full_msg)


class XenditSdkException(OpenApiException):
    def __init__(self, raw_response=None, param_status=None, param_status_text=None):
        if raw_response is None:
            self.rawResponse = raw_response
            self.status = param_status or ""
            self.errorCode = ""
            self.errorMessage = param_status_text or ""
        else:
            raw_response = json.loads(raw_response.decode(encoding="utf-8")) if isinstance(raw_response, bytes) else raw_response
            self.rawResponse = raw_response

            self.status = param_status or ""
            if self.status == "" and "status" in raw_response and raw_response["status"] is not None:
                self.status = raw_response["status"]
            elif self.status == "" and "status_code" in raw_response and raw_response["status_code"] is not None:
                self.status = raw_response["status_code"]
            elif self.status == "" and "statusCode" in raw_response and raw_response["statusCode"] is not None:
                self.status = raw_response["statusCode"]


            if "error" in raw_response and raw_response["error"] is not None:
                self.errorCode = raw_response["error"]
            elif "error_code" in raw_response and raw_response["error_code"] is not None:
                self.errorCode = raw_response["error_code"]
            elif "errorCode" in raw_response and raw_response["errorCode"] is not None:
                self.errorCode = raw_response["errorCode"]
            else:
                self.errorCode = ""

            if "message" in raw_response and raw_response["message"] is not None:
                self.errorMessage = raw_response["message"]
            elif "error_message" in raw_response and raw_response["error_message"] is not None:
                self.errorMessage = raw_response["error_message"]
            elif "errorMessage" in raw_response and raw_response["errorMessage"] is not None:
                self.errorMessage = raw_response["errorMessage"]
            else:
                self.errorMessage = param_status_text or ""

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "Status Code: {0}\n"\
                        "Error Code: {1}\n"\
                        "Error Message: {2}\n"\
                        "Raw Response: {3}\n".format(self.status, self.errorCode, self.errorMessage, self.rawResponse)
        return error_message

def render_path(path_to_item):
    """Returns a string representation of a path"""
    result = ""
    for pth in path_to_item:
        if isinstance(pth, int):
            result += "[{0}]".format(pth)
        else:
            result += "['{0}']".format(pth)
    return result
