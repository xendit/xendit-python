def print_running_function(function_name: str, data: dict):
    if len(data) == 0:
        print(f"Running {function_name}()")
    else:
        print(f"Running {function_name}(")
        for key, value in data.items():
            if isinstance(value, str):
                print(f'    {key}="{value}",')
            else:
                print(f"    {key}={value},")
        print(")")
