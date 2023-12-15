def analyze_string(s):
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

def sort_words(sentence):
    words = sentence.split(", ")

    sorted_words = sorted(words)

    sorted_sequence = ", ".join(sorted_words)

    return sorted_sequence

input_sequence = input("Enter a comma-separated sequence of words: ")

result_sorted_sequence = sort_words(input_sequence)
print("Sorted sequence:", result_sorted_sequence)

result_digit, result_uppercase, result_lowercase, result_special = analyze_string(input_sequence)
print("Number of digits:", result_digit)
print("Number of uppercase characters:", result_uppercase)
print("Number of lowercase characters:", result_lowercase)
print("Number of special characters:", result_special)
