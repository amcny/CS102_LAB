def count_even_odd(numbers):
    even_count = odd_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count

input_list = [int(x) for x in input("Enter the list of numbers separated by space: ").split()]

even_count, odd_count = count_even_odd(input_list)
print("Count of even numbers:", even_count)
print("Count of odd numbers:", odd_count)