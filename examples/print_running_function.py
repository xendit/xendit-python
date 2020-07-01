def print_running_function(function_name: str, data: dict):
    print(f"Running {function_name}(")
    for key, value in data.items():
        print(f"  {key}={value},")
    print(")")
