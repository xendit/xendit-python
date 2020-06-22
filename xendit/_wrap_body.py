def _wrap_body(function_locals, result_class):
    body = dict()
    for keys in result_class.required_attr:
        value = function_locals.get(keys, None)
        if value is not None:
            body[keys] = value
    for keys in result_class.optional_attr:
        value = function_locals.get(keys, None)
        if value is not None:
            body[keys] = value
    return body
