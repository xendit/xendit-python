class _XenditParamInjector:
    """Builder class to inject parameters (api_key, base_url, http_client) to feature class"""

    @staticmethod
    def instantiate(injected_class, params):
        """Inject every static method in `injected_class` with provided parameters.

        Args:
          - injected_class (class): Class that will be injected
          - params (tuple): Parameters that will be injected. Consist of (api_key, base_url, http_client)

        Return:
          injected_class
        """

        class Inject(injected_class):
            """Copy of the injected class. Need to use this to make sure that we do not inject a package-wide class"""

            pass

        for keys, value in vars(injected_class).items():
            if type(value) == staticmethod and not keys.startswith("_"):
                _XenditParamInjector._inject_function(Inject, params, keys, value)
        return Inject

    @staticmethod
    def _inject_function(injected_class, params, func_name, func_value):
        """Inject `func_name` function with params"""
        api_key, base_url, http_client = params
        attr = func_value.__func__

        def inject_func_with_api_key(*args, **kwargs):
            kwargs["api_key"] = api_key
            kwargs["base_url"] = base_url
            kwargs["http_client"] = http_client
            result = attr(*args, **kwargs)
            return result

        setattr(injected_class, func_name, staticmethod(inject_func_with_api_key))
