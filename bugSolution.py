def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            return "Unhandled TypeError"
        else:
            return "Invalid input types"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example usage
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Division by zero
print(function_with_uncommon_error(10, "hello")) # Output: Invalid input types
print(function_with_uncommon_error("hello",10)) # Output: Invalid input types
print(function_with_uncommon_error(10.5,2.0)) # Output: 5.25