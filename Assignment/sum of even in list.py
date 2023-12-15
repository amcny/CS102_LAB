def sum_of_even_numbers(numbers):
    even_sum = 0

    for num in numbers:
        if num % 2 == 0:
            even_sum += num

    return even_sum

input_list = [int(x) for x in input("Enter the list of numbers separated by space: ").split()]

result = sum_of_even_numbers(input_list)
print("Sum of even numbers:", result)