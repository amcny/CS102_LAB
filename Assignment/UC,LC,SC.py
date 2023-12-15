def count_characters(s):
    digit_count = uppercase_count = lowercase_count = special_count = 0

    for char in s:
        if '0' <= char <= '9':
            digit_count += 1
        elif 'A' <= char <= 'Z':
            uppercase_count += 1
        elif 'a' <= char <= 'z':
            lowercase_count += 1
        else:
            special_count += 1

    return digit_count, uppercase_count, lowercase_count, special_count

input_string = input("Enter a string: ")

digit_count, uppercase_count, lowercase_count, special_count = count_characters(input_string)
print("Number of digits:", digit_count)
print("Number of uppercase characters:", uppercase_count)
print("Number of lowercase characters:", lowercase_count)
print("Number of special characters:", special_count)