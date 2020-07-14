class BaseQuery(dict):
    """Abstract class for query with object type"""

    def __init__(self, **kwargs):
        dict_params = {}
        for key, value in kwargs.items():
            if value is not None:
                dict_params[key] = value
        dict.__init__(self, dict_params)
