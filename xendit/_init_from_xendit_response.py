import functools


def _init_from_xendit_response(required, optional=[]):
    """Decorator to initialize class from XenditResponse

    Args:
      - required (list, optional): Required attribute in class. Defaults to [].
      - optional (list, optional): Optional attribute in class. Defaults to [].
    """

    def function_wrapper(func):
        @functools.wraps(func)
        def internal_wrapper(*args):
            wrapped_object = args[0]
            xendit_response = args[1]
            for required_attr in required:
                setattr(wrapped_object, required_attr, xendit_response[required_attr])
            for optional_attr in optional:
                try:
                    setattr(
                        wrapped_object,
                        optional_attr,
                        xendit_response.get(optional_attr, None),
                    )
                except KeyError:
                    pass
            return func(*args)

        return internal_wrapper

    return function_wrapper
