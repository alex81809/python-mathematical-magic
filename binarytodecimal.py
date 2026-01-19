def binary_to_decimal(binary_string):
    try:
        decimal_value = int(binary_string, 2)
        return decimal_value
    except ValueError:
        return "Invalid input! Please enter only 0s and 1s."

code = input("Enter the binary code (0s and 1s): ")
result = binary_to_decimal(code)

print(f"The decimal representation of {code} is: {result}")
