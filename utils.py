#utils.py

def validate_input(prompt, data_type, validation_function = None):
    while True:
        try:
            value = data_type(input(prompt))
            if validation_function and validation_function(value):
                raise ValueError
            return value
        except ValueError:
            print(f"Invalid input. please enter a valid {data_type.__name__}.")
