def is_palindrome_number(num):
    original_num = num
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10
    return original_num == reversed_num
def is_palindrome_string(string):
    original_string = string
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return original_string == reversed_string

number = int(input("Enter a number: "))
if is_palindrome_number(number):
    print(f"{number} is a palindrome number.")
else:
    print(f"{number} is not a palindrome number.")

string_input = input("Enter a string: ")
if is_palindrome_string(string_input):
    print(f"{string_input} is a palindrome string.")
else:
    print(f"{string_input} is not a palindrome string.")
