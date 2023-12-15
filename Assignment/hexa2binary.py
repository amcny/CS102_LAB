def hex_to_binary(hex_number):
    decimal_number = int(hex_number, 16)
    binary_number = bin(decimal_number)[2:]
    return binary_number

# Get user input for a hexadecimal number
hex_input = input("Enter a Hexadecimal number: ")

try:
    # Convert hexadecimal to binary
    binary_output = hex_to_binary(hex_input)
    print(f"The binary representation of {hex_input} is: {binary_output}")

except ValueError:
    print("Invalid hexadecimal number. Please enter a valid hexadecimal value.")