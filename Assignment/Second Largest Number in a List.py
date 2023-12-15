def second_largest(numbers):

    if len(numbers) < 2:
        return "List must have at least two elements."

    sorted_numbers = sorted(numbers)

    second_largest_num = sorted_numbers[-2]

    return second_largest_num

num_list = [12, 45, 23, 67, 34, 98, 56, 21]
result = second_largest(num_list)

print("Original List:", num_list)
print("Second Largest Number:", result)