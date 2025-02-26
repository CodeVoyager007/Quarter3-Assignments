def identify_data_type(user_input):
    # Try to evaluate the input safely for complex types
    if user_input.startswith(('[', '{', '(')):
        try:
            value = eval(user_input)
            if isinstance(value, list):
                return f"Value: {value}, Type: List"
            elif isinstance(value, tuple):
                return f"Value: {value}, Type: Tuple"
            elif isinstance(value, dict):
                return f"Value: {value}, Type: Dictionary"
            elif isinstance(value, set):
                return f"Value: {value}, Type: Set"
        except Exception:
            pass

    # Check for simple types
    if user_input.isdigit():
        return f"Value: {user_input}, Type: Integer"
    try:
        float_value = float(user_input)
        return f"Value: {float_value}, Type: Float"
    except ValueError:
        pass

    if user_input.lower() in ['true', 'false']:
        return f"Value: {user_input}, Type: Boolean"

    # If no other type matches, it's a string
    return f"Value: '{user_input}', Type: String"


def main():
    print("Welcome to the Data Type Identifier!")
    while True:
        user_input = input("Enter a value (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        result = identify_data_type(user_input)
        print(result)


if __name__ == "__main__":
    main()
