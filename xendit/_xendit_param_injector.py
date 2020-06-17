class _XenditParamInjector:
    def __init__(self, injected_class, api_key, base_url, http_client):
        self.api_key = api_key
        self.base_url = base_url
        self.http_client = http_client
        self.injected_class = injected_class
        self.static_method_list = []
        for attr_name, value in injected_class.__dict__.items():
            if isinstance(value, staticmethod):
                self.static_method_list.append(attr_name)
        self.__dict__.update(injected_class.__dict__)

    def __getattribute__(self, name):
        # We need to check whether the passed attribute/method are for APIKeyInjector or the injected class static method.
        # The injected class static method are stored on `static_method_list`, so we can check whether name is contained inside it.
        # To handle infinite loop with attribute checking (Because every attribute access will arrive here),
        # we need to also check whether `name` equals to `static_method_list`.

        if name == "static_method_list" or name not in self.static_method_list:
            attr = object.__getattribute__(self, name)
            return attr
        else:
            attr = object.__getattribute__(self.injected_class, name).__func__

            def inject_func_with_api_key(*args, **kwargs):
                kwargs["api_key"] = self.api_key
                kwargs["base_url"] = self.base_url
                kwargs["http_client"] = self.http_client
                result = attr(*args, **kwargs)
                return result

            return inject_func_with_api_key
