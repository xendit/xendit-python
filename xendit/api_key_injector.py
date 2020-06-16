class APIKeyInjector:
    def __init__(self, injected_class, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url
        self.injected_class = injected_class
        self.static_method_list = []
        for attr_name, value in injected_class.__dict__.items():
            if isinstance(value, staticmethod):
                self.static_method_list.append(attr_name)
        self.__dict__.update(injected_class.__dict__)

    def __getattribute__(self, name):
        if name == "static_method_list" or name not in self.static_method_list:
            attr = object.__getattribute__(self, name)
            return attr
        else:
            attr = object.__getattribute__(self.injected_class, name).__func__

            def inject_func_with_api_key(*args, **kwargs):
                kwargs["api_key"] = self.api_key
                kwargs["base_url"] = self.base_url
                result = attr(*args, **kwargs)
                return result

            return inject_func_with_api_key
